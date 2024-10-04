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