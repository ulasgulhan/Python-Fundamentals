
import pandas as pd


# Group by
# Veri setimizdeki bazı değerlere göre verilerimizi gruplamaya yarar

users = {
    'employee': ['Burak', 'İlker', 'Fatma', 'Ulaş', 'Uğurcan'],
    'occupation': ['Kumarbaz', 'Kalpazan', 'Kalpazan', 'Kaçakçı', 'Kumarbaz'],
    'neighbor': ['Sarıyer', 'Zeytinburnu', 'Sarıyer', 'Gayrettepe', 'Zeytinburnu'],
    'income': [5000, 4000, 5000, 4000, 5000],
    'age': [34, 34, 33, 34, 33]
}

df = pd.DataFrame(users)

# print(df)

# Veri setimizi mesleklerine göre gruplayınız.

print(df.groupby('occupation').groups)

# Hangi semtte kim oturuyor
for name, group in df.groupby('neighbor'):
    print(name)
    print(group)


# Hangi semtte kaç çalışanım var
result = df.groupby('neighbor')['employee'].count()
df_groupby_neighbor = pd.DataFrame(result)
print(df_groupby_neighbor)


# Mesleklere göre toplam maaşları listeleyin
result = df.groupby('occupation')['income'].sum()
print(result)

# Mesleklere göre yaş ortalaması
result = df.groupby('occupation')['age'].mean()
print(result)




