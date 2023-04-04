#darkreading_scraper.py
from subprocess import TimeoutExpired
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from utils import get_content_nojavascript, init_driver_scraping, load_existing_articles, article_exists
import traceback


def scrape_darkreading(keywords,config):
    all_articles = []
    # Load existing articles from JSON file
    existing_articles = load_existing_articles()
    try:
        # set up Selenium Chrome driver
        driver = init_driver_scraping()
        # navigate to Dark Reading search page
        # Join the keywords with +
        keywords = '+'.join(keywords)
        # Remove brackets and quotes
        keywords = keywords.replace('[','').replace(']','').replace('\'','').replace('\"','')


        url = f"https://www.darkreading.com/search?q={keywords}"
        print(f"Scraping {url}")
        driver.get(url)

      
        # wait for page to load
        wait = WebDriverWait(driver, 1)
        try:
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "article.search-result-item")))
        except TimeoutException:
            print("No search results found for the entered keywords.")
            return all_articles
       
        # scrape articles
        articles = driver.find_elements(By.CSS_SELECTOR, "article.search-result-item")
        num_articles = 1
        for article in articles:
            title_element = article.find_element(By.CSS_SELECTOR, "div.title div.summary h2")
            if title_element:
                title = title_element.get_attribute("innerText").strip()
            else:
                title = "N/A"
           
      
            date_element = article.find_element(By.CSS_SELECTOR, "div.info div.time")
            if date_element:
                date = date_element.get_attribute("innerText").strip()
            else:
                date = "N/A"
                
            url = article.find_element(By.TAG_NAME, "a").get_attribute("href")


            # check if article exists in JSON file
            if article_exists(url, existing_articles):
                print(f"Article already exists in the JSON file.{title}")
                continue # move on to the next article
             
            # get article content from the article page with get_content function from utils.py file using BeautifulSoup
            content = get_content_nojavascript(url,"article-content")

            if not content:
                print (f"Error getting content for article: {title}")
                continue
            # Add article to list of articles
            if not content == '':

                all_articles.append({"title": title, "date": date, "url": url, "content": content})

            print(f"Number of article founded {num_articles} title: {title}")
            # increment number of articles
            num_articles += 1 

            if num_articles >= 10:
                break
        # close the driver
        driver.quit()
        return all_articles
    
    except Exception as e:
        print("An error occurred:", str(e))
        traceback.print_exc()
        return all_articles


#darkreading_scraper.py unique testing 
# all_articles = scrape_darkreading(["cybersecurity"],None)
# print(all_articles)



    #full article div class = offset-md-4 col-md-8 p-0 
    #inside that there is a article class = search-result-item 
    #inside that there is my a href = url  
    #then div class = title i found the title into div class = summary the title is in text inside h2 
    #this is the title a wanna get
    #then the date is in div class = info and inside that class= author and time then  div class = time
    #this is the date i wanna get