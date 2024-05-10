import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.geometry("700x400")

radio_var = ctk.IntVar(value=3) # setando o valor inicial


def radio_event():
    print(radio_var.get()) # pegando o valor marcado


radio_1 = ctk.CTkRadioButton(janela, text="Masculino", value=0, command=radio_event, variable=radio_var)
radio_2 = ctk.CTkRadioButton(janela, text="Feminino", value=1, command=radio_event, variable=radio_var)

radio_1.pack(pady=20)
radio_2.pack()

janela.mainloop()
