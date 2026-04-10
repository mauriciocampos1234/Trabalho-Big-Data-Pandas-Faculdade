# 1. Importar a biblioteca pandas
import pandas as pd

# 2. Criar uma variável e ler o conteúdo do arquivo CSV
# Parâmetros solicitados: 
# sep=';' (o arquivo usa ponto e vírgula)
# engine='python' (garante compatibilidade com alguns formatos de CSV)
# encoding='ISO-8859-1' ou 'utf-8' (opcional, vamos usar utf-8 por padrão)

df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# 1. Imprimir as primeiras 10 linhas
print("\n--- Primeiras 10 linhas ---")
print(df.head(10))

# 2. Imprimir as últimas 10 linhas
print("\n--- Últimas 10 linhas ---")
print(df.tail(10))