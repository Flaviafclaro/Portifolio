
import pandas as pd


dados = pd.read_excel("vendas.xlsx") #carregando dados (no cado da planilha excel)

#Análise Exploatória
print(dados.loja.value_counts()) #total de vendas por loja (coluna loja)