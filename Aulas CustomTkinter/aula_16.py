import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.geometry("700x400")

btn_1 = ctk.CTkButton(janela, text="btn 1")
btn_1.place(x=40, y=20)

btn_2 = ctk.CTkButton(janela, text="btn 2")
btn_2.place(relx=0.1, rely=0.2) # posiciona os elementos atraves do calculo da porcentagem em relação a largura e altura da tela


janela.mainloop()
