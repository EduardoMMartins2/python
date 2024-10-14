import customtkinter

def button_callback():
    print("button pressed")

app = customtkinter.CTk()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #título da tela
        self.title("Primeiro CustomTkinter")
        #tamanho da tela
        self.geometry("400x150")
        #estilo do botao
        self.button = customtkinter.CTkButton(self, text="my button", command=button_callback)


        # o padx e pady é a posição na tela em coordenada xy
        # o grid divide uma janela em colunas e linhas
        #button.grid(row=0, column=0, padx=20, pady=20)


        #para centralizar o botão, dou o peso diferente de 0
        self.grid_columnconfigure((0, 1), weight=1)


        #abrande todo espaço pq o peso está na linha
        self.button.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)


        # caixas de seleção
        self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0,20), sticky="w")
        self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0,20), sticky="w")
    
    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()