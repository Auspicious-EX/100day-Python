# DAY 90 : Exercise 10: News App in Python

""" 
Use the NewsAPI and the requests module to fetch the daily news related to different topics. Go to: https://newsapi.org/ and explore the various options to build you application
 """
""" 
Your API key is: 
 """
import requests

def fetch_news(api_key, topic):
    url = f"https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "category": topic,
        "country": "us"  # You can change the country if needed
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] == "ok":
        articles = data["articles"]
        for idx, article in enumerate(articles, 1):
            print(f"{idx}. {article['title']} - {article['url']}")
    else:
        print("Failed to fetch news:", data["message"])

if __name__ == "__main__":
    api_key = "your_api_key"  # Replace "your_api_key" with your actual API key
    topic = input("Enter the topic of news you want (e.g., sports, science, government): ")
    fetch_news(api_key, topic)

