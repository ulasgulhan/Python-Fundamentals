
from pprint import pprint
from requests import get

response = get('https://newsapi.org/v2/everything?q=tesla&from=2023-10-04&sortBy=publishedAt&apiKey=c245051cb8b74acfbb4923697b2adb24')

data = response.json()

# print(f"Author: {data['articles'][0]['author']}")
# print(f"Title: {data['articles'][0]['title']}")
# print(f"Published Date: {data['articles'][0]['publishedAt']}")

# Kullanıcıdan yazar ismi alınacak, alınan bu yazar veri içerisinde search edilecek ve ilgili makalenin tüm bilgileri ekrana yazılacak.

author = input('Yazar adı giriniz: ')

for article in data.get('articles'):
    if article.get('author') == author:
        pprint(article)
