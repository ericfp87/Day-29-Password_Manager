from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()


window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
my_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=my_img)
canvas.grid(column=1, row=0)

#Label
website_label = Label(text="Website:", font=("Arial", 16, "bold"))
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Usuário:", font=("Arial", 16, "bold"))
email_label.grid(column=0, row=2)

password_label = Label(text="Senha:", font=("Arial", 16, "bold"))
password_label.grid(column=0, row=3)

#Entry
website_input = Entry(width=35, font=("Arial", 18))
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=35, font=("Arial", 18))
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21, font=("Arial", 18))
password_input.grid(column=1, row=3)

#Button
password_button = Button(text="Gerar Senha")
password_button.grid(column=2, row=3)

add_button = Button(text="Adicionar", width=36)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
