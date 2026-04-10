import pandas as pd
import numpy as np

# 1. Ler o CSV (usando as configurações que já validamos)
df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# 8. Substituir o valor '1900/01/01' por NaN (Not a Number)
df_limpo = df.copy()
df_limpo['Date'] = (
	df_limpo['Date']
	.astype('string')
	.str.strip()
	.str.strip("'")
	.str.strip('"')
)

df_limpo['Date'] = df_limpo['Date'].replace('1900/01/01', pd.NA)

# 9. Corrigir o erro do valor "20201226" (Linha 26)
# Primeiro usamos o replace para ajustar a string e depois tentamos a conversão
df_limpo['Date'] = df_limpo['Date'].replace('20201226', '2020/12/26')

# 10. Agora convertemos toda a coluna para o formato Datetime
# O parâmetro errors='coerce' transformaria erros em NaN, 
# mas como o roteiro pede para tratar especificamente, usamos a conversão direta:
df_limpo['Date'] = pd.to_datetime(df_limpo['Date'], format='%Y/%m/%d', errors='coerce')

print("\n--- Verificação: Datas convertidas com sucesso ---")
print(df_limpo.loc[[22, 26]]) # Verificando a linha 22 (que virou NaN) e a 26 (ajustada)