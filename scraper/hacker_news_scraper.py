
from bs4 import ResultSet
import requests
from bs4 import BeautifulSoup
from utils import get_content, load_existing_articles,article_exists

def search_hn_articles(keywords):
    # Set Algolia API endpoint and parameters
    api_endpoint = 'https://hn.algolia.com/api/v1/search'
    articles = []

    # Combine keywords into a single query with OR operator
    query = ' OR '.join(keywords)

    # Set query parameter for current keyword
    params = {'query': query}

    # Send GET request to Algolia API
    response = requests.get(api_endpoint, params=params)
    print(response.url)

    # Load existing articles from JSON file
    existing_articles = load_existing_articles()

    # Parse JSON response and extract article information
    number_articles = 0
    if response.status_code == 200:
        results = response.json()['hits']
        for result in results[:10]: # Only get the first 10 articles
            title = result['title']
            date = result['created_at'].split('T')[0]
            url = result['url'] if 'url' in result else f'https://news.ycombinator.com/item?id={result["objectID"]}'

            # Check if article has all the required fields
            if not title or not url:
                print(f'Error parsing article: {title} , URL: {url}')
                continue
            # Check if article is already in the BD
            if article_exists(url, existing_articles):
                print("Article already exists in the JSON file.")
                continue

            #Fetch the article content OLD VERSION
            # content_response = requests.get(url)
            # content_soup = BeautifulSoup(content_response.text, 'html.parser')

            # if content_soup.body:
            #     content = content_soup.body.get_text(' ')
            # else:
            #     content = ''
            #Fetch the article content NEW VERSION
            
            content = get_content(url)
            if not content:
                print (f"Error getting content for article: {title}")
                continue

            # Add article to list of articles
            if not content == '':                  
                articles.append({"title": title, "date": date, "url": url, "content": content})
            # Increment number of articles found
            number_articles += 1
            print(f"Number of article founded {number_articles}")
    else:
        print(f'Error searching for articles on Hacker News: {response.status_code}')

    return articles

# from utils import save_results_to_json2


# keywords = ["python flaws", "tiktok china war","vmware esxi" ]
# print(keywords)
# for keyword in keywords:
#     all_article = search_hn_articles([keyword])
#     save_results_to_json2(all_article, 'hacker_news.json')





# Put the results in a json file if the title is not already in the json file





# keywords = ["python vulnerability", "tiktoc china"]
# for k in keywords:
# https://hn.algolia.com/?{keywords}
# https://hn.algolia.com/?qpython+flaws
# my research was python hacker
# So i want to postrequest this kind of link and get the results of the search
# I want to get the results of the search TITLE, DATE, URL
# here is the exemple HTML for an articles founds with python + flaws
# lets make a function to get the results of the search
# with a paramater of a list of keywords to serach for example
# keywords = ["python vulnerability", "tiktoc china"]
# output in the url POST request should be like that
