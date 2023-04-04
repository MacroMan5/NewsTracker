
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from configuration import selectors, websites

def scrape_website(website):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(website, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error scraping {website}: {str(e)}")
        return []

    soup = BeautifulSoup(response.content, "lxml")

    domain = website.split("//")[-1].split("/")[0]
    domain = domain.replace("www.", "")

    # Get the appropriate selectors from the configuration dictionary
    sel = selectors.get(domain)

    if not sel:
        print(f"Error: No selectors found for {domain}")
        return []

    # Find the relevant elements for URL
    print(f"Extracting articles for {website}...")
    urls = []
    url_elements = soup.select(sel["url"])
    for url_element in url_elements:   
        urls.append(url_element["href"])
        
        # if domain == "wired.com" and "/category/security/" in website:
        #     url = f"https://www.wired.com{url_element["href"]}"
        #     urls.append(url)

    print(f"Found {len(urls)} articles.")


    return urls #return the list of all the url found on the websites
#testing the function scrape_website
url_list = []
for website in websites:
    url_list = scrape_website(website)
    for i in url_list: # print the list of urls skip line for each url in the 
        print(i)


def scrape_article(url, selectors):
    all_article = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error scraping {url}: {str(e)}")
        return None

    soup = BeautifulSoup(response.content, "lxml")

    title_element = soup.select_one(selectors["title"])
    title = title_element.text.strip() if title_element else "No title found"

    content_element = soup.select_one(selectors["content"])
    content = content_element.text.strip() if content_element else "No content found"

    # Assuming that the date selector is added to the selectors dictionary
    date_element = soup.select_one(selectors["date"])
    date_text = date_element.text.strip() if date_element else "No date found"
    try:
        date = datetime.strptime(date_text, "%Y-%m-%d")
    except ValueError:
        date = None

    all_article.append({"title": title, "content": content, "date": date})

    return all_article



# def scrape_article_found(url, selector):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
#     }
#     try:
#         response = requests.get(url, headers=headers)
#         response.raise_for_status()
#     except requests.RequestException as e:
#         print(f"Error scraping {url}: {str(e)}")
#         return {}

#     soup = BeautifulSoup(response.content, "lxml")
#     with open("test.html", "w", encoding="utf-8") as f:
#         f.write(soup.prettify())
#     article = {}

#     # Extract the title
#     title_element = soup.select_one(selector["title"])
#     article["title"] = title_element.text if title_element else ""

#     # Extract the URL
#     article["url"] = url

#     # Extract the date
#     date_element = soup.select_one(selector["date"])
#     article["date"] = date_element.text.strip() if date_element else ""

#     # Extract the content
#     content_element = soup.select_one(selector["content"])
#     paragraphs = content_element.find_all("p")
#     content = "\n".join(p.text.strip() for p in paragraphs)
#     article["content"] = content

#     return article



