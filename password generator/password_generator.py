from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

############## PSW GEN ###############
def generate_password():
    letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g',
        'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 
        'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X',
        'C', 'V', 'B', 'N', 'M']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '£', '$', '%', '&', '/', '(', ')', '=', '?', '^', '*', '#', '@', '-', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_number
    shuffle(password_list)

    password = "".join(password_list)
    psw_entry.insert(0, password)
    pyperclip.copy(password)

############## SAVE PSW ###############

def save():
    website = website_entry.get()
    email = user_entry.get()
    password = psw_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oppps", message="Please compile all field?")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:   
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
        
            with open("data.json", "w") as data_file:   
                json.dump(data, data_file, indent=4)
        finally:    
            website_entry.delete(0, END)
            psw_entry.delete(0, END)

############## FIND PASSWORD  ###############

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


############## GUI ###############
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="WebSite:")
website_label.grid(column=0, row= 1)

website_entry = Entry(width=21)
website_entry.grid(column=1, row= 1)
website_entry.focus()

search_button = Button(text="Search", width=15, command=find_password)
search_button.grid(column=2, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row= 2)

user_entry = Entry(width=40)
user_entry.grid(column=1, row= 2, columnspan=2)
user_entry.insert(0, "nome@sito.com")

psw_label = Label(text="Password:")
psw_label.grid(column=0, row= 3)

psw_entry = Entry(width=21)
psw_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row= 3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row= 4, columnspan=2)



window.mainloop()