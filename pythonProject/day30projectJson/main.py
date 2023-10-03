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
    website = website_input.get()
    username = username_input.get()
    passwords = password_input.get()
    new_data = {
        website: {
            "email": username,
            "password": passwords,
        }
    }
    if len(website) == 0 or len(username) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="Oops", message="Please dont leave any field Empty!")
    else:
        try:
            with open("new_passwords.json", "r") as data_file:
                # reading old data
                my_data = json.load(data_file)
                # updating old data
                my_data.update(new_data)
        except FileNotFoundError:
            with open("new_passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("new_passwords.json", "w") as data_file:
                # saving new data
                json.dump(my_data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            website_input.focus()
            username_input.delete(0, END)
            username_input.insert(0, "diyohshiloh2@gmail.com")
            password_input.delete(0, END)


# ____________________________ FIND PASSWORD ____________________________#
def find_password():
    website = website_input.get()
    if len(website) == 0:
        messagebox.showinfo(title="Oops", message="Please provide a website to search its information!")
    else:
        try:
            with open("new_passwords.json", "r") as data_file:
                # reading old data
                my_data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No such file exists!")
        else:
            if website in my_data:
                website_info = data_file[website]["password"]
                email_info = data_file[website]["email"]
                messagebox.showinfo(title=f"{website} information",
                                    message=f"Website = {website} \n Email = {email_info} \n password = {website_info}")

            else:
                messagebox.showinfo(title="Oops", message="No details for the website exists")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_input = Entry(width=21)
website_input.grid(row=1, column=1)
website_input.focus()
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, "diyohshiloh2@gmail.com")
password_input = Entry(width=21)
password_input.grid(row=3, column=1)

# Buttons
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
