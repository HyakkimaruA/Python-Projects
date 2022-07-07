from tkinter import *
from tkinter import messagebox
import random

PASSWORD_GEN_COUNT = 0


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global PASSWORD_GEN_COUNT
    if PASSWORD_GEN_COUNT == 1:
        password_insert.delete(0, END)
        PASSWORD_GEN_COUNT = 0
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = [*password_letters, *password_symbols, *password_numbers]

    random.shuffle(password_list)

    pass_gen = "".join(password_list)
    password_insert.insert(0, pass_gen)
    PASSWORD_GEN_COUNT += 1

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_insert.get()
    email = email_insert.get()
    password = password_insert.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n\nEmail: {email} \n"
                                                              f"Password: {password} \n\nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file_save:
                file_save.write(f"{website} |")
                file_save.write(f" {email} |")
                file_save.write(f" {password}\n")
                website_insert.delete(0, END)
                password_insert.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg="white")
window.title("Password Manager")

photo_mypass = PhotoImage(file="logo.png")
canvas = Canvas(bg="white", highlightthickness=0, height=200, width=200)
canvas.create_image(100, 100, image=photo_mypass)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:", bg="white", pady=5)
website_text.grid(column=0, row=1)

website_insert = Entry(width=35)
website_insert.grid(column=1, row=1, columnspan=2)
website_insert.focus()

email_text = Label(text="Email/Username:", bg="white", pady=5)
email_text.grid(column=0, row=2)

email_insert = Entry(width=35)
email_insert.grid(column=1, row=2, columnspan=2)
email_insert.insert(INSERT, "example@outlook.com")

password_text = Label(text="Password:", bg="white", pady=5)
password_text.grid(column=0, row=3)

password_insert = Entry(width=21)
password_insert.grid(column=1, row=3)

password_generator = Button(text="Generate Password", bg="white", highlightthickness=0, command=generate_password)
password_generator.grid(column=2, row=3)

add_button = Button(text="Add", width=36, bg="white", highlightthickness=0, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
