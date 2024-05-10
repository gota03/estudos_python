import customtkinter as ctk

janela = ctk.CTk()
# ctk.set_appearance_mode("dark")
janela.geometry("700x400")

switch_var = ctk.StringVar(value="Ativado") # por padrão vai começar Ativado/tema branco


def alternar():
    if switch_var.get() == "Ativado":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")
    print("Estado: ", switch_var.get())


switch = ctk.CTkSwitch(janela,
                       variable=switch_var, # variavel por alterar o valor do tema
                       command=alternar,
                       onvalue="Ativado", # valor responsável por dizer se o switch está ativado
                       offvalue="Desativado") # valor responsável por dizer se o switch está desativado
switch.pack(pady=30)

janela.mainloop()
