# selectors = {
#     "thehackernews.com": {
#         "title": "h2.home-title",
#         "url": "a.story-link",
#         "date": "span.h-datetime",
#         "content": "div.home-desc"
#     },
#     "krebsonsecurity.com": {
#         "title": "h2.entry-title a",
#         "url": "h2.entry-title a",
#         "date": "span.date.updated",
#         "content": "div.entry-content"
#     },
#     "techcrunch.com": {
#         "title": "h2.post-block__title",
#         "url": "a.post-block__title__link",
#         "date": "time.river-byline__full-date-time",
#         "content": "div.post-block__content"
#     },
#     "darkreading.com": {
#         "title": "a.wrap-latest-item div.article-detail span.article-title",
#         "url": "a.wrap-latest-item",
#         "date": "div.article-byline p.date",
#         "content": "a.wrap-latest-item div.article-detail p.article-sumary"
#     },
#     "securityweek.com": {
#         "title": "div.zox-art-text div.zox-art-title a h2.zox-s-title3",
#         "url": "div.zox-art-text div.zox-art-title a",
#         "date": "NA",
#         "content": "div.theiaPostSlider_preloadedSlide"
#     },
#     "wired.com/category/security": {
#         "title": "a.SummaryItemHedLink-ciaMYZ h3.SummaryItemHedBase-eaxFWE",
#         "url": "a.SummaryItemHedLink-ciaMYZ",
#         "date": "NA",
#         "content": "div.SummaryItemDek-dyrmLu"
#     },
#     "bleepingcomputer.com": {
#         "title": "div.bc_latest_news_text h4 a",
#         "url": "div.bc_latest_news_text h4 a",
#         "date": "li.bc_news_date",
#         "content": "p.ltr"
#     }
# }
selectors = {
    "thehackernews.com": {
        "title": "h2.home-title",
        "url": "a.story-link",
        "content": "div.home-desc"
    },
    "krebsonsecurity.com": {
        "title": "h2.entry-title a",
        "url": "h2.entry-title a",
        "content": "div.entry-content"
    },
    "techcrunch.com": {
        "title": "h2.post-block__title",
        "url": "a.post-block__title__link",
        "content": "div.post-block__content"
    },
    "darkreading.com": {
        "title": "div.wrap-latest-item div.article-detail span.article-title",
        "url": "div.wrap-latest-item",
        "content": "a.wrap-latest-item div.article-detail p.article-sumary"
    },
    "securityweek.com": {
        "title": "div.zox-art-text div.zox-art-title a h2.zox-s-title3",
        "url": "div.zox-art-text div.zox-art-title a",
        "content": "div.theiaPostSlider_preloadedSlide"
    },
    "wired.com/category/security/": {
        "title": "a.SummaryItemHedLink-ciaMYZ h3.SummaryItemHedBase-eaxFWE",
        "url": "a.SummaryItemHedLink-ciaMYZ",
        "content": "div.SummaryItemDek-dyrmLu"
    },
    "bleepingcomputer.com": {
        "title": "div.bc_latest_news_text h4 a",
        "url": "div.bc_latest_news_text h4 a",
        "content": "p.ltr"
    }
}

websites = [
"https://www.thehackernews.com/",
"https://www.krebsonsecurity.com/",
"https://www.techcrunch.com/",
"https://www.darkreading.com/",
"https://www.securityweek.com/",
"https://www.wired.com/category/security/",
"https://www.bleepingcomputer.com/",
]













# all_articles = []
# for website in websites:
#     try:
#         articles = scrape_articles(website)
#         all_articles.extend(articles)
#     except Exception as e:
#         print(f"Error scraping {website}: {e}")

# # Save the articles to a JSON file
# with open('articleBD.json', 'w') as f:
#     json.dump(all_articles, f, indent=4)


# selector for hackernew 
# title <h2 class="home-title"
# url <a class="story-link" href="https://thehackernews.com/2023/04/western-digital-hit-by-network-security.html">
# time <span class="h-datetime"><i class="icon-font icon-calendar"></i>Apr 03, 2023</span>
# content  <div class="home-desc"> content 



# # selector for krebsonsecurity exemple 
# title and url same tag look like <h2 class="entry-title"> <a href="https://krebsonsecurity.com/2023/03/german-police-raid-ddos-friendly-host-flyhosting/" title="Permalink to German Police Raid DDoS-Friendly Host ‘FlyHosting’" rel="bookmark">German Police Raid DDoS-Friendly Host ‘FlyHosting’</a> </h2>  
# date : <span class="date updated">March 31, 2023</span>
# content : <div class="entry-content">  all <p> tag   I want to add only the text without any html tag 

