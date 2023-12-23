
import pandas as pd
import numpy as np
from math import sqrt


movie_df = pd.read_csv('Data/movies.csv')
rating_df = pd.read_csv('Data/ratings.csv')


movie_df['year'] = movie_df['title'].str.extract(r'\((\d{4})\)', expand=False)
movie_df['title'] = movie_df['title'].str.replace(r'\(\d{4}\)', '', regex=True).str.strip()

movie_df.drop(
    labels=['genres', 'year'],
    axis=1,
    inplace=True
)

rating_df.drop('timestamp', axis=1, inplace=True)

user_input_df = pd.DataFrame([
    {'title': 'Toy Story', 'rating': 5},
    {'title': 'Jumanji', 'rating': 5},
    {'title': 'Space Jam', 'rating': 5},
    {'title': 'Robots', 'rating': 4},
    {'title': 'Back to the Future', 'rating': 4},
])

input_movies = movie_df.merge(
    right=user_input_df,
    how='right',
    left_on='title',
    right_on='title'
)

# Yeni gelen kullanıcı ile hali hazırda aynı filmleri rate etmiş kullanıcıları saptayalım

user_subset_df = pd.merge(
    left=rating_df,
    right=input_movies,
    left_on='movieId',
    right_on='movieId',
    how='inner'
)

user_subset_df.drop(
    labels=['title', 'rating_y'],
    axis=1,
    inplace=True
)

user_subset_df.rename(
    columns={
        'rating_x': 'rating'
    },
    inplace=True
)

# Artık 'user_subset_df' içerisinde benle aynı filmleri rate etmiş kullanıcılar var.
# userId'lerine göre ilgili veri setini gruplayalım.

user_subset_groups = user_subset_df.groupby(['userId'])

# for name, group in user_subset_groups:
#     print(f'Group Name: {name}\nGroup: {group}')

# Yukarıda elde ettiğimiz veri kümesini sort edelim ki hali hazırda benimle aynı filmleri rate etmiş kullanıcıları daha verimli bir şekilde görelim.

sorted_user_usesubset_group = sorted(
    user_subset_groups,
    key=lambda x: len(x[1]),
    reverse=True
)

# Çalışmanın bu sayfasında yeni gelen kullanıcı ile bu kullanıcının rate ettiği filmleri hali hazırda rate etmiş kullanıcılar arasındaki korelasyonu bulacağız. Burada korelasyon ile kullanıcılar arasındaki ilişkiyi inceleyeceğiz. Korelasyon istatistik biliminde yoğun olarak kullanılmaktadır ve farklı korelasyon türleri vardır. Biz burada Pearson Korelasyonunu kullanacağız.

# Korelasyon sonucunu store etmek için bir dictionary yaratalım

pearson_corellation_dict = {}

for userId, group in sorted_user_usesubset_group:
    # group girdisi ile 'input_movies' her iki tarafta bulunan movieId sütununa göre sıralıyoruz. Böylelikle değerler daha sonra birbirlerine karışmayacak nizami bir sıralama elde etmiş olacağım.
    group.sort_values(by='movieId', inplace=True)
    input_movies.sort_values(by='movieId', inplace=True)

    # Pearson korelasyonnu hesaplamak için kullanılan formlü burada teşekkül etmemiz gerekecek. Bu yüzden formülde bulunan N katsayısını tanımlıyoruz
    n_rating = len(group)

    # Merge işlemi yaparken söylediğim gibi merge işlemini isin() fonksiyonu ile yapabiliriz.
    # grouplar içerisindeki movieId ile input_movies'deki movieId'lerden iki veri setini birleştiriyoruz. Ayık olun yukarıda bu iki setini sort ederek hizalamıştık.
    temp_df = input_movies[input_movies['movieId'].isin(group['movieId'].tolist())]

    # yukarıdaki satırda yapılan işlem sonucunda bize gereksiz bir çok sütun oluşturur. Bize sadece rating bilgisi gerekli olduğu için onları select edelim.
    temp_rating_list = temp_df['rating'].tolist()
    temp_group_list = group['rating'].tolist()

    # Bu ana kadar korelasyon formülünü uygulamak için ihtiyaç duyulan argümanların hazırlığını yaptık. Şimdi X ve Y olarak nitelendireceğimiz iki attribute arasındaki benzerliği bulacağız.

    Sxx = sum([i ** 2 for i in temp_rating_list]) - pow(sum(temp_rating_list), 2) / float(n_rating)
    Syy = sum([i ** 2 for i in temp_group_list]) - pow(sum(temp_group_list), 2) / float(n_rating)

    Sxy = sum(i * j for i, j in zip(temp_rating_list, temp_group_list)) - sum(temp_rating_list) * sum(temp_group_list) / float(n_rating)

    if Sxx != 0 and Syy != 0:
        pearson_corellation_dict[userId] = Sxy / sqrt(Sxx * Syy)
    else:
        pearson_corellation_dict[userId] = 0

print(pearson_corellation_dict.items())
