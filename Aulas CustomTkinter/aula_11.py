import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.geometry("700x400")

def enviar(value):
    print("Valor: ", value)

segmento = ctk.CTkSegmentedButton(janela,
                                  command=enviar,
                                  values=["tkinter", "django", "flask"],
                                  fg_color="teal",
                                  selected_color="red",
                                  selected_hover_color="green",
                                  border_width=5,
                                  width=10,
                                  corner_radius=30,
                                  unselected_color="blue",
                                  unselected_hover_color="yellow")
segmento.pack(pady=20)
segmento.set("tkinter")


janela.mainloop()
