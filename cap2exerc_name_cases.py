# 2.3
nome = "Eduardo"
sobrenome1 = "Moraes"
mensagem = f"Olá, {nome} {sobrenome1}, gostaria de aprender um pouco de python hoje?"
print(mensagem)

# 2.4
todo_nome = f"{nome} {sobrenome1}"
print(todo_nome.upper())
print(todo_nome.lower())
print(todo_nome.title())

# 2.5
frase = f'\n"Estou convencido de que metade do que separa empreendedores de sucesso dos não sucedidos é pura perseverança."        '
famous_person = f"\t Steve Jobs "
pensamento = f"{famous_person.strip()} disse uma vez: {frase.rstrip()}"
print(pensamento)



file_name = 'python_notes.txt'
print(file_name)
file_name = file_name.removesuffix('.txt')
print(file_name)