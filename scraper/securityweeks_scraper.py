#securityweeks_scraper.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import get_content_selenium, load_existing_articles, article_exists
from selenium.common.exceptions import NoSuchElementException, TimeoutException


#function to scrap the website https://www.securityweek.com/
def scrape_securityweek(keywords,config):
    # Load existing articles from JSON file
    existing_articles = load_existing_articles()
    all_articles = []
    # set up Selenium Chrome driver
    chrome_path = "/path/to/chromedriver"
    service = Service(chrome_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-notifications')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)

    # Join the keywords with +
    keywords = '+'.join(keywords)
    # Remove brackets and quotes
    keywords = keywords.replace('[','').replace(']','').replace('\'','').replace('\"','')


    # navigate to SecurityWeek search page
    url = f"https://www.securityweek.com/?s={keywords}"
    print(f"Scraping {url}")
    driver.get(url)

    # wait for page to load
    wait = WebDriverWait(driver, 1)
    try:
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.zox-art-text-cont")))
    except TimeoutException:
        print("Timeout waiting for page to load.")
        return all_articles
    # scrape articles
    articles = driver.find_elements(By.CSS_SELECTOR, "div.zox-art-text-cont")
    num_articles = 1
    for article in articles:       
        try:
            title_element = article.find_element(By.CSS_SELECTOR, "div.zox-art-title a")
            title = title_element.get_attribute("innerText").strip()     
            url = title_element.get_attribute("href")   
        except NoSuchElementException:
            continue

        
        try:
            date_element = article.find_element(By.CSS_SELECTOR, "span.zox-byline-date")
            date = date_element.text.strip()
        except NoSuchElementException:
            date = "N/A"

        #check if article already exists in the JSON file
        if article_exists(url, existing_articles):
            print(f"Article already exists in the JSON file.{title}")
            continue

        #get content from the url of the article 
        content = get_content_selenium(url,"zox-post-main")
        if not content:
                print (f"Error getting content for article: {title}")
                continue # skip to next article
        

        # Add article to list of articles
        if not content == '':

            all_articles.append({"title": title, "date": date, "url": url, "content": content})
            print(f"Number of article founded {num_articles} title: {title}")
        # increment number of articles
        num_articles += 1 

        if num_articles >= 10:
            break

        # Close the driver
        driver.quit()

    return all_articles






#lets make another function to scrap the website https://www.securityweek.com/ 
# the get request is  https://www.securityweek.com/?s={keywords[0]}+{keywords[1]}
# the result are located in <div class="zox-art-text-cont"> 
# inside that we found the title <div class="zox-art-title">
# there is the URL <a href="https://www.securityweek.com/severe-azure-vulnerability-led-to-unauthenticated-remote-code-execution/" rel="bookmark">
# THERE IS the title  <h2 class="zox-s-title2">Severe Azure Vulnerability Led to Unauthenticated Remote Code Execution</h2>
#then the date is in <span class="zox-byline-date">
# <i class="far fa-clock"></i>
# March 31, 2023 </span>