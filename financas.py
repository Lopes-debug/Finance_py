import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from pandas_datareader import data as pdr
import yfinance as yf

# Obtenção dos dados diretamente com yfinance
# cotacao_ibov = yf.download('^BVSP', start= '2022-01-01', end= '2022-03-01')

# # Criar gráfico correspondente
# cotacao_ibov['Adj Close'].plot(figsize=(15,5))

# # Obter percentual entre primeiro e último valor
# div_ibov = cotacao_ibov['Adj Close'][-1] / cotacao_ibov['Adj Close'][0] - 1
# print('Percentual: {:.2%}'.format(div_ibov))

# Acrescentar Media Movel no gráfico
# cotacao_ibov['Adj Close'].plot(figsize=(15,5), label='IBOV')
# cotacao_ibov['Adj Close'].rolling(5).mean().plot(label='MM5')
# plt.legend()
# plt.show()

## Aula 2

# excel = pd.read_excel(r'C:\Users\leand\OneDrive\Documentos\hashtag\f_financas\Carteira.xlsx')

# df_carteira = pd.DataFrame()  #start a empty DataFrame

# for empresa in excel['Ativos']:
#     #Importar carteira de empresas da web e adicioná-las ao DataFrame vazio
#     df_carteira[empresa] = yf.download(f'{empresa}.SA', start= '2022-01-01', end= '2022-03-01')['Adj Close']  

## Remover empresas com valores vazios na coluna
## Functions to filter DataFrame
# print(df_carteira.info())  #show info of DataFrame
# media = df_carteira.mean()  #show the mean of all columns
# df_carteira = df_carteira.fillna(media)  #change empty rows to total mean
# df_carteira = df_carteira.ffill()  #change empty rows to value anterior
# df_carteira = df_carteira.dropna(axis=1, how='all')
 #remove columns que have anyone cell empty


## Normalizar carteira
# df_carteira_norm = df_carteira / df_carteira.iloc[0]
# df_carteira_norm.plot(figsize=(15,5))
# plt.legend(loc= 'upper left')
# plt.show()


## Calcular valor investido
# investimento = pd.DataFrame()
# for ativo in excel['Ativos']:
#     if ativo in df_carteira.columns:
#         investimento[ativo] = df_carteira[ativo] * excel.loc[excel['Ativos']==ativo, 'Qtde'].values[0]
        
    

## Comparar minha carteira com IBOV
# cotacao_ibov = yf.download('^BVSP', start= '2022-01-01', end= '2022-03-01')

# investimento['Total'] = investimento.sum(axis=1)
# investimento_norm = investimento / investimento.iloc[0]
# cotacao_ibov_norm = cotacao_ibov / cotacao_ibov.iloc[0]

# investimento_norm['Total'].plot(figsize=(15,5), label = 'Carteira')
# cotacao_ibov_norm['Adj Close'].plot(label = 'IBOV')
# plt.legend()


## Retorno da Carteira e do IBOV
# retorno_cart = investimento['Total'][-1] / investimento['Total'][0] - 1
# retorno_ibov = cotacao_ibov['Adj Close'][-1] / cotacao_ibov['Adj Close'][0] - 1

# print('O retorno do investimento na carteira foi de {:.2%}'.format(retorno_cart))
# print('O retorno do investimento na carteira IBOV foi de {:.2%}'.format(retorno_ibov))

## Correlação entre os dois
# correlacao = investimento['Total'].corr(cotacao_ibov['Adj Close'])
# print(correlacao)