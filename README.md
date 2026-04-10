# Trabalho Big Data com Pandas (Faculdade)

Este repositório documenta um trabalho prático/microatividades utilizando **Python + Pandas** para exploração e limpeza de um conjunto de dados.

## Linha do tempo do que foi feito (baseado nos commits)

Abaixo está o passo a passo reconstruído a partir das mensagens de commit (todos em **2026-04-10**).

### Commit inicial

- **first commit**
  - Início do repositório e estrutura base do projeto.

### Microatividade 02 — Criar um subconjunto de dados

- **microatividade 02-Criar um subconjunto de dados**
  - Seleção de um subconjunto do dataset (ex.: colunas específicas e/ou filtragem de linhas) para facilitar análises e testes.
  - Objetivo típico: reduzir dimensionalidade/volume e validar transformações em um recorte do dado.
 
  ### Microatividade 03 — Configurar o número máximo de linhas exibidas

- **Microatividade 3: Configurar o número máximo de linhas exibidas**
  - Ajuste de opções de visualização do Pandas para melhorar a inspeção em notebooks/terminal.
  - Exemplo comum:
    - `pd.set_option('display.max_rows', N)`

### Microatividade 04 — Exibir as primeiras e últimas "N" linhas

- **Microatividade 04-Exibir as primeiras e últimas "N" linhas**
  - Uso de operações do Pandas para inspecionar rapidamente o dataset.
  - Exemplos comuns:
    - `df.head(N)` para as primeiras linhas
    - `df.tail(N)` para as últimas linhas

### Microatividade 05 — Informações gerais sobre o conjunto de dados

- **Microatividade 5: Informações gerais sobre o conjunto de dados**
  - Coleta de estatísticas e metadados do dataset.
  - Exemplos comuns:
    - `df.info()` (tipos, nulos, memória)
    - `df.describe()` (estatísticas descritivas)
    - `df.shape`, `df.columns`, `df.dtypes`

## Trabalho prático — Passos 1 a 5: Preparação e cópia de segurança

- **Trabalho Prático | Passo 1 ao 5: Preparação e Cópia de Segurança**
  - Estruturação inicial do fluxo de trabalho.
  - Prováveis ações:
    1. Importar bibliotecas (Pandas, NumPy etc.)
    2. Carregar o dataset
    3. Inspecionar o conteúdo (head/info)
    4. Criar uma cópia de segurança do DataFrame (ex.: `df_backup = df.copy()`)
    5. Definir um baseline antes de iniciar limpeza/transformações

## Passo 6 — Tratando a coluna `Calories`

- **Passo 6: Tratando a coluna 'Calories'**
  - Limpeza/conversão de tipos e padronização de valores na coluna `Calories`.
  - Possíveis atividades:
    - Converter para numérico: `pd.to_numeric(df['Calories'], errors='coerce')`
    - Tratar valores inválidos/ausentes
    - Validar intervalos esperados

## Passo 7 — O desafio da coluna `Date` (Parte 1)

- **Passo 7: O desafio da coluna 'Date' (Parte 1)**
  - Diagnóstico inicial dos problemas de data (formatos mistos, strings inválidas, timezone etc.).
  - Primeiras tentativas de padronização/conversão.

## Passos 8 a 11 — Corrigindo as datas e formatos

- **Passo 8 ao 11: Corrigindo as Datas e Formatos**
  - Consolidação da limpeza de datas e padronização de formatos.
  - Possíveis atividades:
    - Conversão para datetime: `pd.to_datetime(df['Date'], errors='coerce', dayfirst=True)` (dependendo do dataset)
    - Correção de linhas com datas inválidas
    - Extração/normalização de componentes (ano/mês/dia) quando necessário
    - Ajuste de formatos finais para exportação/relatórios

## Passo 12 — Removendo registros nulos

- **Passo 12: Removendo registros nulos**
  - Remoção (ou tratamento) de registros com valores ausentes.
  - Exemplos comuns:
    - `df.dropna()` para remover linhas com nulos
    - `df.dropna(subset=[...])` para focar em colunas críticas
    - Alternativamente, preenchimento com `fillna(...)` quando fizer sentido

---