# selector for techcrunch exemple
# title : <h2 class="post-block__title"> h2 text in this tag is the title
# url : <a class="post-block__title__link" href="/2023/04/03/quantexa-raises-129m-  HREF in this tag is the URL 
# date : <time class="river-byline__full-date-time" datetime="2023-04-03T23:05:38">7:05 PM EDT<span class="full-date-time__separator">•</span>April 3, 2023</time>
# content :<div class="post-block__content">Financial fraud and other online crime continue to present major threats to businesses, and they remain a key focus for regulators requiring more rigorous efforts to keep illicit activity at bay. N...</div>

# # selector for darkreading  exemple
# <a href="https://www.darkreading.com/attacks-breaches/doj-112m-crypto-stolen-romance-scams" class="wrap-latest-item wrap-latest-item--link"><div class="latest-item"><div class="article-detail"><span class="article-title title-pc">DoJ Recovers $112M in Crypto Stolen With Romance Scams</span><p class="article-sumary article-sumary-pc">Authorities claw back funds from six crypto accounts they say were linked to a "pig-butchering" cybercrime ring.</p></div></div><p class="article-sumary article-sumary-mobile">Authorities claw back funds from six crypto accounts they say were linked to a "pig-butchering" cybercrime ring.</p><div class="article-byline"><div class="author-image"><div class="lazyload-wrapper " style="margin: auto;"><picture><source media="(max-width: 576px)" srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blte161b23f0fd3a84b/60b1ea374e7eb868c4c6a293/dr_staff_125x125.jpg?quality=80&amp;format=webply&amp;width=48" type="image/webp"><source media="(max-width: 767px)" srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blte161b23f0fd3a84b/60b1ea374e7eb868c4c6a293/dr_staff_125x125.jpg?quality=80&amp;format=webply&amp;width=48" type="image/webp"><source media="(min-width: 768px)" srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blte161b23f0fd3a84b/60b1ea374e7eb868c4c6a293/dr_staff_125x125.jpg?quality=80&amp;format=webply&amp;width=48" type="image/webp"><source srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blte161b23f0fd3a84b/60b1ea374e7eb868c4c6a293/dr_staff_125x125.jpg?quality=80&amp;format=jpg&amp;width=48" type="image/jpeg"><img class="author-avatar" src="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blte161b23f0fd3a84b/60b1ea374e7eb868c4c6a293/dr_staff_125x125.jpg?quality=80&amp;format=jpg&amp;width=48" alt="dr_staff_125x125.jpg" height="24" width="24"></picture></div></div><p class="byline">by Dark Reading Staff, Dark Reading</p><p class="date">Apr 03, 2023</p></div><div class="d-flex footer-block"><div class="article-icon-primary"><div class="icon"><span>Attacks/Breaches</span></div></div><div class="reading-time-container"><svg width="14" height="14" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.894.754a.513.513 0 01.392-.016A6.667 6.667 0 117 .333.513.513 0 117 1.36a5.642 5.642 0 101.935.342.513.513 0 01-.04-.947z" fill="#494949"></path><path d="M6.636 3.561a.513.513 0 01.876.363v2.865l2.026 2.026a.513.513 0 01-.725.725L6.637 7.364A.512.512 0 016.487 7V3.924c0-.136.053-.267.15-.363z" fill="#494949"></path></svg><span class="text-uppercase reading-time-text icon">1 MIN READ</span></div><div class="article-icon"><div class="icon"> <div class="lazyload-wrapper " style="margin: auto;"><picture><source media="(max-width: 576px)" srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blt27dca7fd9a7ec07d/60da98a6537dbc26a0e2a2d3/Article.svg?quality=80&amp;format=webply&amp;width=26" type="image/webp"><source media="(max-width: 767px)" srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blt27dca7fd9a7ec07d/60da98a6537dbc26a0e2a2d3/Article.svg?quality=80&amp;format=webply&amp;width=26" type="image/webp"><source media="(min-width: 768px)" srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blt27dca7fd9a7ec07d/60da98a6537dbc26a0e2a2d3/Article.svg?quality=80&amp;format=webply&amp;width=26" type="image/webp"><source srcset="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blt27dca7fd9a7ec07d/60da98a6537dbc26a0e2a2d3/Article.svg?quality=80&amp;format=jpg&amp;width=26" type="image/jpeg"><img src="https://eu-images.contentstack.com/v3/assets/blt66983808af36a8ef/blt27dca7fd9a7ec07d/60da98a6537dbc26a0e2a2d3/Article.svg?quality=80&amp;format=jpg&amp;width=26" alt="Article Icon" height="13" width="13"></picture></div> <span>Article</span></div></div></div><hr></a>

