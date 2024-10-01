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