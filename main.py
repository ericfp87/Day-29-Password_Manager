from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0 or len(email) == 0:
        messagebox.showerror(title="Erro", message="Nenhum campo pode ficar em branco")
    else:
        it_is_ok = messagebox.askokcancel(title=website, message=f"Estas são as informações: \nEmail: {email} \nSenha: {password} \nConfirma as informações?")

        if it_is_ok:

            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                email_input.delete(0, END)
                password_input.delete(0, END)

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
website_input.focus()


email_input = Entry(width=35, font=("Arial", 18))
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21, font=("Arial", 18))
password_input.grid(column=1, row=3)

#Button
password_button = Button(text="Gerar Senha", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Adicionar", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)



window.mainloop()
