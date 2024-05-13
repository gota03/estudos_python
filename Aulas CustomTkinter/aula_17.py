from customtkinter import *

janela = CTk()
set_appearance_mode("dark")
janela.geometry("700x400")
janela.title("Sistema de Login")

label = CTkLabel(janela, text="Faça o login", font=("Arial bold", 30))
label.pack()

username = CTkEntry(janela, placeholder_text="Username...", width=250)
username.pack(pady=20)

password = CTkEntry(janela, placeholder_text="Password...", width=250, show="*")
password.pack()

button = CTkButton(janela, text="Login".upper(), width=250)
button.pack(pady=30)

janela.mainloop()
