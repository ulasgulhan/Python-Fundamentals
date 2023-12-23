# Content Base Recommendation System

import pandas as pd
import numpy as np


movie_df = pd.read_csv('Data/movies.csv')


# rating_df = pd.read_csv('Data/ratings.csv')
# print(rating_df.head().to_string())

# title sütununda bulunan yıl bilgisini 'year' isimli yeni açılacak sütuna ekleyelim
movie_df['year'] = movie_df['title'].str.extract(r'\((\d{4})\)', expand=False)
# title sütunundaki yıl bilgisinden kurtulduk
movie_df['title'] = movie_df['title'].str.replace(r'\(\d{4}\)', '', regex=True).str.strip()
# print(movie_df.head().to_string())


# Her bir filmin veri setindeki her bir türe sahipse 1, değilse 0 basalım. one hot encoding kullanmıyoruz. Hard code yapacağız.

# region Ben Yaptım

# def genre_split(genre: str):
#     return list(genre.split('|'))
#
#
# def all_genres():
#     genre_list = []
#     for genres in movie_df['genres'].apply(genre_split):
#         for genre in genres:
#             if genre not in genre_list and genre != '(no genres listed)':
#                 genre_list.append(genre)
#             else:
#                 pass
#     return genre_list
#
#
# def genre_column_create(df):
#     for genre in all_genres():
#         if genre in all_genres():
#             df[genre] = df['genres'].apply(lambda x: 1 if genre in x else 0)
#
#
# genre_column_create(movie_df)
# print(movie_df.head().to_string())

# endregion


# region Hocam Yaptı

genre_list = []

for index, column in movie_df.iterrows():
    for genre in column['genres'].split('|'):
        if genre not in genre_list and genre != '(no genres listed)':
            genre_list.append(genre)


movies_genre_df = movie_df.copy()
for genre in genre_list:
    movies_genre_df[genre] = np.NAN


for index, column in movies_genre_df.iterrows():
    for genre in column['genres'].split('|'):
        if genre in genre_list:
            movies_genre_df.loc[index, genre] = 1


movies_genre_df.fillna(0, inplace=True)

# endregion


# Yeni üyenin datası

user_input_df = pd.DataFrame([
    {'title': 'Toy Story', 'rating': 5},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Space Jam', 'rating': 5},
    {'title': 'Heat', 'rating': 4},
    {'title': 'Back to the Future', 'rating': 4},
])


# Kullanıcı verisi bize sadece title ve rating bilgisi ile geldi. Peki bu gelen veride ki filmler veri setimizde hangi filmlere denk geliyor bunu saptayalım

merged_input = movie_df.merge(user_input_df, how='inner', on='title')

# Heat filmi ana film setinde farklı yıllardaki versiyonları da veri setimize dahil oldu. Bu filmleri yıllarına bakarak uçuralım.

merged_input.drop(index=[3, 4], axis=0, inplace=True)

# Genres ve Year sütunlarından kurtulalım

merged_input.drop(labels=['genres', 'year'], axis=1, inplace=True)

# Yukarıda yapılan çalışmalar sonucu ilgili veri setinin index yapısı bozuldu. Örneğin 1,2,3,5,6 şeklinde devam ediyor bunları sıfırlayalım.

input_movies_df = merged_input.reset_index(drop=True)

# Yeni gelen kullanıcının rate ettiği filmlerin sahip olduğu türleri saptayalım

user_movies_df = movies_genre_df.merge(input_movies_df, how='inner', on='movieId')

# Merge işlemi sonucunda birçok sütun yaratıldı. Gereksiz sütunlardan kurtulalım

user_genre_df = user_movies_df.drop(labels=['movieId', 'title_x', 'genres', 'year', 'title_y', 'rating'], axis=1)

# Yukarıda yaptığımız işlemler sonucunda yeni gelen kullanıcının rate ettiği filmlerin sahip olduğu türleri saptadık. Bu adımda ise yeni gelen kullanıcı rating puanı ile bu türleri çarparak 'user_profile' elde edeceğiz

user_profile = user_genre_df.transpose().dot(input_movies_df['rating'])

# Content Base sistemini uygulamak için ihtiyaç duyulan bir başka matrix olan movie matrix oluşturalım. Bizim elimizde zaten filmlerin sahip olduğu türler movies_genre_df veri seti var. Bu veri setini manipüle ederek istediğimiz yani ihtiyacımız olan veri setine dönüştüreceğiz.

# 1.Adım: movieId sütununu ilgili veri setine index olarak set ediyoruz.

movie_matrix = movies_genre_df.set_index(movies_genre_df['movieId'])

# 2.Adım: İhtiyacımız olmayan sütunları silelim.

movie_matrix.drop(
    labels=['movieId', 'title', 'genres', 'year'],
    axis=1,
    inplace=True)

# user profile ve movie matrix veri setleri hazırladık. Artık weighred movie matrix bulabiliriz.

weighted_movie_matrix = (user_profile * movie_matrix).sum(axis=1)

# Recomandation matrix oluşturuyoruz

recomandation_movie_matrix = weighted_movie_matrix / user_profile.sum()
recomandation_movie_matrix.sort_values(ascending=False, inplace=True)

# recomandation_movie_matrix içerisinde sadece movieId ve öneri ağırlığı var. Bu matrixi DF dönüştürelim ki rahat rahat manipüle ederek ihtiyaç duyulan alanları getirelim. Örneğin; title, genres vs.

recomandation_df = pd.DataFrame(recomandation_movie_matrix)

# df dönüştürdük lakin bakıma muhtaç durumda. Örneğin sütun ismi '0' vs.

recomandation_df.columns = ['Weight of Recomandation']

# recomandation veri setinde yan bilgiler getirmek için movie_df ile merge edelim

result = movie_df.merge(
    recomandation_df,
    how='right',
    left_on='movieId',
    right_on='movieId'
)

print(result.head(10).to_string())
