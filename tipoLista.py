#Lista - USA COLCHETES
primeira_lista = ["Let's Data", 4, 2.1, False]
print(primeira_lista)
print(primeira_lista[0])
print(primeira_lista[-1])
#o Índice começa do item 0.

#para adicionar elemento na lista, no final da lista
lista = ["1 elemento"]
print(lista)
lista.append("2 elemento")
print(lista)

#para remover elementos - colocar a posição
del lista[1]
print(lista)
# ou pode remover com o elemento que queremos remover
lista.append("Adicionei um exemplo")
print(lista)
#para remover o exemplo
lista.remove("Adicionei um exemplo")
print(lista)

#para alterar um valor
lista_nova = ["Let's Data", "Data", "4tw"]
print(lista_nova)
lista_nova[2] = "ftw"
print(lista_nova)

#para saber o tamanho de uma lista len()
print( len(lista_nova) )

#a STRING se comporta como LISTA!
listaString = "Let's Data"
print( listaString[6] )
print( type(listaString) )