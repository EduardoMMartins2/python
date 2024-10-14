import numpy as np
#import statsmodels as sm
import statsmodels.api as sm
#import statsmodels.formula.api as smf
from patsy import dmatrices
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor  # Importação corrigida


#carrega dados
caminho = r"C:\Users\Win11\Desktop\Modelo.csv"          
base_dados = pd.read_csv(caminho)

#print(base_dados.head())

#primeira rodada do modelo
#y, X = dmatrices("total ~ ataque_casa + ataque_fora + ataque_p_casa + ataque_p_fora + fin_casa + fin_fora + cht_gol_casa + cht_gol_fora + escanteio_casa + escanteio_fora + cruzamento_casa + cruzamento_fora + placar_casa + placar_fora + tempo", data=base_dados, return_type ='dataframe')


#segunda rodada do modelo
y, X = dmatrices("total ~ ataque_casa + ataque_fora + ataque_p_casa + ataque_p_fora + fin_casa + fin_fora + cht_gol_casa + cht_gol_fora + escanteio_casa + escanteio_fora + cruzamento_casa + cruzamento_fora + placar_casa + placar_fora", data=base_dados, return_type ='dataframe')


#terceira rodada do modelo - 0 + indica q não haverá intercepto no modelo
#y, X = dmatrices("total ~ 0 + ataque_casa + ataque_fora + ataque_p_casa + ataque_p_fora + fin_casa + fin_fora + cht_gol_casa + cht_gol_fora + escanteio_casa + escanteio_fora + cruzamento_casa + cruzamento_fora + placar_casa + placar_fora", data=base_dados, return_type ='dataframe')


#quarta rodada
#base_dados['ataque_casa_'] = base_dados['ataque_p_casa'] / base_dados["ataque_casa"]
#base_dados['ataque_p_casa_'] = base_dados['ataque_p_fora'] / base_dados["ataque_fora"]
#y, X = dmatrices("total ~ 0 + ataque_casa_ + ataque_p_casa_ + fin_casa + fin_fora + cht_gol_casa + cht_gol_fora + escanteio_casa + escanteio_fora + cruzamento_casa + cruzamento_fora + placar_casa + placar_fora", data=base_dados, return_type ='dataframe')


#print(y[:3])
#print(X[:3])

mod = sm.OLS(endog=y, exog=X)
res = mod.fit()

print(res.summary())

#estimativa de parametros
print("\nParâmetros")
print(res.params)
#r quadrado digitado
print("\nR²")
print(res.rsquared)


print("\nTeste para Linearidade - Primeiro valor estatística F, segundo estatítistica P")
print(sm.stats.linear_rainbow(res))


print("\nCorrelação")
corr_matrix = base_dados.corr()
print(corr_matrix)


# Cálculo do VIF
print("\nVIF - Variância Inflação Fator")
vif_data = pd.DataFrame()
vif_data["Variáveis"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]

print(vif_data)



#Monta Gráfico
#print("\nFigura")
#figura = sm.graphics.plot_partregress('total', 'ataque_casa', 'ataque_fora', data=base_dados, obs_labels=False)
#plt.show()