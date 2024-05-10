import customtkinter as ctk

janela = ctk.CTk()

ctk.set_appearance_mode("dark")
janela.geometry("700x400")
janela.title("Custom Tkinter")

(ctk.CTkLabel(janela,
             text="Menu de opções", # texto
             font=("arial bold", 20), # estilo do texto
             text_color="white") # cor do texto
            .pack(pady=20, padx=5)) # posicionando o texto

(ctk.CTkLabel(janela,
             text="Escolha um mes abaixo", # texto
             font=("arial bold", 20), # estilo do texto
             text_color="white") # cor do texto
            .pack(pady=10)) # posicionando o texto


def escolha_mes_nascimento(escolha): # vai capturar o valor escolhido no menu de opções
    print(f"Mês de nascimento: {escolha}")


mes_set_2 = ctk.StringVar(value="Escolha um mes")  # 2º forma de colocar placeholder no menu de opções

mes = ctk.CTkOptionMenu(janela,
                        values=["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"], # valores do menu
                        command=escolha_mes_nascimento, # função a ser executado quando clicado em algum valor do menu
                        variable=mes_set_2, # definindo o placeholder
                        width=250, # largura do menu
                        height=50, # altura do menu
                        corner_radius=50, # arredondamento das bordas
                        fg_color="red", # cor de fundo do botão
                        button_color="green", # cor da seta pra baixo do dropdown
                        button_hover_color="teal", # cor da seta pra baixo quando o mouse passar por cima
                        dropdown_font=("arial bold", 20), # font dos textos dos valores do menu
                        dropdown_fg_color="teal", # cor de fundo do menu dropdown
                        dropdown_text_color="purple", # cor dos textos dos valores do menu
                        dropdown_hover_color="white" # cor de fundo quando o mouse passa por cima
                        )

mes.pack()
#mes.set("Escolha um mes")  # define um placeholder no menu de opções

janela.mainloop()
