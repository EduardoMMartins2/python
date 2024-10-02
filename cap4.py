#Trabalhando com Listas

#Loops percorrendo uma lista inteira
# For - mesma ação em todos elementos da lista

magicians = ['alice', 'david', 'carolina']
# extraio 1 nome de cada da lista magicians, associando a variável magician

################################################################
# Para cada mágico na lista de mágicos, exiba o nome do mágico #
################################################################
for magician in magicians:
    print(magician)


# Análise minuciosa dos loops
# o python executa " for magician in magicians " para cada linha da lista, um conjunto de etapas é repetido uma vez para cada elemento da list

# ao escrever o loop, é importante o nome da variável que retornará apenas 1 elemento da lista, listas normalmente está associada a vários elementos, já essa variável está associada apenas a 1 elemento (por exemplo magician, é apenas "mágico", enquanto magicians é "mágicos")
# for cat in cats:
# for dog in dogs:
#for item in list_of_items:
# usar singular e plural pode ajustar a saber se estou executando uma variável ou uma lista de elementos


#Fazendo mais tarefas dentro de um loop For
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
#cada linha identada é executada uma vez para cada valor na lista, posso fazer oq quiser com cada valor da lista
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

#Fazendo mais tarefas após usar um loop for - linha não identada, executa apenas 1x, pois, dentro do for ela executa N vezes [tamanho da lista]
print(f"Thank you, everyone. That was a great magic show!")


#Evitando Erros de indentação
    # Esquecendo da indentação
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
#print(magician) - incorreto
    print(magician)

    #Esquecendo de indentar linhas adicionais
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
print(f"I Can't wait to see your next trick, {magician.title()}.\n")
# a linha acima é um erro lógico, faltou a indentação, e portanto, o retorno foi sobre o último nome relacionado a variável magician da lista


#Identando Desnecessariamente - só idente se for necessário, caso contrário poderá retornar erro
message = "Hello Python World!\n\n"
    #print(message) - errado
print(message)


#Identando denecessariamente após o loop
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print(f"Thank you everyone, that was a great magic show!") #essa linha não deveria estar identada


#Esquecendo os dois-pontos  - os dois pontos ao final da instrução, informam ao python para interpretar a próxima linha como início do loop
magicians = ['alice', 'david', 'carolina']
#for magician in magicians      - erro - sytaxerror: expected ':'
for magician in magicians:
    print(magician)


# Listas Numéricas
#Função Range - gera uma série de números - atencao os resultados serão apénas uma sequencia de números
for value in range(1,5):
    print(f"{value}\n")
#o range faz calcular começando do primeiro valor fornecido e parando no segundo valor fornecido

for value in range(1,6):
    print(value)
print(f"\n")

for value in range(6):
    print(value)
print(f"\n")

#Usando range() para criar uma lista de números - basta envolver range() em um list()
numbers = list(range(1,6))
print(numbers)

#Se passarmos um terceiro argumento para a funcao range(), esse argumento será o "step", e usará como tamanho do "passo" ou intervalo
even_numbers = list(range(2,11,2))
print(even_numbers)
print(f"\n")

#inserir os 10 primeiros números quadrados em uma lista
#começa uma lista vazia
squares = []
#percorre o python de 1 a 10
for value in range(1,11):
    #eleva o valor de cada elemento do loop a segunda potencia
    square = value ** 2
    #atribui a variável lista square
    squares.append(square)

print(squares)

#a mesma coisa  q em cima, porém, código clean
squares = []
for value in range(1,11):
    squares.append(value ** 2)

print(squares)
print(f"\n\n")


#Estatísticas Simples com uma lista de números
digits = []
for digit in range(0,10):
    digits.append(digit)

print(digits)
print(min(digits))
print(max(digits))
print(sum(digits))
print(f"\n\n")


#LIST COMPREHENSIONS - gera uma lista de códigos somente em uma linha de código - combina loop e criação de elementos em uma linha
#abre a lista [colchetes], defina a expressão q eleve ao quadrado, escreva o loop for para gerar os números - não tem 2 pontos no final da expressao
squares = [value ** 2 for value in range(1,11)]
# lista = []
# expressao = value ** 2
# loop = for value in range(1,11)
print(squares)

print(f"\n\n")


#Trabalhando com uma parte da lista
#Fatiando uma Lista
players = ['Grohe', 'Geromel', 'Kannemann', 'Edilson', 'Cortez']
print(players[0:3])

print(players[1:4]) #pula o primeiro elemento  - o zero
print(f"\n")
print(players[:4]) #começa do início da lista
print(players[2:]) #começa do elemento start até o final da lista
print(players[-3:]) # últimos 3 jogadores da lista - índice negativo retorna um elemento a uma certa distancia do final
# é possível colocar o terceiro elemento nos colchetes, indicará qnts elementos o python deve desconsiderar
print(f"\n")


# Percorrendo uma Fatia em Loop
print('Here are the first three players on my team: ')
for player in players[:3]:
    print(player.title())

print(f"\n")

# Copiando uma lista
lanches_meus = ['pizza', 'xis', 'lasanha']
lanches_outros = lanches_meus[:]

lanches_meus.append('coca-cola')
lanches_outros.append('sorvete')

print('Meu lanche favorito é:')
print(lanches_meus)
print('\nOs lanches favoritos dos meus amigos são:')
print(lanches_outros)

print(f"\n")
# caso eu atribua uma lista a outra lista, ao incluir elementos na lista A, também incluiremos na lista B e como estamos atribuindo B = A, logo, o elemento adicionado apenas a B também aparecerá em A
my_foods = ['pizza', 'xis', 'lasanha']
friend_foods = my_foods

my_foods.append('coca-cola')
friend_foods.append('sorvete')

print('Meu lanche favorito é:')
print(my_foods)
print('\nOs lanches favoritos dos meus amigos são:')
print(friend_foods)


#Tuplas - PG 102 são listas imutáveis - listas que não podem mudar são tuplas