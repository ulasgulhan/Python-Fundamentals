
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
