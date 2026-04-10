import pandas as pd
import numpy as np

# 1. Ler o CSV (usando as configurações que já validamos)
df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# 11. Remover registros onde a coluna 'Date' possui valores nulos
# O subset garante que ele olhe apenas para a coluna Date para decidir a exclusão
df_limpo = df.copy()
df_limpo.dropna(subset=['Date'], inplace=True)

# 12. Imprimir o resultado final para validação
print("\n--- DataFrame Final após Limpeza ---")
print(df_limpo.to_string())

# Verificação final de informações
print("\n--- Resumo Final ---")
df_limpo.info()