import customtkinter as ctk

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
janela.geometry("700x400")

progressbar = ctk.CTkProgressBar(janela, corner_radius=100, border_width=2, height=8, progress_color="green", fg_color="white")
progressbar.pack(pady=20)

progressbar.start()
for i in range(1, 11):
    progressbar.step()

progressbar.stop()

janela.mainloop()
