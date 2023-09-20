import pandas as pd

# Substitua "consolidado.csv" pelo caminho completo do arquivo CSV, se estiver em um local diferente
caminho_arquivo_csv = "consolidado.csv"

# Lê o arquivo CSV e armazena os dados em um DataFrame
dados_consolidados = pd.read_csv(caminho_arquivo_csv, encoding='ISO-8859-1')

# Verifica se o DataFrame está vazio
if dados_consolidados.empty:
    print("O DataFrame está vazio.")
else:
    print(dados_consolidados.head())
