from tkinter import *
from tkinter import ttk

#atribui as funções
# root = inicia o Tk cria uma janela de nível superior, janela raiz, janela principal da applicação
root = Tk()
# frm = o frame se encaixa dentro da janela raiz
frm = ttk.Frame(root, padding=10)


#chama o widget
frm.grid()

#chama o róutlo - cria um widget contendo a string, o grid() especifica o layout relativo (posição) dentro do frame
ttk.Label(frm, text= " Hello World!").grid(column=0, row=0)

#chama o tipo de botão - cria o botão, quando chamado usa o método destroy() - destroy coloca tudo no display
ttk.Button(frm, text= "Quit", command=root.destroy).grid(column=1, row=0)

#como deve executar
root.mainloop()