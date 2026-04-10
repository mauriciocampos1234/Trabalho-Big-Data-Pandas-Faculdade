import pandas as pd

# 1. Ler o CSV (usando as configurações que já validamos)
df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# 1. Substituir nulos por '1900/01/01'
df['Date'] = df['Date'].fillna('1900/01/01')

print("\n--- Verificação: Coluna Date com 1900/01/01 ---")
print(df.loc[[22]]) # A linha 22 era a que tinha NaN

# 2. Tentar transformar em datetime (ISSO VAI GERAR ERRO)
try:
    df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d')
except Exception as e:
    print(f"\n❌ ERRO ESPERADO ENCONTRADO: {e}")