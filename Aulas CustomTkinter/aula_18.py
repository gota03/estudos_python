from customtkinter import *

janela = CTk()
set_appearance_mode("dark")
janela.geometry("700x400")
janela.grid_columnconfigure((0, 1), weight=1)

btn = CTkButton(janela, text="Botão")
btn.grid(row=0, column=0, pady=20, padx=20, sticky='ew', columnspan=2)

check = CTkCheckBox(janela, text="Checkbox")
check.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='effw')

check_2 = CTkCheckBox(janela, text="Checkbox 2")
check_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='w')

janela.mainloop()
