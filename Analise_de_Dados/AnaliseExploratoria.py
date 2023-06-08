import pandas as pd
import xlsxwriter

dados = pd.read_excel("vendas.xlsx")  # carregando dados (no caso da planilha excel)

#Análise Exploratória
analise1 = dados.head()  # listar primeiras linhas
analise2 = dados.tail()  # listar últimas linhas
#Estatisticas
analise3 = dados.describe() #Estatisticas
analise4 = dados.tamanho.value_counts() #Vendas por Loja
analise5 = dados.forma_pagamento.value_counts() #Vendas por forma de pagamento
#Agrupamento de dados
analise6 = dados.groupby("loja").preco.sum() #faturamento por loja somando os valores
analise7 = dados.groupby("loja").preco.mean() #média de faturamento por loja
analise8 = dados.groupby("estado").preco.sum() #faturamento por estado
analise9 = dados.groupby(["estado","cidade"]).preco.sum().to_frame() #faturamento por estado

# Criar um objeto ExcelWriter para salvar os dados em um arquivo Excel
writer = pd.ExcelWriter('AnaliseExploratoria.xlsx', engine='xlsxwriter')
workbook = writer.book  # Obter a referência ao objeto workbook

# Definir o formato do título
titulo_formato = workbook.add_format({"bold": True, "font_size": 14})

# Verificar se a planilha 'Resultados' existe
if 'Resultados' in writer.sheets:
    worksheet = writer.sheets['Resultados']
else:
    # Criar a planilha 'Resultados'
    worksheet = workbook.add_worksheet('Resultados')

# Escrever o título "Primeiras 5 linhas da planilha"
worksheet.write(1, 0, "Primeiras 5 linhas da planilha", titulo_formato)

##################################
###### Análise Exploratória ######
##################################

# Ajustar automaticamente a largura das colunas na planilha 'Resultados'
worksheet = writer.sheets['Resultados']
worksheet.autofilter(0, 0, len(dados), len(dados.columns) - 1)  # Aplica um filtro automático nas células
for i, col in enumerate(dados.columns):
    column_width = max(dados[col].astype(str).map(len).max(), len(col))  # Calcula a largura da coluna baseada no maior valor entre o tamanho do conteúdo e o tamanho do nome da coluna
    worksheet.set_column(i, i, column_width + 2)  # Ajusta a largura da coluna com uma margem adicional de 2 caracteres

# Salvar o primeiro DataFrame na planilha 'Resultados'
analise1.to_excel(writer, sheet_name='Resultados', index=True, startrow=2)

# Escrever Últimas 5 linhas da Planilha
worksheet.write(9,0, "Últimas 5 linhas da Planilha", titulo_formato)

# Salvar o segundo DataFrame na planilha 'Resultados' após o primeiro
analise2.to_excel(writer, sheet_name='Resultados', index=True, startrow=analise1.shape[0] + 5)

##########################
###### Estatisticas ######
##########################

# Verificar se a planilha 'Estatisticas' existe
if 'Estatisticas' in writer.sheets:
    worksheet = writer.sheets['Estatisticas']
else:
    # Criar a planilha 'Estatisticas'
    worksheet = workbook.add_worksheet('Estatisticas')

# Ajustar automaticamente a largura das colunas na planilha 'Resultados'
worksheet = writer.sheets['Estatisticas']
worksheet.autofilter(0, 0, len(dados), len(dados.columns) - 1)  # Aplica um filtro automático nas células
for i, col in enumerate(dados.columns):
    column_width = max(dados[col].astype(str).map(len).max(), len(col))  # Calcula a largura da coluna baseada no maior valor entre o tamanho do conteúdo e o tamanho do nome da coluna
    worksheet.set_column(i, i, column_width + 2)  # Ajusta a largura da coluna com uma margem adicional de 2 caracteres
    
# Escrever o título "Preço Médio Por Venda"
worksheet.write(1, 0, "Preço Médio Por Venda", titulo_formato)
# Excluir a coluna de data e hora
analise3 = analise3.drop('data', axis=1)
# Salvar o segundo DataFrame na planilha 'Estatisticas' após o primeiro
analise3.to_excel(writer, sheet_name='Estatisticas', index=True, startrow=2)

# Escrever o título "Quantidade de Vendas Por Tamanho do Copo"
worksheet.write(12, 0, "Quantidade de Vendas Por Tamanho do Copo", titulo_formato)
# Salvar o segundo DataFrame na planilha 'Estatisticas' após o primeiro
analise4.to_excel(writer, sheet_name='Estatisticas', index=True, startrow=analise3.shape[0] + 5)

# Escrever o título "Quantidade de Vendas Por Forma de Pagamento"
worksheet.write(21, 0, "Quantidade de Vendas Por Forma de Pagamento", titulo_formato)
# Salvar o segundo DataFrame na planilha 'Estatisticas' após o primeiro
analise5.to_excel(writer, sheet_name='Estatisticas', index=True, startrow=analise4.shape[0] + 17)

#########################
###### Agrupamento ######
#########################

# Verificar se a planilha 'Agrupamento' existe
if 'Agrupamento' in writer.sheets:
    worksheet = writer.sheets['Agrupamento']
else:
    # Criar a planilha 'Resultados'
    worksheet = workbook.add_worksheet('Agrupamento')
    
# Ajustar automaticamente a largura das colunas na planilha 'Resultados'
worksheet = writer.sheets['Agrupamento']
worksheet.autofilter(0, 0, len(dados), len(dados.columns) - 1)  # Aplica um filtro automático nas células
for i, col in enumerate(dados.columns):
    column_width = max(dados[col].astype(str).map(len).max(), len(col))  # Calcula a largura da coluna baseada no maior valor entre o tamanho do conteúdo e o tamanho do nome da coluna
    worksheet.set_column(i, i, column_width + 2)  # Ajusta a largura da coluna com uma margem adicional de 2 caracteres

# Escrever o título "Faturamento por Loja"
worksheet.write(1, 0, "Faturamento por Loja", titulo_formato)
# Salvar o segundo DataFrame na planilha 'Resultados' após o primeiro
analise6.to_excel(writer, sheet_name='Agrupamento', index=True, startrow=2)

# Escrever o título "Média de Faturamento das Lojas"
worksheet.write(10, 0, "Média de Faturamento das Lojas", titulo_formato)
# Salvar o segundo DataFrame na planilha 'Agrupamento' após o primeiro
analise7.to_excel(writer, sheet_name='Agrupamento', index=True, startrow=analise6.shape[0] + 5)

# Escrever o título "Faruramento por Estado"
worksheet.write(20, 0, "Faruramento por Estado", titulo_formato)
# Salvar o segundo DataFrame na planilha 'Agrupamento' após o primeiro
analise8.to_excel(writer, sheet_name='Agrupamento', index=True, startrow=analise7.shape[0] + 15)

# Escrever o título "Faruramento por Cidade"
worksheet.write(28, 0, "Faruramento por Cidade", titulo_formato)
# Salvar o segundo DataFrame na planilha 'Agrupamento' após o primeiro
analise9.to_excel(writer, sheet_name='Agrupamento', index=True, startrow=analise8.shape[0] + 25)

# Fechar o escritor do Excel
writer._save()
