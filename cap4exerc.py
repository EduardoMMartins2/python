# 4.1
sabores = ['carne', 'frango', 'calabresa', 'bacon']
for sabor in sabores:
    print(f" Gosto muito do sabor {sabor.title()}!!")
print(f"\n Eu amo pizza! <3\n\n")

# 4.2
animais = ['gato', 'tigre', 'onça']
for animal in animais:
    print(f"Ele é felino fofinho e dá vontade de amassar ( {animal.title()} ).")
print(f"Todos esses animais são felinos!!!")

print(f"\n\n")

# 4.3
vinte = [vintes for vintes in range(1,21)]
print(vinte)

# 4.4
milhao = []
for unidade in range(0,1000000,1):
#    print(unidade)             # comentei para não demorar tanto
    milhao.append(unidade)

# print(milhao)                 # comentei para não demorar tanto

# 4.5
print(min(milhao))
print(max(milhao))
print(sum(milhao))

# 4.6
milhaoImpar = []
for unidade in range(1,100,2):
#    print(unidade)             # comentei para não demorar tanto
    milhaoImpar.append(unidade)
print(milhaoImpar)

# 4.7
multiplos = []
for valor in range(1,11):
    elemento = valor * 3
    multiplos.append(elemento)

print(multiplos)

# 4.8
cubos = []
for numero in range(1,11):
    cubo = numero ** 3
    cubos.append(cubo)

print(cubos)

# 4.9 - lista, expressao, loop
cubos_comprehensions = [numero ** 3 for numero in range(1,11)]
print(cubos_comprehensions)

print(f"\n\n")

# 4.10
animais2 = ['gato', 'tigre', 'onça', 'cachorro', 'arara']

print(f"Os três primeiros elmentos da lista são:")
print(animais2[:3])
print(f"Os três elementos da metade na lista são:")
# (len(animais2)-1) = 4 penultimo elemento da lista
print(animais2[1: (len(animais2)-1) ])
print(f"Os três últimos elmentos da lista são:")
print(animais2[-3:])



print(f"\n\nExercicio 4.11")
# 4.11
novosSabores = sabores[:]
print(sabores)
novosSabores.append('gorgonzola')
sabores.append('file')

print(f"Minhas pizzas favoritas são: ")
for pizza in sabores:
    print(pizza)
print(f"Minhas novas pizzas favoritas são: ")
for pizzaNova in novosSabores:
    print(pizzaNova)


print(f"\n\nExercício 4.12")
# 4.12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite food are: ')
for food in my_foods:
    print(food.title())

print(f"\nMy friend's favorite foods are:")
for food1 in friend_foods:
    print(food1.title())
# food1 = [food1 for food1 in friend_foods] - list comprehension, mas n eh isso q o exercicio pede
#print(food1)