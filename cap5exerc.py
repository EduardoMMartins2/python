print(f'\n #5.1 - Testes Condicionais')
idade = 29
print(f'Minha idade é 29 anos?')
print(idade == 29)
print(f'Minha idade é 28 anos?')
print(idade == 29)

# operacoes
idade = 29
print(f'\nMinha idade é != de 29?')
print ( idade != 29)
print(f'Minha idade é != de 29?')
print ( idade != 15)

print(f'\nMinha idade é >= de 29?')
print ( idade >= 29)

idade_lista = [29]
print(f'\nMinha idade está na lista das idades?')
print(f'{29 in idade_lista}')
print(f'Minha idade não está na lista das idades?')
pergunta = 10
if pergunta not in idade_lista:
# caso a idade não esteja na lista, será exibido o print abaixo
    print(f'Minha idade não está na lista? {pergunta}')

print(f'\n#5.2 +Testes Condicionais')
carros = ['gol', 'celta', 'fusca', 'mobi', 'kwid']
primeiro_carro = 'Gol'
segundo_carro = 'Celta'

print(f'Meu primeiro carro foi um gol? { (primeiro_carro.lower()) == 'gol'}')
print(f'Meus primeiros carros foram Gol ou Celta?')
print(primeiro_carro.lower() == 'gol' or segundo_carro != 'celta')
print(f'Meu primeiro carro foi um Gol e o segundo um Celta?')
print(primeiro_carro.lower() == 'gol' and segundo_carro.lower() == 'celta')
print(primeiro_carro == 'gol' and segundo_carro == 'celta')
print(primeiro_carro != 'gol' and segundo_carro != 'celta')

print(f'\nO {segundo_carro} pertence a lista de carros?')
if segundo_carro.lower() in carros:
    print(f'\t{segundo_carro.title()}, este carro pertence a lista.')


print(f'\n\n#5.3 Cores de Alienígenas')
alien_color = "verde"
if 'verde' in alien_color:
    print('Você acabou de ganhar 5 pontos.')

if 'amarelo' in alien_color:
    print('Você acabou de ganhar 5 pontos.')


print(f'\n\n#5.4 Cores de Alienígenas #2')
if alien_color == 'verde':
    print("Você acabou de ganhar 5 pontos por abrir fogo contra alienígena.")
else:
    print("Você acabou de ganhar 10 pontos.")

if alien_color == 'vermelho':
    print("Você acabou de ganhar 5 pontos por abrir fogo contra alienígena.")
else:
    print("Você acabou de ganhar 10 pontos.")


print(f'\n\n#5.5 Cores de Alienígenas #3')
alien_color = 'amarelo'
if alien_color == 'verde':
    print('Você ganhou 5 pontos!')
elif alien_color == 'amarelo':
    print('Você ganhou 10 pontos.')
elif alien_color == 'vermelho':
    print('Você ganhou 15 pontos.')
else:
    print('Você ganhou 0 pontos!')

alien_color = 'verde'
if alien_color == 'verde':
    print('Você ganhou 5 pontos!')
elif alien_color == 'amarelo':
    print('Você ganhou 10 pontos.')
elif alien_color == 'vermelho':
    print('Você ganhou 15 pontos.')
else:
    print('Você ganhou 0 pontos!')

alien_color = 'vermelho'
if alien_color == 'verde':
    print('Você ganhou 5 pontos!')
elif alien_color == 'amarelo':
    print('Você ganhou 10 pontos.')
elif alien_color == 'vermelho':
    print('Você ganhou 15 pontos.')
else:
    print('Você ganhou 0 pontos!')


print('\n\n#5.6 Fases da Vida')
#idade = int(input("Qual sua idade? "))
idade = 29
if idade < 2:
    print('Você é um neném')
elif idade < 4:
    print('Você é uma criança')
elif idade < 13:
    print('Você é um menine KKKKKK')
elif  idade < 20:
    print('Você é um adolescente')
elif idade < 65:
    print('Você é um adulto')
elif idade >= 65:
    print('Tu é veio!')


print('\n\n#5.7 Fruta Favorita')
frutas = ['maça', 'banana', 'laranja', 'pessego', 'abacaxi']

#esse programa nao retorna nada, caso seja true
if 'bergamota' not in frutas:
    print('Essa fruta não está na lista!')

print(f'\n')
if 'laranja' in frutas:
    print('Essa fruta está na lista!')
else:
    print('Essa fruta não está na lista!')

print(f'\n')
if 'limao' in frutas:
    print('Essa fruta está na lista!')
elif 'abacate' in frutas:
    print('Essa fruta está na lista!')
elif 'goiaba' in frutas:
    print('Essa fruta está na lista!')
else:
    print('Essa fruta não está na lista!')


print('\n\n#5.8 Olá, admin')
usuarios = ['admin', 'eduardo', 'evandro', 'teemo', 'dudu']
for usuario in usuarios:
    if usuario == 'admin':
        print(f'{usuario.title()}, oq tu quer hoje seu merda?')
    else:
        print(f'Bem-Vindo, fiadapu {usuario.title()}')

print(f'\n#5.9 Sem Usuário')
#usuarios1 = ['admin', 'eduardo', 'evandro', 'teemo', 'dudu']
usuarios1 = []
#se a lista contém elementos
if usuarios1:
    for usuario in usuarios1:
        if usuario == 'admin':
            print(f'{usuario.title()}, oq tu quer hoje seu merda?')
        else:
            print(f'Bem-Vindo, fiadapu {usuario.title()}')
else:
    print(f'Encontre algum fodido')


print(f'\n#5.10 Verificando nomes de Usuários')
new_users = ['marcal', 'bolsonaro', 'xandao']
current_users = ['Bolsonaro', 'lula', 'dilma', 'xandao', 'temer']

for current_user in current_users:
    #se liga no lower aqui, ele garante q o bolsonaro está com letra minúscula
    if current_user.lower() in new_users:
        print(f'Usuário {current_user} já cadastrado! Use outro!')
    else:
        print(f'Usuário {current_user} novo!')


print(f'\n\n#5.11 Números Ordinais')
lista = [1,2,3,4,5,6,7,8,9]

for numero in lista:
    if numero == 1:
        print("1st")
    elif numero == 2:
        print("2nd")
    elif numero == 3:
        print("3nd")
    else:
        print(f'{numero}th')
