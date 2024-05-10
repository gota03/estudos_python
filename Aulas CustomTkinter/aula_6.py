import customtkinter as ctk

janela = ctk.CTk()  # criando a janela principal
ctk.set_appearance_mode("dark")  # configurar o tema para claro, escuro ou padrão do sistema
ctk.set_default_color_theme("blue")
janela.geometry("700x400")  # configurando as dimensões da janela
janela.title("Custom Tkinter")  # configurando o titulo da janela

def abrir_caixa_dialogo():
    dialogo = ctk.CTkInputDialog(title="Caixa de dialogo", entry_border_color="black")
    print(dialogo.get_input())

btn = ctk.CTkButton(janela, text="Abrir caixa de dialogo", command=abrir_caixa_dialogo)
btn.pack()

janela.mainloop()
