import customtkinter as ctk

janela = ctk.CTk()  # criando a janela principal
janela._set_appearance_mode("light")  # configurar o tema para claro, escuro ou padrão do sistema
janela.geometry("700x400")  # configurando as dimensões da janela
janela.title("Custom Tkinter")  # configurando o titulo da janela

frame_1 = ctk.CTkFrame(master=janela, width=200, height=330, fg_color="teal", corner_radius=20, bg_color="red", border_width=2, border_color="black").place(x=10, y=60)
#frame cria um bloco, corner_radiu = arredonda as bordas, border_color = define a cor da borda, border_width = largura da borda

frame_2 = ctk.CTkFrame(master=janela, width=200, height=330).place(x=230, y=60)

frame_3 = ctk.CTkFrame(master=janela, width=200, height=330).place(x=450, y=60)

janela.mainloop()  # rodando a janela
