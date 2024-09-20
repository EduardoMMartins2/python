# dicionário é o tipo de dado que recebe uma chave e um valor - pares
# Dicionário - 
dicionario = {"píton": "Serpente da Ásia e da África, não venenosa, que constringe as presas com seus anéis."
              }
print(dicionario)
print(type(dicionario))

#as chaves devem ser únicas
#                 chave : valor
out_dicionario = {"nome": "Eduardo Moraes Martins", "idade": 29}
#out_dicionario, tem 2 elementos
print(out_dicionario)

#chaves de dicionários são únicas
#para acessar basta:
print( out_dicionario["nome"] )

# Há três métodos importantes keys(), values() e items()
#keys = retorna todas as chaves do dicionário
print( out_dicionario.keys() )
#values = retorna todos os valores do dicionário
print( out_dicionario.values() )
#items = retorna todos os pares de chave: valor do dicionário
print( out_dicionario.items() )

#para remover, usamos o del e a chave a ser removida - também removerá o valor
del out_dicionario["idade"]
print( out_dicionario )