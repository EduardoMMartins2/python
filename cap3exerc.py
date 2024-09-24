# 3.1
amiguinhos = ['Eduardo', 'Maryana', 'Evandro', 'Rafael', 'Zayron', 'Cassiano']
print(amiguinhos[0])
print(amiguinhos[1])
print(amiguinhos[4])
print(amiguinhos[-2])


cumprimento = f'Tenho apenas dois únicos amigos verdadeiros, {amiguinhos[1].title()} e {amiguinhos[-4].title()}'
print(cumprimento)

carros = ['Gol', 'Celta', 'Polo', 'Golf']
carro1 = f'Meu primeiro carro foi {carros[0]};'
carro2 = f' Meu segundo carro é {carros[1]};'
carro3 = f'\tO carro de quem beija homens é {carros[2]} ;'
carro4 = f' O sonho do brasileiro iludido é ter o hatchback mais famoso da europa,\no carro popular da europa é o {carros[3]}.'

print(carro1.title())
print(carro2.upper())
print(carro3.lower())
print(carro4)
print(carro4.strip())
print(carro3.rstrip())
print(carro4.removeprefix('O sonho do'))

# 3.4
convidados = ['elisane', 'mae', 'silverio', 'maryana']
print(f'{convidados[0].title()} vem jantar aqui em casa hoje?')
print(f'Oi {convidados[1].title()}, como está?')
print(f'Oi {convidados[-1].title()}, dai cabeção, como vai o cu?')

# 3.5
convidados = ['elisane', 'mae', 'silverio', 'maryana']
nao_vai = 'silverio'
convidados.remove(nao_vai)
print(nao_vai.title())
print(f' O {nao_vai.title()} não irá no jantar.')
print(convidados)

convidados_2 = ['elisane', 'mae', 'silverio', 'maryana']
convidados_2[2] = 'evandro'
print(convidados_2)
print(f'{convidados_2[-2].title()} como vai o cu?')

# 3.6
convidados = ['elisane', 'mae', 'silverio', 'maryana']
print(convidados)
convidados.insert(0, 'evandro')
convidados.insert(3, 'diego')
convidados.append('cassiano')
print(convidados)

# 3.7
print(f'Galera {convidados}, só vou poder convidar duas pessoas!')

popped_convidados_1 = convidados.pop()
print(f'Bah, desculpa, mas infelizmente vai faltar lugar {popped_convidados_1.title()}, espero que você entenda.')
popped_convidados_2 = convidados.pop()
print(f'Bah, desculpa, mas infelizmente vai faltar lugar {popped_convidados_2.title()}, espero que você entenda.')
popped_convidados_3 = convidados.pop()
print(f'Bah, desculpa, mas infelizmente vai faltar lugar {popped_convidados_3.title()}, espero que você entenda.')
popped_convidados_4 = convidados.pop()
print(f'Bah, desculpa, mas infelizmente vai faltar lugar {popped_convidados_4.title()}, espero que você entenda.')
popped_convidados_5 = convidados.pop()
print(f'Bah, desculpa, mas infelizmente vai faltar lugar {popped_convidados_5.title()}, espero que você entenda.')

print(convidados)
print(f'Pow, tu vai vir né {convidados[0].title()}?')
print(f'Pow, tu vai vir né {convidados[-1].title()}?')

del convidados[0]
del convidados[0]
print(convidados)