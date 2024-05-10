import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.geometry("700x400")

def value_slider(value):
    print(value)

slider = ctk.CTkSlider(janela,
                       from_=0,
                       to=100,
                       command=value_slider,
                       button_color="white",
                       button_hover_color= "white",
                       progress_color="blue")
slider.pack(pady = 30)

janela.mainloop()