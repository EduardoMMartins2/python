#uma vez criada a tupla, ela NÃO PODE MAIS MUDAR, alterar ou acrescentar!!
# Tupla - USA PARÊNTESIS
primeira_tupla = ("Let's Data", 4, 2.1, False)
print(primeira_tupla)

#se atribuir valores separados por vírgula, o python insere como tupla
outra_tupla = 1,2,3, "de Oliveira 4"
print(outra_tupla)
print( type(outra_tupla) )

#o acesso aos elementos é da mesma forma
print( primeira_tupla[0] )