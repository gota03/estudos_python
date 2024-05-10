import customtkinter as ctk

janela = ctk.CTk()  # criando a janela principal
janela._set_appearance_mode("light")  # configurar o tema para claro, escuro ou padrão do sistema
janela.geometry("700x400")  # configurando as dimensões da janela
janela.title("Custom Tkinter")  # configurando o titulo da janela

textbox = ctk.CTkTextbox(janela, width=400, height=300, scrollbar_button_color="red", fg_color="black", text_color="white") # criando caixa de texto

textbox.insert("0.0", text="Ola, sou mateus\n"*20) # inserindo texto na caixa de texto
textbox.pack()

janela.mainloop()
