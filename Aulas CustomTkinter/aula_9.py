import customtkinter as ctk
from PIL import Image  # importar o IMAGE para trabalhar com imagens

janela = ctk.CTk()
ctk.set_appearance_mode("light")
janela.geometry("700x400")

img = ctk.CTkImage(light_image=Image.open("./assets/batman.jpg"),  # definindo imagem para o modo claro
                   dark_image=Image.open("./assets/batman.jpg"),  # definindo imagem para o modo escuro
                   size=(200, 200))  # definindo tamanho da imagem

img_2 = ctk.CTkImage(light_image=Image.open("./assets/superman.jpg"),  # definindo imagem para o modo claro
                     # dark_image=Image.open("./assets/superman.jpg"), # definindo imagem para o modo escuro
                     size=(25, 25))  #definindo tamanho da imagem

(ctk.CTkLabel(janela, text="",
              image=img) # passando imagem para o label
 .pack())

ctk.CTkButton(janela,
              image=img_2, # passando imagem para o botão
              text="Teste").pack()

janela.mainloop()
