#in day 90 we are going to slove another excersize called make a news app.. using news API and requests  module in python.....
import requests
import json #json module is used to parsing the string......
query=input("what type of news are you inrestred in : ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2024-03-28&sortBy=publishedAt&apiKey=8e394f364ede4432921782f1bff20528"

r=requests.get(url)
news = json.loads(r.text)
# print(news , type(news))
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("...............................................")
