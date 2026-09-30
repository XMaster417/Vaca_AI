import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carga de datos
print("========== Carga de Datos ==========")
data = pd.read_csv('./data.csv')
print(data.shape)

# Eliminacion de datos duplicados
print("========= Duplicados =========")
print(data.duplicated().sum())
print("/=/=/ Limpiando datos /=/=/")
data = data.drop_duplicates()
print(data.shape)

# Exploracion basica de los datos
print("========== Info del DataSet =========")
data.info()
print("/=/=/ Columnas del DataSet /=/=/")
print(data.columns)
print("/=/=/ Head del DataSet /=/=/")
print(data.head())

# Revision de datos faltantes
print("========== Datos faltantes ==========")
print("Null data:\n", data.isnull().sum())
print("Null data: ", data.isnull().sum().sum())
print("/=/=/=/=/=/=/=/=/=/=")
print("? Data:\n", (data == '?').sum())
print("? Data total: ", (data == '?').sum().sum())
print("/=/=/ Transformando ? a valores na /=/=/")
data = data.replace('?', np.nan)
print("Null data nuevo: ", data.isnull().sum().sum())

# Conteo de datos por columna
print("========== Conteo de Datos por columna ==========")
cols = data.columns
for i in cols:
    print(data[i].value_counts())
    print("/=/=/=/=/=/=/=/=/=/=")

