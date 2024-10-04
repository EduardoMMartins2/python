#Instruções IF
print(f"\n for in no if")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#Testes Condicionais
# o python avalia os valores, caso true, executa instrução após o if
# caso seja false, desconsidera a instrução if

print(f"\n = e ==")
#Verificando Igualdade
# car = 'bmw'   -> significa declaração - o valor atribuído é igual a "bmw"
car = 'bmw'
# já o duplo sinal equivale a " o valor do carro é uma 'bmw' ?"
print(car == 'bmw')  #retorna true
print(car == 'audi') #retorna false

print(f"\n A != a = true")
#Ignorando letras maiusculas e minusculas ao verificar iguldade
# É DIFERENCIADO MAIUSCULA DE MINUSCULA NOS TESTES
car = 'Audi'
car == 'audi'  # retorno > falso
# é recomendado que seja testado valores com a letra minúscula
car = 'Audi'
print(car.lower() == 'audi') # retorno -> true

print(f"\n !=")
#Verificando a diferença  !=
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

print(f"\n Comparacao Numerica")
# Comparacao Numérica
age = 18
print(age == 18)

answer = 17
# se answer for diferente de quarenta e dois, retorna a mensagem
if answer != 42:
    print("That is not the correct answer. Please try again!")

print(f"\nVerificando Múltiplas Condições ao mesmo tempo!!")
#and e or

#and
age_0 = 22
age_1 = 18
print( age_0 >= 21 and age_1 >= 21 )
age_1 = 22
print( age_0 >= 21 and age_1 >= 21 )
#melhor legibilidade
print((age_0 >= 21) and (age_1 >= 22))

#or
age_0 = 22
age_1 = 18
print( age_0 >= 21 or age_1 >= 21 )
age_0 = 18
print( age_0 >= 21 or age_1 >= 21 )


print(f'\nVerifica se o valor está na Lista')
# verificar se está na lista com IN
requested_toppings = ['mushrooms', 'onions', 'pineapple']
teste_1 = 'mushrooms' in requested_toppings
print(teste_1)
teste_2 = 'pepperoni' in requested_toppings
print(teste_2)


print(f'\nVerifica se o valor NÃO está na Lista')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you can post a response if you wish.')
# se marie não está na lista de usuários banidos, então executa a mensagem

print(f'\nExpressões Booleanas')
# valor booleano ou é true ou é false
game_active = True
can_edit = False


print(f"\n\nIF")
#Simples
# if teste_condicional:
# faça alguma coisa
# se a condicional for verdadeira, será executado o if
print('Se a sua idade for maior que 18 anos, você pode votar!')
age = 19
if age > 18:
    print('Você pode votar!')

#Instrução IF-Else
print(f'\nInstrução IF-ELSE')
age = 17
if age >= 18:
    print('Você pode votar!')
else:
    print('Você não pode votar!')

#Instrução IF-ELIF-ELSE
print(f'\nInstrução IF-ELIF-ELSE')
# mais de uma situação
#o python executa somente um bloco em uma sequencia,quando 1 passa,será exibido
age = 12
if age < 4:
    print('É de graça!')
elif age < 18:
    print('Custa 25 reais!')
else:
    print('Custa 50 Reais!')

#ou faz dessa forma
if age < 4:
    preco = 'de graça'
elif age < 18:
    preco = '25 reais'
else:
    preco = '50 reais'
print(f'O valo do ingresso é {preco}!')


print(f'\nUsando Múltiplos blocos de elif')
# dá para usar quantos elif quiser
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'Your admission cost is ${price}')