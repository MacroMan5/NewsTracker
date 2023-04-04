
# utils.py
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import contextlib
from typing import List, Dict
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re
import csv 
import json
import threading
from bs4 import NavigableString

############### functions for search_articles2.py #####################
def pre_classify_articles(articles, query):
    pre_classified = []

    for article in articles:
        if any(word.lower() in article['title'].lower() for word in query.split()):
            pre_classified.append(article)

    return pre_classified

#score articles based on how many times the query words appear in the content 
def score_articles(pre_classified, query):
    #split the query into individual words
    query_words = query.lower().split()
    scored_articles = []
    #loop through the articles that have at least one word in the title
    for article in pre_classified:
        score = 0
        word_count = {word: 0 for word in query_words}

        for word in query_words:
            count = article['content'].lower().count(word)
            if count > 0:
                word_count[word] = min(count, 3)
                score += word_count[word]
        #add a bonus score if multiple words are in the content
        bonus = sum(1 for count in word_count.values() if count > 0)
        if bonus >= 2:
            score += 3 + (bonus - 2) * 5
#         This line calculates and adds the bonus score to the article's score. The bonus score calculation is as follows:
        # If there are 2 unique query words in the content, the bonus score is 3 (3 + (2 - 2) * 5 = 3).
        # If there are 3 unique query words in the content, the bonus score is 8 (3 + (3 - 2) * 5 = 7).
        # If there are 4 or more unique query words in the content, the bonus score is 13 (3 + (4 - 2) * 5 = 10), and so on.
        # The bonus

        #add the article to the list of scored articles if it has at least 3 points
        if score >= 3:
            article_score = {
                "title": article["title"],
                "date": article["date"],
                "url": article["url"],
                "score": score
            }
            scored_articles.append(article_score)

    return scored_articles

#display the articles that have at least 3 points
def display_scored_articles(scored_articles):
    sorted_articles = sorted(scored_articles, key=lambda x: x["score"], reverse=True)

    for article in sorted_articles:
        print(f"{article['title']} (Date: {article['date']}, Score: {article['score']})")
        print(f"URL: {article['url']}\n")

#search the articles and score them
def search(query, articles):
    pre_classified = pre_classify_articles(articles, query)
    scored_articles = score_articles(pre_classified, query)
    #display_scored_articles(scored_articles) used to show in the terminal 
    return scored_articles #returned for the GUI interface 


def clean_date_string(date_str: str) -> str:
    """
    Given a date string in the format "Month Day, Year", convert it to
    ISO format (YYYY-MM-DD).
    """
    dt = datetime.strptime(date_str, '%B %d, %Y')
    return dt.date().isoformat()

def scrape_url(url: str, **kwargs) -> str:
    """
    Given a URL, return the HTML content of the page.
    """
    response = requests.get(url, **kwargs)
    response.raise_for_status()
    return response.text

def handle_http_error(response):
    """
    Raises an exception for any HTTP errors encountered during a request
    """
    response.raise_for_status()

import csv

def init_driver_scraping():
    chrome_path = "/path/to/chromedriver"
    service = Service(chrome_path)
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-notifications')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def print_results(articles):
    print(f"\nTotal articles found: {len(articles)}")
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Date: {article['date']}")
        print(f"URL: {article['url']}")
        print()

# def save_results_to_csv(articles, filename):
#     with open(filename, 'a', newline='', encoding='utf-8') as f:
#         writer = csv.writer(f, delimiter='\t', quotechar='"', lineterminator='\n', dialect='excel-tab')
#         for article in articles:
#             title = article['title']
#             url = f'=HYPERLINK("{article["url"]}'
#             # remove non-printable characters from date string
#             date = ''.join(filter(lambda x: x.isprintable(), article['date']))
#             try:
#                 formatted_date = datetime.strptime(date, '%b %d, %Y').strftime('%m/%d/%Y')
#             except ValueError:
#                 formatted_date = 'N/A'
#             writer.writerow([title, url, formatted_date])

def save_results_to_json(articles, filename):
    import json
    with open(filename, 'a', newline='') as f:
        #formatage date 
        for article in articles:
            date = ''.join(filter(lambda x: x.isprintable(), article['date']))
            try:
                formatted_date = datetime.strptime(date, '%b %d, %Y').strftime('%m/%d/%Y')
            except ValueError:
                formatted_date = 'N/A'
            article['date'] = formatted_date
        json.dump(articles, f)



import os
import json

def save_results_to_json2(articles, filename):
    # Load existing articles from JSON file
    existing_articles = []
    if os.path.isfile(filename):
        with open(filename, 'r') as f:
            existing_articles = json.load(f)
    existing_titles = set([article['title'] for article in existing_articles])
    
    # Format new articles and add them to the list
    new_articles = []
    for article in articles:
        # Format the date
        date = ''.join(filter(lambda x: x.isprintable(), article['date']))
        try:
            formatted_date = datetime.strptime(date, '%b %d, %Y').strftime('%m/%d/%Y')
        except ValueError:
            formatted_date = 'N/A'
        article['date'] = formatted_date
        
        # Check if the title is already in the list
        if article['title'] not in existing_titles:
            new_articles.append(article)
            existing_titles.add(article['title'])
    
    # Append the new articles to the existing articles and write to the JSON file
    all_articles = existing_articles + new_articles
    with open(filename, 'w') as f:
        json.dump(all_articles, f, indent=4)





#
def count_query_words_in_text(query, article):
    print(query)
    print(article)
    text = article['content']
    query_parts = query.lower().split()
    text_parts = text.lower().split()
    return sum(text_parts.count(part) for part in query_parts)


def search_and_score_articles(query, data):
    query_parts = query.lower().split()

    # # Check if any part of the query is present in the title
    # def title_contains_query_parts(title, query_parts):
    #     return any(part in title.lower() for part in query_parts)

    # Count occurrences of query words in the text, with a maximum of 3 per word
    def count_words_with_limit(query, article, limit=4):
        text = article['content']
        query_parts = query.lower().split()
        text_parts = text.lower().split()
        return sum(min(text_parts.count(part), limit) for part in query_parts)

    # Add bonus score if all query words are present in the text
    def calculate_bonus(query, article):
        text = article['content']
        query_parts = query.lower().split()
        text_lower = text.lower()
        if all(part in text_lower for part in query_parts):
            return 6
        return 0

    # # Initialize results with 0 score for each item that has a matching title
    # results = [{"item": item, "score": 0} for item in data if title_contains_query_parts(item["title"], query_parts)]
    results = []
    for item in data:
        try:
            title_score = count_query_words_in_text(query_parts, item['title'])
        except TypeError:
            print(f"Error processing item: {item}")
            continue
        content_score = count_words_with_limit(query, item)
        bonus_score = calculate_bonus(query, item)
        total_score = title_score + content_score + bonus_score


        if total_score > 0:
            results.append({"item": item, "score": total_score})

    # Sort results by score, then by date
    results.sort(key=lambda x: (-x["score"], -x["item"]["date"]), reverse=True)
    print("Results:", results)

    # Return top 20 results with scores
    return [{"item": result["item"], "score": result["score"]} for result in results[:20]]






# #algorythme de recherche et de scoring for better search result 
# def search_and_score_articles(query, data):
#     query_parts = query.lower().split()

#     # Check if any part of the query is present in the title
#     def title_contains_query_parts(title, query_parts):
#         return any(part in title.lower() for part in query_parts)

#     # Count occurrences of query words in the text, with a maximum of 5 per word
#     def count_words_with_limit(query, text, limit=5):
#         query_parts = query.lower().split()
#         text_parts = text.lower().split()
#         return sum(min(text_parts.count(part), limit) for part in query_parts)

#     # Add bonus score if all query words are present in the text
#     def calculate_bonus(query, text):
#         query_parts = query.lower().split()
#         text_lower = text.lower()
#         if all(part in text_lower for part in query_parts):
#             return 7
#         return 0

