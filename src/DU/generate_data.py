import pandas as pd
import numpy as np
from pathlib import Path

raiz = Path(__file__).resolve().parent.parent.parent
carpeta = raiz / "Data" / "vacas"
clean = []
total_duplicados = 0
total_nulos = 0
total_archivos = len(list(carpeta.glob("*.csv")))

for archivo in carpeta.glob("*.csv"):
    # Carga de datos
    print(f"\nLeyendo: {archivo.name} ")
    data = pd.read_csv(archivo, sep=',', header=1, engine='python')

    # Conteo de datos duplicados
    duplicados = data.duplicated().sum()
    total_duplicados += duplicados

    # Revision de datos faltantes
    data = data.replace('?', np.nan)
    nulos = data.isnull().sum().sum()
    total_nulos += nulos

    nombre_archivo = archivo.stem

    # Crear columna al inicio
    data.insert(0, "id_vaca", nombre_archivo)

    clean.append(data)

print("============================= DF completo =============================")
df_salida = pd.concat(clean, ignore_index=True)
print("Total de archivos procesados: ", total_archivos)
print("Observaciones duplicadas: ", total_duplicados)
print("Valores nulos: ", total_nulos)

print("... guardando ...")
df_salida.to_csv(raiz / "Data" / "dataset_vacas.csv", index=False)
print("Guardado!")