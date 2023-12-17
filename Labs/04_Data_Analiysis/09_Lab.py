
# Content Base Recommendation System

import pandas as pd


movie_df = pd.read_csv('Data/movies.csv')
print(movie_df.head().to_string())


# rating_df = pd.read_csv('Data/ratings.csv')
# print(rating_df.head().to_string())

# title sütununda bulunan yıl bilgisini 'year' isimli yeni açılacak sütuna ekleyelim
movie_df['year'] = movie_df['title'].str.extract(r'\((\d{4})\)', expand=False)
# title sütunundaki yıl bilgisinden kurtulduk
movie_df['title'] = movie_df['title'].str.replace(r'\(\d{4}\)', '', regex=True).str.strip()
# print(movie_df.head().to_string())


# Her bir filmin veri setindeki her bir türe sahipse 1, değilse 0 basalım. one hot encoding kullanmıyoruz. Hard code yapacağız.


def genre_count(genre: str):
    return list(genre.split('|'))


print(movie_df['genres'].apply(genre_count))
