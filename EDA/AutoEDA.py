import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns

raiz = Path(__file__).resolve().parent.parent
carpeta = raiz / "Data" / "vacas"

clean = []

for archivo in carpeta.glob("*.csv"):

    # Carga de datos
    print(f"\n======= Leyendo: {archivo.name} =======")
    data = pd.read_csv(archivo, sep=',', header=1, engine='python')
    print(data.shape)

    # Eliminación de datos duplicados
    print("=!=!= Duplicados =!=!=")
    print(data.duplicated().sum())
    print("/=/=/ Limpiando datos /=/=/")
    data = data.drop_duplicates()
    print(data.shape)

    # Revision de datos faltantes
    print("=!=!= Datos faltantes =!=!=")
    print("Null data: ", data.isnull().sum().sum())
    print("/=/=/=/=/=/=/=/=/=/=")
    print("? Data total: ", (data == '?').sum().sum())
    print("/=/=/ Transformando ? a valores na /=/=/")
    data = data.replace('?', np.nan)
    print("Null data nuevo: ", data.isnull().sum().sum())
    print("... Transformando Null a 0 ...")

    data = data.fillna(0)
    data = data.drop(columns=["RCS (* 1000 células / ml)"])

    nombre_archivo = archivo.stem

    # Crear columna al inicio
    data.insert(0, "id_vaca", nombre_archivo)

    clean.append(data)

print("=!=!=!=!=! DF completo =!=!=!=!=")
df_salida = pd.concat(clean, ignore_index=True)
print(df_salida.shape)
print(df_salida.isnull().sum)
print(df_salida.dtypes)
print(df_salida.head())

salida = int(input(("Buscas guardar el data set nuevo? 1: Si 2: No\n")))

if salida == 1:
    print("... guardando ...")
    df_salida.to_csv(raiz / "Data" / "dataset_vacas.csv", index=False)
    print("Guardado!")