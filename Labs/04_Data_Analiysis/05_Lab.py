
import pandas as pd
import numpy as np


df = pd.read_csv('Data/nba.csv')


# En yüksek maaşı olan oyuncu kim

print(df[df['Salary'] == df['Salary'].max()][['Name']])

# Yaşı 20 ile 35 arsında olan oyuncuların adı, takımı, yaş bilgileri ekrana getirin. Yaş bilgisine göre çoktan aza sıralayarak ekrana basın

print(df[df['Age'].between(20, 35)][['Name', 'Team', 'Age']].sort_values(by='Age'))

# James Young isimli zatı muhterem hangi takım oyuncusu

print(df[df['Name'] == 'James Young'][['Team']])

# Takımlara göre oyuncuların maaş ortalaması nedir

result = df.groupby('Team')['Salary'].mean()
print(result.map("{:.2f}".format))

# Veri setinde kaç farklı takım var. Hazır fonksiyon bakın

print(df['Team'].nunique())


# İsim içerisinde "and" ifadesi geçen oyuncuları listeleyen bir fonksiyon yazın. Bu fonksiyon name sütununa uygulayın.


