import pandas as pd 
import numpy as np

def segmentateDF(df : pd.DataFrame, category : str):
    segmented_dfs = []
    categories = df[category].unique()
    series = pd.Series(categories)
    for c in categories:
        # df_emissions = df_emissions.filter(items=[ "year", 'value'])
        segmented_dfs.append( df[df[category] == c])
    return segmented_dfs

def totalSubmissions():
    pass

def mergeDts(dt1, dt2, commonField: str):
    df_merge_col = pd.merge(dt1, dt2, on = commonField)
    return df_merge_col

def beforeTotal (dts : list, commonField : str):
    res = dts[0]
    for i in range (1, len(dts)):
        res = mergeDts(res, dts[i], commonField)
    return res

pd.set_option('display.max_rows', None)

# File Paths
file_Path_population = "../TextFiles/populationbycountry19802010millions.csv"
file_path_GHE = "../TextFiles/greenhouse_gas_inventory_data_data.csv"

# Creates dataframes
df_population = pd.read_csv(file_Path_population, index_col = 0) # Sets country to be the key

df_emissions = pd.read_csv(file_path_GHE, index_col = 0) # Sets country to be the key

# Clears population dataset
df_population = df_population.replace(to_replace= ["--", "NA"], value= "0" )
# There is no need to clear the second one

# Passes data from Text to float
df_population = df_population.astype({"2009": float, "2010": float})
df_emissions = df_emissions.astype({"year": int, "value": float})


print("------------")
print("¿Cuáles fueron los 5 paises más productores de GEI en 2010?")

# We filter only the data from 2010
df_emissions_2010 = df_emissions[df_emissions["year"] == 2010]
print(df_emissions_2010)

df_emissions_2010_segmented = segmentateDF(df_emissions_2010, "category")
total = beforeTotal(df_emissions_2010_segmented, "country_or_area")


print(total, "")

print("")
print("¿Cuáles fueron los 5 paises más poblados en 2010?")

# Regex means -> regular expression 
df_population = df_population.sort_values("2010", ascending = False ) #

print(df_population["2010"][:6])

print("")
print("¿Tienen alguna relación?")


print("Sí, son los paises del primer mundo que colonizaron al resto. ")
print("")
print("----")
