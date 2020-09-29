import pandas as pd 
import numpy as np

file_Path = "../TextFiles/populationbycountry19802010millions.csv"

df_population = pd.read_csv(file_Path)

df_population.set_index('Country')

print(df_population)

print(df_population.keys())

print("¿Cuáles fueron los 5 paises más productores de GEI en 2010?")


print("\n¿Cuáles fueron los 5 paises más poblados en 2010?")

df_population = df_population.iloc[1:]
df_population.astype("float64", errors='ignore') #np.dtype()
#df_population.infer_objects() #infer_objects=True

df_population = df_population.sort_values("2010", ascending = False)

print(df_population["2010"][:20])
print(df_population.dtypes)
print("\n¿Tienen algunra relación?")