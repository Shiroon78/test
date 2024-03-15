import requests
import json
def fetch_news_articles(topic, api_key):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': topic,
        'apiKey': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()['articles']
    else:
        print(f'Error: {response.status_code}')
        return []

api_key = '39f959759796465da8720c705a01a180'
topic = 'Apple'
articles = fetch_news_articles(topic, api_key)

# Print the fetched news articles
for article in articles:
    print(f'Title: {article["title"]}\nURL: {article["url"]}\nDescription: {article["description"]}\n')


