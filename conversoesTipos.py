#tipo Lista
raul_seixas = ["Eu prefiro seeeer", "essa metamorfose ambulante"]
print(raul_seixas)
print(type(raul_seixas))

#tipo Tupla
raul_seixas = tuple(raul_seixas)
print(type(raul_seixas))

#tipo Conjunto
raul_seixas = set(raul_seixas)
print(type(raul_seixas))

#para converter em dicionário, é necessário criar uma lista ou tuplas com chave-valor
dicionario_lista_tupla = dict([("DF", "Distrito Federal"), ("GO", "Goiás")])
print(dicionario_lista_tupla)
print(type(dicionario_lista_tupla))