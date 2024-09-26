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