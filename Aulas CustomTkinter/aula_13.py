import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.geometry("700x400")

check_var = ctk.StringVar(value="on")

def marca_checkbox():
    valor_atual = check_var.get()
    print("Valor atual do checkbox: ", valor_atual)


checkbox = ctk.CTkCheckBox(janela, text="Checkbox", variable=check_var, onvalue="on", offvalue="off", command=marca_checkbox)
checkbox.pack(pady=10)

janela.mainloop()