#selector for security week 
# <div class="zox-art-text">
# <div class="zox-art-title">
# <a href="https://www.securityweek.com/cisco-to-acquire-cloud-security-firm-lightspin-for-reported-200-million/" rel="bookmark">
# <h2 class="zox-s-title3">Cisco to Acquire Cloud Security Firm Lightspin for Reported $200 Million</h2>
# </a>
# </div>
# <p class="zox-s-graph"> 
# Cisco is set to acquire Israel-based cloud security company Lightspin for a reported $200-250 million. </p>
# </div>

#selector for wired/category/security 
# #  title and url and found in this tag <a class="SummaryItemHedLink-ciaMYZ kRJmrk summary-item-tracking__hed-link summary-item__hed-link" data-component-title="" data-component-type="recirc-river" data-recirc-pattern="summary-item" href="/story/vulkan-files-russia-security-roundup/" target="_self" data-uri="f70689e49274eccd9c90572c666e7971"><h3 class="SummaryItemHedBase-eaxFWE fcczqx summary-item__hed" data-testid="SummaryItemHed">‘Vulkan’ Leak Offers a Peek at Russia’s Cyberwar Playbook</h3></a>
# content = text in this tag <div class="BaseWrap-sc-SJwXJ BaseText-fEohGt SummaryItemDek-dyrmLu deUlYF hQMuwO fZMRPW summary-item__dek summary-item__dek--extra-spacing">Plus: A major new supply chain attack, Biden’s 
#date NA for this site

#selector for bleeping computer 
# <div class="bc_latest_news_text">
# <div class="bc_latest_news_category">
# <span><a href="https://www.bleepingcomputer.com/news/security/" style="color: #d93240" aria-label="Show more stories related to Security">Security</a></span>
# </div>
# url and title in this tag : <h4><a href="https://www.bleepingcomputer.com/news/security/cisa-warns-of-zimbra-bug-exploited-in-attacks-against-nato-countries/">CISA warns of Zimbra bug exploited in attacks against NATO countries</a></h4>
# content is in p <p>The Cybersecurity and Infrastructure Security Agency (CISA) warned federal agencies to patch a Zimbra Collaboration (ZCS) cross-site scripting flaw exploited by Russian hackers to steal emails in attacks targeting NATO countries.</p>
# <ul><li class="bc_news_author"><a rel="author" href="https://www.bleepingcomputer.com/author/sergiu-gatlan/" class="author">Sergiu Gatlan</a></li> <li class="bc_news_date">April 03, 2023</li>
# date here  <li class="bc_news_time">04:36 PM</li>
# <li class="bc_news_comment"><a href="https://www.bleepingcomputer.com/news/security/cisa-warns-of-zimbra-bug-exploited-in-attacks-against-nato-countries/#comment_form"><img src="https://www.bleepstatic.com/images/site/comment.png" alt="Comment Count"> 0</a></li>
# </ul></div>


# Hi I want to scrap multiple website to get their recent article posted 
# I would like to use beautiful soup to do so 
# here the site i wanna scrap : 
  
# The Hacker News (THN) - https://thehackernews.com/
# Krebs on Security - https://krebsonsecurity.com/
# Ars Technica - https://arstechnica.com/
# ZDNet - https://www.zdnet.com/
# TechCrunch - https://techcrunch.com/
# CNET - https://www.cnet.com/
# Dark Reading - https://www.darkreading.com/
# Threatpost - https://threatpost.com/
# Infosecurity Magazine - https://www.infosecurity-magazine.com/
# SecurityWeek - https://www.securityweek.com/
# The Register - https://www.theregister.com/
# Wired - https://www.wired.com/category/security/
# Bleeping Computer - https://www.bleepingcomputer.com/
# CSO Online - https://www.csoonline.com/
# SC Magazine - https://www.scmagazine.com/

# so i want to have the most modular code possible with error handling and good comment to scrap their main page and get the recent article posted, i also have a utils.py file 
# and save it in my database articleBD.json  
#My json file look like this :   {
    #     "title": "Canada\u2019s National Cyber Security Strategy: Takeaways for the Private Sector",
    #     "date": "N/A",
    #     "url": "https://www.mccarthy.ca/en/insights/blogs/cyberlex/canadas-national-cyber-security-strategy-takeaways-private-sector-1",
    #     "content": "Ca"
    # },
# What information do you need to start the project?  