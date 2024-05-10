import customtkinter as ctk

janela = ctk.CTk()  # criando a janela principal
janela._set_appearance_mode("light")  # configurar o tema para claro, escuro ou padrão do sistema
janela.geometry("700x400")  # configurando as dimensões da janela
janela.title("Custom Tkinter")  # configurando o titulo da janela

tabview = ctk.CTkTabview(master=janela, width=400, border_width=2, border_color="black", fg_color="teal", segmented_button_fg_color="black", segmented_button_selected_color="red", segmented_button_selected_hover_color="red", segmented_button_unselected_color="blue", segmented_button_unselected_hover_color="blue") # criando abas de navegação

tabview.pack() # o pack posiciona o elemento centralizado
tabview.add("Nomes") # adicionando abas de navegação
tabview.add("Idade") # adicionando abas de navegação
tabview.add("Sexo") # adicionando abas de navegação

tabview.tab("Nomes").grid_columnconfigure(0, weight=1) # posicionando as abas de navegação
tabview.tab("Idade").grid_columnconfigure(0, weight=1) # posicionando as abas de navegação
tabview.tab("Sexo").grid_columnconfigure(0, weight=1) # posicionando as abas de navegação

text = ctk.CTkLabel(tabview.tab("Nomes"), text="Mateus\nLyandra\nRenato") # adicionando textos em cada aba
text.pack()

idade = ctk.CTkLabel(tabview.tab("Idade"), text="21\n21\n6") # adicionando textos em cada aba
idade.pack()

sexo = ctk.CTkLabel(tabview.tab("Sexo"), text="masculino\nfeminino\nmasculino") # adicionando textos em cada aba
sexo.pack()

janela.mainloop()
