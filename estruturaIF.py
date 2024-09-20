insereNome = str( input("Digite o Nome: ") )
nome = insereNome

if nome == "Eduardo":
    print("Acertou o nome!")
else:
    print("Erroooooou")



#if e else
insereVariavel = int( input("Digite a variável inteira: ") )
x = insereVariavel
resto = x % 2

if resto == 0:
    print("O número é par!")
else:
    print("O número é impar!")



#testar a nota com if elif e else - int, float, str
varNota = int(input("Digite a Nota: "))
nota = varNota

if nota >= 9:
    print("Tirou SS!")
elif nota >= 7:
    print("Tirou MS!")
elif nota >= 5:
    print("Tirou MM!")
else:
    print("Tirou MI, se lascou!")