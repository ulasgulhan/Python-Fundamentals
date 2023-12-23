
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import openpyxl


df_can = pd.read_excel(
    io='Data/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2,
    engine='openpyxl')

print(df_can.to_string())


# AREA, REG, Type, Coverage, DevName sütunlarını silin

df_can.drop(columns=['AREA', 'REG', 'Type', 'Coverage', 'DevName'], axis=1, inplace=True)
print(df_can.to_string())


# OdName => Country
# AreaName => Continent
# RegName => Region
# Sütunlarının isimlerini yukardaki gibi revize edin

df_can.rename(columns={'OdName': 'Country', 'AreaName': 'Continent', 'RegName': 'Region'}, inplace=True)
print(df_can.to_string())


# Sütun başlıklarının tiplerini ekrana yazdıralım

for column in df_can.columns:
    print(type(column))


# Yukarıdaki incelememiz sonucunda intiger tipinde olan sütunların tiplerini stringe map edelim

df_can.columns = list(map(str, df_can.columns))

for column in df_can.columns:
    print(type(column))


# Veri setindeki Country sütununu index olarak ayarlayalım

df_can.set_index(keys='Country', inplace=True)


# Yıl yıl göçmen sayılarını toplayarak 'Total' isimli bir sütuna yazın

df_can['Total'] = df_can.sum(axis=1, numeric_only=True)
print(df_can.head().to_string())


# Veri setindeki yılları baz alarak yani 1980-2013 yıllarını tutan bir bağımsız liste oluşturalım. Listenin itemlarının tipi string olsun

years = list(map(str, range(1980, 2014)))
print(years)


# En çok göç vermiş 5 ülkeyi bulun ve bu 5 ülkeyi df_top_five_country objesine assigned edin

df_can.sort_values(by='Total', ascending=False, axis=0, inplace=True)
df_top_five_country = df_can.head()
print(df_top_five_country.to_string())


# Yukarıda oluşturduğumu 'df_top_five_country' ve 'years' listesini kullanarak 'df_top_five_country' veri setini transpose edelim. Yani 'df_top_five_country''nin hali hazırdaki indexi olan countryler sütun years listesindeki yıllar ise index olacak.

df_top_five_country = df_top_five_country[years].transpose()
print(df_top_five_country.to_string())


# Yukarıda ana veri setimizi manipüle ederek df_top_five_country df'i oluşturduk. Bu oluşturulan veri setini 'area plot' olarak görselleştiriniz.

# df_top_five_country.plot(kind='area',
#                          stacked=False,
#                          figsize=(10, 8),
#                          alpha=0.25,)
# plt.title(label='Immigtant Trand of Top 5 Country', c='r')
# plt.ylabel(ylabel='Numbers of Immigrant', c='r')
# plt.xlabel(xlabel='Years', c='r')
# plt.show()


# 2013 yılındaki göçmen hareketliliğini histogram grafiğinde gösterelim. numpy modülünün histogram() fonksiyonunu kullanarak oluşturacağımız giafiğin frekans aralığnı bulalım

# count, bin_edges = np.histogram(df_can['2013'])
# print(count)
# print(bin_edges)
# df_can['2013'].plot(kind='hist',
#                     stacked=False,
#                     figsize=(7, 5),
#                     color='b',
#                     xticks=bin_edges)
# plt.title(label='Histogram of Immigrant from 195 Countries in 2013')
# plt.ylabel(ylabel='Numbers of Country')
# plt.xlabel(xlabel='Numbers of Immigrant')
# plt.grid(True)
# plt.show()


# Baltık ülkelerinin verdiği göçmenlerin histogram grafiği ile görselleştirelim.

# df_baltic_country = df_can.loc[['Denmark', 'Norway', 'Sweden'], years].transpose()
#
# count, bin_edges = np.histogram(df_baltic_country)
#
# df_baltic_country.plot(kind='hist',
#                        stacked=False,
#                        figsize=(7, 5),
#                        xticks=bin_edges,
#                        color=['coral', 'darkblue', 'green']
#                        )
# plt.title(label='Histogram of Immigrant from Baltic Countries')
# plt.ylabel(ylabel='Years')
# plt.xlabel(xlabel='Numbers of Immigrant')
# plt.grid(True)
# plt.show()


# 1980 - 2013 yılları arasında Iceland göçmenlerini çubuk grafikte gösterelim

df_iceland = df_can.loc['Iceland', years]


df_iceland.plot(kind='bar',
                figsize=(7, 5),
                )
plt.title(label='Iceland Immigrant of Canada 1980 to 2013')
plt.ylabel(ylabel='Numbers of Immigrant')
plt.xlabel(xlabel='Years')
plt.grid(True)
plt.show()

# Kıtalara göre göçmen dağılımını pasta grafikte gösterelim




