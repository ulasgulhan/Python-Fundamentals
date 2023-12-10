
import pandas as pd
import numpy as np


numbers = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd']
scaler = 5
dictionary = {
    'a': 10,
    'b': 20,
    'c': 30,
}

np_array = np.array([20, 30, 40, 40])

# numbers isimli python list objesini pandas Series dönüştürelim.
# pd_series = pd.Series(numbers)
# print(pd_series)
#
# pd_series = pd.Series(letters)
# print(pd_series)

# pd_series = pd.Series(dictionary)
# print(pd_series)
#
# # python temellerinde öğrendiğimiz dilimleme işlemini pandas serilerine de uygulayabiliriz.
# print(pd_series[:2])
#
# # pandas serilerinin sahip olduğu bazı built-in fonksiyonlar ve attributeler
# print(pd_series.shape)
#
# # serinin veri tipini döner
# print(pd_series.dtype)
#
# # serinin kaç katmanlı olduğunu döner
# print(pd_series.ndim)
#
# # serinin hızlıca count, mean, std vb özet bilgilerini verir.
# print(pd_series.describe())
#
# # serinin ilk index'ten başlayarak görmek istediğimiz aralıkta ki index'leri bize döner
# print(pd_series.head(1))
#
# # head() fonsksiyonunun sondan başlayarak çalışan versiyonu
# print(pd_series.tail(1))
#
# # şartın tutup tutmama durumuna göre true false döner
# print(pd_series > 20)
# print(pd_series % 2 == 0)
#
# print(f'Bütün değerlerin toplamı: {pd_series.sum()}')


opel_2000 = pd.Series([20, 30, 40], ['astra', 'corsa', 'vetra'])
opel_2001 = pd.Series([50, 60, 70], ['astra', 'corsa', 'vetra'])

total = opel_2000 + opel_2001
print(total)


# DataFrame
# pandas'da yoğun olarak kullanılan bir başka yapıdır. Excel gibi düşünebilirsiniz. Yani satır ve sütunlardan oluşan bir yapısı söz konusudur.

df = pd.DataFrame(
    data=np.random.rand(3, 5),
    index=['A', 'B', 'C'],
    columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
)

print(df)

# DataFrame üzerinden veri seçme (select)
print(df['Column2'])
print(type(df['Column2']))
print(df['Column1'])
print(type(df[['Column1']]))
print(type(df))


# loc[] index değerini vererek istediğimiz index değerinde tutulan kayıda erişebiliriz.
print(df.loc['B'])
print(type(df.loc['B']))

# loc['index', 'column']
print(df.loc['C', 'Column3'])

# ilgili sütunların tüm index'lerini retrun eder
print(df.loc[:, ['Column1', 'Column3']])

print(df.loc[['A', 'C'], ['Column2']])
