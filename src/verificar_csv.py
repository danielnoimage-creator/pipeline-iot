import pandas as pd

arquivo = "data/IOT-temp.csv"

df = pd.read_csv(arquivo)

print("Colunas encontradas:")
print(df.columns.tolist())

print("\nPrimeiras 5 linhas:")
print(df.head())

print("\nQuantidade de linhas e colunas:")
print(df.shape)