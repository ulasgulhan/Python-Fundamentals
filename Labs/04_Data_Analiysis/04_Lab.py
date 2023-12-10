
import pandas as pd


# merge & join
# İki ayrı veri setinde ortak olarak bulunan sütunlar kullanılarak bu iki veri setinin birleştirilesi işlemine merge ya da join denir. Join işleminin birebir aynısı SQL veri tabanında bulunmaktadır.

customer = {
    'Customer Id': [1, 2, 3],
    'First Name': ['Burak', 'Hakan', 'İpek'],
    'User Name': ['beast', 'bear', 'keko']
}

orders = {
    'Order Id': [1001, 1002, 1003, 1004, 1005],
    'Customer Id': [1, 2, 3, 4, 5],
    'Order Date': ['2023-07-01', '2023-06-06', '2023-06-10', '2023-07-01', '2023-07-01']
}

df_customer = pd.DataFrame(customer)
df_orders = pd.DataFrame(orders)

print(pd.merge(left=df_customer, right=df_orders, on='Customer Id', how='inner'))
print(pd.merge(left=df_customer, right=df_orders, on='Customer Id', how='right'))
print(pd.merge(left=df_customer, right=df_orders, on='Customer Id', how='left'))
