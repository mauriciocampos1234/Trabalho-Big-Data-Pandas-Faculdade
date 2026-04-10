import pandas as pd

# 1. Ler o CSV (usando as configurações que já validamos)
df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# Substituir valores nulos por 0 na coluna 'Calories'
df['Calories'] = df['Calories'].fillna(0)

print("\n--- Verificação: Coluna Calories (Linhas 18 e 28) ---")
print(df.loc[[18, 28]])