#main.py # Path: main.py
import csv
import datetime
import keyword
from scraper.hacker_news_scraper import search_hn_articles
from scraper.darkreading_scraper import scrape_darkreading
from scraper.securityweeks_scraper import scrape_securityweek
import configparser
from utils import display_all_article, print_results, save_results_to_json2
from datetime import datetime
import re


# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')


# Call the custom scraper functions for each website
all_articles = []

# Define the keywords as a list, every keyword will be searched on each website


# keywords = [
#     "canada cybersecurity",
#     "tiktok china",
#     "spy hacker china",
#     "ukraine war",
#     "Security vulnerabilities Azure",
#     "vulnerabilities Microsoft windows 10",
#     "vulnerabilities cisco",
#     "Emerging Technologies",
#     "Security Best Practices",
#     "Security Threats and Vulnerabilities",
#     "cyberattacks ransomware news",
#     "cyber security news",
#     "cyber attack updates",
#     "latest ransomware incidents",
#     "network security trends",
#     "artificial intelligence developments",
#     "internet of things vulnerabilities",
#     "cloud computing breaches",
#     "data privacy regulations",
#     "government surveillance laws",
#     "social engineering attacks",
#     "hacking techniques and tools",
#     "cyber warfare updates",
#     "software vulnerabilities and patches",
#     "data breaches and leaks",
#     "online fraud prevention tips",
#     "malware detection and prevention",
#     "cybersecurity career advice",
#     "threat intelligence updates",
#     "cyber insurance news",
#     "web application security best practices",
#     "mobile device security tips",
#     "insider threat prevention strategies",
#     "cyber risk assessments and management",
#     "digital forensics and incident response updates",
#     "news about social media"
#     "onlyfans "
#     "spyware cyber crime "
#     "ransomware evolution gpt "
#     "chat gpt malware "
#     "ai malware evloving "
#     "ai chaging world "
# ]
keywords = ["data breaches western"]
            



# Call the custom scraper functions for each website
#Hackernews
try:
    hackernews_keywords = keywords
    for k in keywords:
        all_articles.extend(search_hn_articles([k]))
except Exception as e:
    print("An error occurred while scraping Hacker News:", str(e))
#show the results in the console
display_all_article(all_articles,"Hacker News")
#save in the json file 
save_results_to_json2(articles=all_articles, filename='articleBD.json')
#clear the list 
all_articles.clear()
#continue with the other website

#Darkreading
try:
    # keywords = input("Enter a keyword to search articles on Dark Reading: ")
    # keywords = "+".join(keywords.split())
    dr_keywords = ['+'.join(k.split()) for k in keywords]
    for k in dr_keywords:   
        all_articles.extend(scrape_darkreading([k], config))
except Exception as e:
    print("An error occurred while scraping Dark Reading:", str(e))
#show the results in the console
display_all_article(all_articles,"Dark Reading")
#save in the json file 
save_results_to_json2(articles=all_articles, filename='articleBD.json')
#clear the list 
all_articles.clear()
#continue with the other website


#Securityweek
try:
    # keywords = input("Enter a keyword to search articles on Security Week: ")
    # keywords = "+".join(keywords.split())

    sw_keywords = ['+'.join(k.split()) for k in keywords]
    for k in sw_keywords:
        all_articles.extend(scrape_securityweek([k], config))
except Exception as e:
    print("An error occurred while scraping Security Week:", str(e))
#show the results in the console
display_all_article(all_articles,"Security Week")
#save in the json file 
save_results_to_json2(articles=all_articles, filename='articleBD.json')
#clear the list 
all_articles.clear()
#continue with the other website
#verify if the list is empty
if not all_articles:
    print("The list is empty")


#show the results in the console
display_all_article(all_articles,"ZDNet")
#save in the json file 
save_results_to_json2(articles=all_articles, filename='articleBD.json')
#clear the list 
all_articles.clear()
#verify if the list is empty
if not all_articles:
    print("The list is empty")


