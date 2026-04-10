import pandas as pd

# 1. Ler o CSV (usando as configurações que já validamos)
df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# 2. Verificar a importação
print("--- Info Original ---")
df.info()
print("\n--- Primeiras Linhas ---")
print(df.head())

# 3. Criar uma variável com a CÓPIA dos dados
df_limpo = df.copy()