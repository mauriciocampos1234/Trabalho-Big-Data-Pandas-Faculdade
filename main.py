# 1. Importar a biblioteca pandas
import pandas as pd

# 2. Criar uma variável e ler o conteúdo do arquivo CSV
# Parâmetros solicitados: 
# sep=';' (o arquivo usa ponto e vírgula)
# engine='python' (garante compatibilidade com alguns formatos de CSV)
# encoding='ISO-8859-1' ou 'utf-8' (opcional, vamos usar utf-8 por padrão)

df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# 1. Definir o valor máximo de linhas para exibição como 9999
pd.options.display.max_rows = 9999

# 2. Imprimir o conjunto original usando o método to_string()
# O to_string() transforma o DataFrame em uma string completa, sem resumos.
print("\n--- Visualização Completa (Microatividade 3) ---")
print(df.to_string())