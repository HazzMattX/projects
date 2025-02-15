import json
from tkinter import *
from tkinter import messagebox
from  random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = id_entry.get()
    password = password_entry.get()
    manage_login = {
        website: {
            "email": email,
            "password": password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Emergency!", message="There's some missing information")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Email: {email}"
                                                              f"\nPassword: {password}"
                                                              f"\nSave this information?")
        if is_ok:
            try:
                with open("login_information.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("login_information.json", "w") as data_file:
                    json.dump(manage_login, data_file, indent=4)
            else:
                data.update(manage_login)
                with open("login_information.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------------ #
def search_json():
    website = website_entry.get()
    try:
       with open("login_information.json") as data_file:
           data = json.load(data_file)
    except FileNotFoundError:
       messagebox.showinfo(title="Error", message="Doesn't exist")
    else:
       if website in data:
           email = data[website]["email"]
           password = data[website]["password"]
           messagebox.showinfo(title=website, message=f"Email: {email} "
                                                      f"\n{password}")
       else:
           messagebox.showinfo(title="Error", message="It's not here")

# ---------------------------- UI SETUP ------------------------------------ #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=38)
website_entry.grid(column=1, columnspan=2, row=1)
website_entry.focus()
id_label = Label(text="Email/Username:")
id_label.grid(column=0, row=2)
id_entry = Entry(width=38)
id_entry.grid(column=1, columnspan=2, row=2)
id_entry.insert(0, "dowdmatt93@gmail.com")
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)
add_password = Button(text="Add", width=36, command=save_password)
add_password.grid(column=1, columnspan=2, row=4)
search_button = Button(text="Search", width=12, command=search_json)
search_button.grid(column=2, row=1)


window.mainloop()