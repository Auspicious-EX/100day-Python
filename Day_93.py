# DAY 93 : Exercise 10 - News App Solution & Shoutout 

import requests
import json

query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-01-28&sortBy=publishedAt&apiKey=9112e5feeb644241b18e39ba16102b90"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]: 
    print(article["title"])
    print(article["description"])
    print("--------------------------------------")