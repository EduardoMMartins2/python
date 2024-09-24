message = "Hello Python World!"

print(message)

message = "Hello Python Crash Course World!"

print(message)

# é possível mudar o valor da variável a qualquer momento e python manterá o registro do valor atual.

name = "eduardo martins"
print(name.title())
# o title() é um método, todo método é seguido de parentesis, já q provavelemente vai precisar de informações adicionais

print(name.upper())
print(name.lower())
#para deixar todas as letras maiusculas e minúsculas


first_name = "Eduardo"
last_name  = "Moraes"
full_name = f"{first_name} {last_name}"
# f-strings, vem de formato, o python formata a string
print(full_name)

first_name = "Renato"
last_name = "Gaúcho"
full_name = f"{first_name} {last_name}"
mensagem = f"Boa Noite, {full_name.title()}!"
print(mensagem)

#Adicionando Espaço em Branco a string com tabs ou quebra linhas
print("Eduardo")
print("\tEduardo")
print("\nEduardo \nMoraes \nMartins")
print("\nEduardo \n\tMoraes \n\t\tMartins")

#Removendo Espaços em Branco
direita = "direita  "
print(direita)
print(direita.rstrip())
print(direita)
#para remover o espaço em branco da string de forma definitiva, devemos associar o valor removido ao nome da varíavel:
favorite_language = 'python  '
print(favorite_language)
favorite_language = favorite_language.rstrip()
print(favorite_language)
#podemos usar lstrip para remover só da esquerda(left) e ou, usar só strip() remove de ambos os lados
esquerda = " esquerda"
print(esquerda)
print(esquerda.lstrip())
ambos = " ambos "
print(ambos)
print(ambos.strip())

#Removendo Prefixos
nostarch_url = 'https://nostarch.com'
print(nostarch_url)
print(
    nostarch_url.removeprefix('https://')
)
# se quiser atribuir a uma variável para não precisar executar o removeprefix toda hr
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

#Erros de sintaxe string
erro = "One of Python's strengths is its diverse community."
print(erro)
#Se usar apóstrofe, dará erro
# erro = 'One of Python's strengths is its diverse community.'



#Números
#Inteiros
soma = 5 + 3
print(soma)
subtrai = 5 - 3
print(subtrai)
multiplica = 5 * 3
print(multiplica)
divide = 5 / 3
print(divide)
expoente = 3 ** 3
print(expoente)
ordemOp = 2 + 3 * 4 
print(ordemOp)
ordemOp1 = (2 + 3) * 4
print(ordemOp1)

#Floats - ponto decimal
soma1 = 0.1 + 0.1
print(soma1)
multiplicacao2 = 0.2 * 0.2
print(multiplicacao2)

universe_age = 14_000_000_000
print(universe_age)
# 1000 é o mesmo que 1_000

#atribuição múltipla
x, y, z = 0, 0, 0
print(x)
print(y)
print(z)

#constantes - escrever em maiúsculo - não tem como ter variáveis constantes - apenas cuidado com o uso
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS)