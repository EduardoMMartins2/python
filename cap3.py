bicicletas = ['trek', 'cannondale', 'redline', 'specialized']
print(bicicletas)

#acessando elementos da lista #o primeiro item da lista é Zero
print(bicicletas[0])
print(bicicletas[0].title())
#para retornar o item final, basta usar -1
print(bicicletas[-1].upper())

message = f"My first bicycle was a {bicicletas[0].title()}."
print(message)


#Modificando, adicionando e removendo elementos - Modificando elementos em uma lista - Motocicletas
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
#modificou
motocicletas[0] = 'ducati'
print(motocicletas)

#anexando ao final da lista
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
#anexou ao fim
motocicletas.append('ducati')
print(motocicletas)

motocicletas = []
motocicletas.append('honda')
print(motocicletas)
motocicletas.append('yamaha')
print(motocicletas)
motocicletas.append('suzuki')
print(motocicletas)

#Inserindo elementos em uma lista - o insert empurra os outros elementos e insere no índice desejado - o insert não remove o indice 0
motocicletas.insert(0, 'ducati')
print(motocicletas)

#Removendo elementos de uma lista - del caso saiba qual elemento e posição
del motocicletas[0]
print(motocicletas)
del motocicletas[1]
print(motocicletas)

#Removendo elemento com o pop  - se usar o método pop, o elemento que removemos da lista não fica mais armazenado nela
motocicletas = ['honda', 'yamaha', 'suzuki']
print(motocicletas)
popped_motocicletas = motocicletas.pop()
print(motocicletas)
print(popped_motocicletas)
#imagina que o último registro exibe a última moto que compramos
print(f'The last motorcycle I owned was a {popped_motocicletas.title()}.')

#Removendo elementos de qualquer posição em uma lista
motocicletas = ['honda', 'yamaha', 'suzuki']
first_owned = motocicletas.pop(0)
print(f'The first motorcycle I owned was a {first_owned.title()}.')

#SE EU USAR O DEL, NUNCA MAIS VOU PODER USAR ESSE ELEMENTO DA LISTA. SE USAR O POP, PODEREI RECORRER A QUALQUER HORA NO PROGRAMA POR ESSE ELEMENTO

#Removendo um elemento por valor
motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocicletas)
motocicletas.remove('ducati')
print(motocicletas)

motocicletas = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motocicletas)
too_expensive = 'ducati'
motocicletas.remove(too_expensive)
print(motocicletas)
print(f'\nA {too_expensive.title()} is too expensive for me.')


#Ordenando Permanente
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
#ordem reversa
cars_2 = ['bmw', 'audi', 'toyota', 'subaru']
cars_2.sort(reverse=True)
print(cars_2)

#Ordenando temporariamente
cars_3 = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars_3)

print("\nHere is the sorted list:")
print(sorted(cars_3))

print("\nHere is the original list again:")
print(cars_3)
#Ordenar sempre depois de minúsculas, maiúsculas perdem o contexto

#Exibindo uma lista em ordem inversa - não é ordem alfabética, apenas transforma a lista do último para o primeiro
cars_4 = ['bmw', 'audi', 'toyota', 'subaru']
print(cars_4)
#altera permanente
cars_4.reverse()
print(cars_4)

#Identificando o tamanho da lista - len() - começa contando de 1 e não 0
print(len(cars_4))


#Evite erros de índice ao trabalhar com listas
#Ver a lista original ou números de elementos ajuda a resolver erros. Pode ser q sua lista tenha sido manipulada dinamicamente em algum passo
#erro: list index out of range
teste_erro = ['elemento um', 'elemento dois']
#print(teste_erro[3])