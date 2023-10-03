import tkinter
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_input.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get().title()
    username = username_input.get()
    passwords = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": passwords,
        }
    }
    if len(website) == 0 or len(username) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any field Em[ty!")
    else:
        try:
            with open("my_passwords.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("my_passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("my_passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            website_input.focus()
            username_input.delete(0, END)
            username_input.insert(0, "diyohshiloh2@gmail.com")
            password_input.delete(0, END)


# _________________________  SEARCH PASSWORD ____________________________#
def search_password():
    website = website_input.get().title()
    username = username_input.get()
    try:
        with open("my_passwords.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='ERROR', message="No data found")
    else:
        if len(website) == 0:
            messagebox.showinfo(title="Oops", message="Please provide a website to search!")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"email: {email} \npassword: {password}")
            else:
                messagebox.showinfo(title='OOPS', message=f'no details for {website} exist')


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Diyoh Shiloh Password manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="../day30projectJson/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1, )
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_input = Entry(width=5)
website_input.grid(column=1, row=1, columnspan=1, sticky="ew")
website_input.focus()
username_input = Entry(width=40)
username_input.grid(column=1, row=2, columnspan=2, sticky="ew")
username_input.insert(0, "diyohshiloh2@gmail.com")
password_input = Entry(width=21)
password_input.grid(column=1, row=3, sticky="ew")

Search_button = Button(text="Search", command=search_password, highlightthickness=0)
Search_button.grid(column=2, row=1, sticky="ew")
Add_button = Button(width=36, text="Add", command=save_password, highlightthickness=0)
Add_button.grid(column=1, row=4, columnspan=2, sticky="ew")
Generate_button = Button(text="Generate Password", command=generate_password, highlightthickness=0)
Generate_button.grid(column=2, row=3, sticky="ew")
window.mainloop()
