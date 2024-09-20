# conjunto NÃO TEM ORDEM definida, não pode ter repetidos
# Conjuntos - USA CHAVES
primeiro_conjunto = {"Let's Data", 4, 2.1, False}
print(primeiro_conjunto)

# e se adicionar elemento repetido ?
segundo_conjunto = {1, 1, 3, 3, "Let's", "Let's", "Data"}
print( segundo_conjunto )
print( type(segundo_conjunto) )

#para incluir o elemento no conjunto, adiciona em qualquer ordem
segundo_conjunto.add("1 + elemento")
print(segundo_conjunto)

# é necessário atribuir o elemento
elemento = segundo_conjunto.pop()
print(elemento)
print(segundo_conjunto)
#DICA: para remover um item em específico do conjunto, deve-se transformar em lista e acessar conforme exibido na primeira parte do treinamento
