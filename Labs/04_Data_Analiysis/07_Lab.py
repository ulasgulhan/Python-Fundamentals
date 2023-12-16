
import pandas as pd
import numpy as np


df = pd.read_csv('Data/auto.csv')

df.columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration", "num-of-doors", "body-style",
              "drive-wheels", "engine-location", "wheel-base", "length", "width", "height", "curb-weight",
              "engine-type", "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke", "compression-ratio",
              "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

# print(df.head(5).to_string())


# Hatalı ya da eksik değerleri saptama
# Veri steimizde bazı hücrelerde "?" sembolu bulunmaktadır. Şayet veri setimizde bu tarz anormallik bulunması durumunda veri setini her hangi bir ML algoritması kullanamayız. Çünkü tüm ML algoritmalarının arkasında yoğun bir matematik vardır. Bu bağlamda "?" sembolünü matematiksel işlem olarak saklayamayacağından bu anormalliği hangle etmek gerekir.

df.replace(to_replace='?', value=np.nan, inplace=True)
# print(df.head().to_string())


# Bu adımda 'NaN' gördüğümüz yere True görmediğimiz yere False değeri basacağız. Böylelikle hangi sütunda ne kadar eksik bilgim var tespit edeceğim. Bu tespit işleminden sonra gerekli şekilde eksik bilgileri handle edeceğiz.

missing_values_df = df.isnull()
# print(missing_values_df.head().to_string())


# Ne kadar eksik verim var sayalım
for item in missing_values_df.columns.values.tolist():
    print(f'Column Name: {item}\n{missing_values_df[item].value_counts()}')


# Yukarıda missing valueların hangi sütunda ne kadar olduğunu belirledik. Artık bu eksik bilgileri handle edebiliriz.
# Handling missin values

# Yol 1 -> İlgili sütunlarda bulunan değerlerin ortalamasını alıp elde ettiğimiz bu ortalamayı eksik değerlerin olduğu hücrelere yazabiliriz.
# Yol 2 -> Yine ilgili sütunda bulunan değerlerin frekans aralığını bulup eksik değerlerin bulunduğu alanlara bu frenaks aralığındaki değerleri yazabiliriz. Frekans aralığından kastımız bir sütunda bulunan bir değerin bulunma sıklığıdır

# Ortalama değer ile eksik verilerin değiştirilmesi

df['normalized-losses'].replace(np.nan,
                                df['normalized-losses'].astype(float).mean(),
                                inplace=True)

print(df.head().to_string())

# frekans aralığı ile eksik verilerin değiştirilmesi

df['num-of-doors'].replace(np.nan,
                           df['num-of-doors'].value_counts().idxmax(),
                           inplace=True)

print(df.head().to_string())


# Veri standartizasyonu
# ML algoritmalarında kullanılacak veri steindeki verilerin belirli bir standartta olması ML algoritmalarının train edilmesi sonucunda elde edilen çıktıların doğruluk payına etki eder. Örneğin 2 ayrı merkezden gelen verilerde hastaların kilo bilgileri olsun. Bir veri setinde KG kullanılırken bir veri setinde Libre kullanılması bir anormalliğe neden olacağından kilo verisinin bir standarda kavuşturulması gerekir.

df['city_l/km'] = 235 / df['city-mpg']
df['highway_l/km'] = 235 / df['highway-mpg']


# Veri Normalizasyonu
df['length'] = df['length'] / df['length'].max()
df['width'] = df['width'] / df['width'].max()
df['height'] = df['height'] / df['height'].max()

print(df[['length', 'width', 'height']])


# Dummy Varibale
# Veri setimizde sözel (categorical) yani string diyebileceğimiz veri tipleri de değer alabilir. Hak vereceksiniz ki bu değerleri aritmatik işlere sokmalıyız ve tüm ML algoritmalarında matematiksel işlemler içerir. Bu bağlamda sözel verili scaler verilere büyüklüklere dönüştürmemiz gerekmektedir. Bu sözel verilere de dummy variable diyoruz

dummy_varibale = pd.get_dummies(df['fuel-type'], dtype='float')
print(dummy_varibale.head(20))


# Bakımı biten veri setini yeni bir excele yazalım

df.to_csv('Data/clean_auto.csv')
