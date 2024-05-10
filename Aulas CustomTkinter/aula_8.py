import customtkinter as ctk

janela = ctk.CTk()
janela.geometry("700x400")

# def escolher_tema(escolha):
#     tema = escolha
#     ctk.set_appearance_mode(tema)
#
# ctk.CTkOptionMenu(janela, values=["light", "dark", "system"], command=escolher_tema).pack()

ctk.CTkLabel(janela,
             text="Digite seu nome completo").pack()

#text_var = ctk.StringVar(value=input("Digite seu nome: "))

label = ctk.CTkLabel(janela,
                     textvariable = "",
                     text="",
                     width=200,
                     height=30,
                     text_color="red",
                     font=("arial bold", 20))

entry = ctk.CTkEntry(janela, width=200, placeholder_text="digite seu nome",
                     border_color="white")  # cria uma caixa de entrada de input
entry.pack()


def enviar():
    nome = entry.get() #pega o valor digitado na caixa de entrada
    print(entry.get()) # pega o valor digitado na caixa de entrada e exibe no terminal
    label.configure(text=str(nome)) # exibe o valor passado na caixa de entrada no label
    pass


ctk.CTkButton(janela,
              command=enviar, # executa a função enviar
              text="Enviar").pack(pady=10)

label.pack(pady=20)

janela.mainloop()
