import customtkinter as ctk

janela = ctk.CTk()  # criando a janela principal
janela._set_appearance_mode('dark')  # configurar o tema para claro ou escuro
janela.geometry("700x400") # configurando as dimensões da janela
janela.maxsize(width=900, height=600) # configurando o tamanho máximo da tela
janela.minsize(width=500, height=300) # configurando o tamanho mínimo da tela
janela.resizable(width=True, height=False) # configura o bloqueio da largura e altura da janela, True permite aumentar e False bloqueia
#janela.iconify() # abre e fecha a janela
#janela.deiconify() # reabre a janela
janela.title("Custom Tkinter") # configurando o titulo da janela

janela.mainloop()  # rodando a janela
