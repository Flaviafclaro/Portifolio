# Análise Exploratória de Vendas (AnaliseExploratoria.py)

Este é um projeto de análise exploratória de vendas utilizando Python e a biblioteca pandas. O objetivo deste projeto é explorar um conjunto de dados de vendas de uma planilha excel com 70 mil registros e realizar diversas análises estatísticas e de agrupamento para extrair insights e informações úteis.

## Funcionalidades

- Carregamento dos dados de vendas a partir de um arquivo Excel
- Listagem das primeiras e últimas linhas dos dados
- Estatísticas descritivas dos dados
- Contagem de vendas por loja e forma de pagamento
- Agrupamento dos dados por loja, estado e cidade para análises de faturamento

## Requisitos

- Python 3.x
- Pandas
- XlsxWriter

## Como usar

1. Instale as bibliotecas necessárias:

2. Faça o download do arquivo `vendas.xlsx` e coloque-o na mesma pasta do código.

3. Execute o arquivo `analise.py`:

4. Será gerado um arquivo `AnaliseExploratoria.xlsx` com os resultados da análise.

## Resultados

Os resultados da análise serão salvos no arquivo `AnaliseExploratoria.xlsx`, contendo três planilhas:

1. **Resultados**: Primeiras e últimas linhas dos dados, com ajuste automático da largura das colunas.
2. **Estatisticas**: Estatísticas descritivas dos dados, quantidade de vendas por tamanho do copo e forma de pagamento.
3. **Agrupamento**: Faturamento por loja, média de faturamento das lojas, faturamento por estado e faturamento por cidade.

![resultados](https://github.com/Flaviafclaro/Portifolio/assets/93830753/255df5d6-ec77-483b-95a1-0582d224217b)
![estatisticas](https://github.com/Flaviafclaro/Portifolio/assets/93830753/4b1e7974-e72e-4c93-a1a3-e6286d6127bd)
![agrupamento](https://github.com/Flaviafclaro/Portifolio/assets/93830753/2dfecf45-ec01-47de-809b-f782a7b5731d)

# Análise de Vendas - Código e Gráficos (Graficos.py)

Contém um código em Python para realizar análise de vendas a partir de um arquivo Excel e gerar gráficos interativos utilizando a biblioteca Plotly Express. Os gráficos gerados são salvos em arquivos HTML.

## Pré-requisitos

- Python 3.x
- Pandas
- Plotly Express

Certifique-se de ter o Python instalado e as bibliotecas necessárias antes de executar o código.

## Como usar

1. Faça o download do arquivo `vendas.xlsx` contendo os dados das vendas.

2. Execute o código `analise_vendas.py` para realizar a análise e gerar os gráficos.

3. Os gráficos gerados serão salvos em arquivos HTML com os nomes `grafico-{coluna}.html` e `grafico_dinamico.html`.

## Estrutura do código

- O código carrega os dados do arquivo Excel utilizando a biblioteca Pandas.

- Em seguida, são criados gráficos de histograma para cada coluna especificada na lista `lista_colunas`. Os gráficos são salvos em arquivos HTML separados.

- Além disso, é criado um gráfico dinâmico que mostra o valor acumulado das vendas por loja ao longo do tempo. Esse gráfico é salvo em um arquivo HTML separado.

## Exemplos de Gráficos Gerados

Os gráficos interativos estão hospedados nos links abaixo:

Gráfico Animado: https://flaviafclaro.github.io/site/graficos/grafico_dinamico.html

Receita por Loja: Receita por Loja: https://flaviafclaro.github.io/site/graficos/grafico-loja.html

Receita por Cidade: https://flaviafclaro.github.io/site/graficos/grafico-cidade.html

Receita por Estado: https://flaviafclaro.github.io/site/graficos/grafico-estado.html

Receita por Forma de Pagamento: https://flaviafclaro.github.io/site/graficos/grafico-forma_pagamento.html

Receita por Local de Comsumo: https://flaviafclaro.github.io/site/graficos/grafico-local_consumo.html

Receita por Região: https://flaviafclaro.github.io/site/graficos/grafico-regiao.html

Receita por Tamanho do Copo: https://flaviafclaro.github.io/site/graficos/grafico-tamanho.html

Abaixo estão prévias dos gráficos gerados:
![Receita_Cidade](https://github.com/Flaviafclaro/Portifolio/assets/93830753/52d605cc-4712-4889-b2dc-d81da3ac50be)
![Receita_Estado](https://github.com/Flaviafclaro/Portifolio/assets/93830753/6041d009-21da-477d-883b-87697dc0a5a7)
![Receita_Forma![Receita_FormaPgto](https://github.com/Flaviafclaro/Portifolio/assets/93830753/110d73eb-b2b9-4a92-9820-aab7993795a0)
![Receita_LocalConsumo](https://github.com/Flaviafclaro/Portifolio/assets/93830753/f7a34e46-6ef9-4451-80ff-b96462b6c42a)
![Receita_PorLoja](https://github.com/Flaviafclaro/Portifolio/assets/93830753/efb08af4-871a-440f-a6b2-81f631066746)
![Receita_porRegiao](https://github.com/Flaviafclaro/Portifolio/assets/93830753/a3ad01fe-388c-49d6-8aa5-9347316520b2)
![Receita_TamanhoCopo](https://github.com/Flaviafclaro/Portifolio/assets/93830753/d42ebf25-936d-433b-ab94-46da3bd47f40)
![GraficoAnimado](https://github.com/Flaviafclaro/Portifolio/assets/93830753/e06450f5-02e0-4f47-b25d-cb9f2f2f2bb1)
