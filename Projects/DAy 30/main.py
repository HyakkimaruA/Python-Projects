from tkinter import *
from tkinter import messagebox
import random
import json

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


# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search():
    website = website_insert.get()
    try:
        with open("data.json", "r") as read_file:
            data = json.load(read_file)
            messagebox.showinfo("Data of Website", f"Email: {data[website]['email']}\n\nPassword: {data[website]['password']}")
    except KeyError:
        messagebox.showerror("ERROR", "This website does not exist.")
    except FileNotFoundError:
        messagebox.showerror("ERROR", "This website does not exist.")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_insert.get()
    email = email_insert.get()
    password = password_insert.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as file_save:
                # Reading old data
                data = json.load(file_save)
        except FileNotFoundError:
            with open("data.json", "w") as file_save:
                json.dump(new_data, file_save, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file_save:
                # Saving updated data
                json.dump(data, file_save, indent=4)

        finally:
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

website_insert = Entry(width=21)
website_insert.grid(column=1, row=1)
website_insert.focus()

email_text = Label(text="Email/Username:", bg="white", pady=5)
email_text.grid(column=0, row=2)

email_insert = Entry(width=42)
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

search_button = Button(text="Search", bg="white", highlightthickness=0, command=search)
search_button.grid(column=2, row=1, columnspan=2)

window.mainloop()
