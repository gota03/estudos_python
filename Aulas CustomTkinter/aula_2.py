import customtkinter as ctk

janela = ctk.CTk()  # criando a janela principal
janela._set_appearance_mode("dark")  # configurar o tema para claro, escuro ou padrão do sistema
janela.geometry("700x400")  # configurando as dimensões da janela
janela.title("Custom Tkinter")  # configurando o titulo da janela

def nova_janela():
    nova_janela = ctk.CTkToplevel(janela, fg_color="teal") # fg_color define a cor de fundo da janela
    nova_janela.geometry("400x400")
    nova_janela.title("Nova janela")

btn_nova_janela = ctk.CTkButton(master=janela, text="Nova janela", command=nova_janela).place(x = 300, y = 100) # cria um botão que leva para uma janela, master = tela a ser criado o botão, text = texto no botão, command = comando a ser executado pelo botão

janela.mainloop()  # rodando a janela
