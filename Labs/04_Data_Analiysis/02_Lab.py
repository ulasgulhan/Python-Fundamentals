
import pandas as pd
from os import path

print(path.abspath('imdb.csv'))

# CSV formatındaki datamı okuyorum
df = pd.read_csv('Data/imdb.csv', encoding='utf-8')
print(df.head().to_string())

# Movie_Title sütununun ilk 20 satırını df olarak ekrana basın
# Yol 1
print(df.head(20)[['Movie_Title']])
# Yol 2
print(df[['Movie_Title']][0:20])
# Yol 3
print(df.loc[:19, ['Movie_Title']])

# Movie_Title ve Rating sütunlarının 20 ile 50.ci index aralığındaki bilgileri getirelim.
# Yol 1
print(df.loc[20:50, ['Movie_Title', 'Rating']])
# Yol 2
print(df[['Movie_Title', 'Rating']][20:51])

# Rating sütun 7.0'dan büyük olan fimleri Title, Rating, YR_Released bilgilerini listeleyin

print(df[df['Rating'] >= 7.0][['Movie_Title', 'Rating', 'YR_Released']])

# YR_Released bilgisi 2014 ile 2018 arasında olan filmlerin Title, Rating, YR_Released bilgilerini listeleyin

# Yol 1
print(df[df['YR_Released'].between(2014, 2018)][['Movie_Title', 'Rating', 'YR_Released']])

# Yol 2
print(df[(df['YR_Released'] >= 2014) & (df['YR_Released'] <= 2018)][['Movie_Title', 'Rating', 'YR_Released']])


# Num_Reviews 100'den büyük ya da Rating 8 ile 9 arasında olan filmlerin Title, Rating, YR_Released bilgilerini listeleyin

# Yol 1
print(df[(df['Rating'].between(8, 9)) | (df['Num_Reviews'] >= 100000)][['Movie_Title', 'Rating', 'YR_Released']])

# Yol 2
print(df[(df['Num_Reviews'] >= 100000) | (df['Rating'] >= 8) & (df['Rating'] <= 9)][['Movie_Title', 'Rating', 'YR_Released']])
