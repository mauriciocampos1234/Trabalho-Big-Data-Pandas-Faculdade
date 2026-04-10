# 1. Importar a biblioteca pandas
import pandas as pd

# 2. Criar uma variável e ler o conteúdo do arquivo CSV
# Parâmetros solicitados: 
# sep=';' (o arquivo usa ponto e vírgula)
# engine='python' (garante compatibilidade com alguns formatos de CSV)
# encoding='ISO-8859-1' ou 'utf-8' (opcional, vamos usar utf-8 por padrão)

df = pd.read_csv('data.csv', sep=';', engine='python', encoding='utf-8')

# 1. Criar uma nova variável para o subconjunto
# Selecionando 3 colunas: 'Pulse', 'Maxpulse' e 'Calories'
df_reduzido = df[['Pulse', 'Maxpulse', 'Calories']]

# 2. Exibir o novo subconjunto
print("\n--- Subconjunto de Dados (3 Colunas) ---")
print(df_reduzido)