#     # Initialize results with 0 score for each item that has a matching title
#     results = [{"item": item, "score": 0} for item in data if title_contains_query_parts(item["title"], query_parts)]

#     for result in results:
#         text = fetch_article_text(result["item"]["url"])
#         print(f"Text for {result['item']['title']}: {text}")  # Debugging print statement
#         word_count = count_words_with_limit(query, text)
#         bonus_score = calculate_bonus(query, text)
#         result["score"] = word_count + bonus_score
#         print(f"Word count: {word_count}, Bonus score: {bonus_score}")  # Debugging print statement

#     # Sort results by score, then by date
#     results.sort(key=lambda x: (-x["score"], x["item"]["date"]), reverse=True)

#    # Return top 10 results along with their scores
#     return [{"item": result["item"], "score": result["score"]} for result in results[:10]]


#function to load the json file
def load_existing_articles(filename='articleBD.json'):
    try:
        with open(filename, 'r') as f:
            articles = json.load(f)
    except FileNotFoundError:
        articles = []
    
    return articles


#function to check if the article is already in the json file with api 
def article_exists(url, existing_articles):
    for article in existing_articles:
        if article['url'] == url:
            return True
    return False

def init_driver():
    options = Options()
    # Set the headless mode using the new method
    options.add_argument('--headless')
    
    driver = webdriver.Chrome(executable_path='path/to/chromedriver.exe', options=options)
    return driver


def get_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Remove script and style elements from the soup object
            for script in soup(["script", "style"]):
                script.decompose()

            content = soup.get_text(strip=True, separator=' ')

            # Optionally, replace consecutive whitespaces with a single space
            content = re.sub(r'\s+', ' ', content)

            # Check if content is text
            if not isinstance(content, str):             
                return ''

            return content
        else:
            return ''
    except Exception as e:
        print(f"Error getting content for URL {url}: {str(e)}")
        return ''
    


def get_content_nojavascript(url, div_class):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content_div = soup.find('div', class_=div_class)
            
            if content_div is None:
                print(f"No div with class '{div_class}' found for URL {url}")
                return ''

            # Find all <p> and <h2> tags within the content_div
            p_tags = content_div.find_all('p') # type: ignore
            h2_tags = content_div.find_all('h2') # type: ignore

            # Extract the text from the tags and join them in a single string
            content = ' '.join([tag.get_text(strip=True) for tag in p_tags + h2_tags])

            return content
        else:
            return ''
    except Exception as e:
        print(f"Error getting content for URL {url}: {str(e)}")
        return ''

# Test the function with an example URL
# url = "https://www.darkreading.com/endpoint/what-covid-19-teaches-us-about-social-engineering"
# div_class = "article-content"  # Replace this with the desired div class
# content = get_content_nojavascript(url, div_class)
# print(url)
# print(content)



def get_content_selenium(url, div_class):
    driver = init_driver()
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content_div = soup.find('div', class_=div_class)

        p_tags = content_div.find_all('p')  # type: ignore
        h2_tags = content_div.find_all('h2')  # type: ignore

        content = ' '.join([tag.get_text(strip=True) for tag in p_tags + h2_tags])

        driver.quit()
        return content
    except Exception as e:
        print(f"Error getting content for URL {url}: {str(e)}")
        return ''

# # Test the function with the example URLs
# url2 = "https://www.securityweek.com/free-all-no-crippling-cyberattacks-ukraine-war/"
# div_class2 = "zox-post-main"
# content2 = get_content_selenium(url2, div_class2)
# print("                               ")
# print(url2)
# print(content2)










# I want to update de code to show the 10 best result(high scoring) for the search query 
# class by score then date 
# add a maximum score of 5 per words in the paragraph 
# add +7 score if all the words in the query are in the paragraph at least once 
# show the score of each result in the window after the url in the reuslt display
#then comment the code 



def display_all_article(all_articles, website):    
    # Display the total number of articles found
    print(f"\nTotal articles found: {len(all_articles)} on {website}")
    # Step 2: Print the results
    print_results(all_articles)
