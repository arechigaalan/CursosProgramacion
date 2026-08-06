from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip 

FONT = ('Arial', 14, 'normal')
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
              'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R',
              'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ]
NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
SYMBOLS = ['#', '$', '%', '&', '/', '(', ')', '!', '¡', '¿', '?', '+', '*']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    pass_list = []
    pass_list += [choice(LETTERS) for letter in range(nr_letters)]
    pass_list += [choice(SYMBOLS) for symbol in range(nr_symbols)]
    pass_list += [choice(NUMBERS) for number in range(nr_numbers)]

    shuffle(pass_list)

    password_generated = ''.join(pass_list)
    input_password.insert(0, password_generated)

    pyperclip.copy(password_generated)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    if check_data(website, username, password):
        is_ok = messagebox.askokcancel(title='website', message=f'These are the details entered: \nUsername: {username} '
                                    f'\nPassword: {password} \nIs it ok to save?')
        if is_ok:
            data = f'{website} | {username} | {password}\n'
            with open('data.txt', mode='a') as data_txt:
                data_txt.write(data)
            clear_data()
    else:
        messagebox.showerror(title='Oops', message='Please don\'t leave any fields empty!')

def check_data(website, username, password):
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        return False
    return True

def clear_data():
    input_website.delete(first=0, last=END)
    input_password.delete(first=0, last=END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

padlock_img = PhotoImage(file='logo.png')
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=padlock_img)
canvas.grid(column=2, row=1)

label_website = Label(text='Website:', font=FONT)
label_website.grid(column=1, row=2)

input_website = Entry(width=51)
input_website.focus()
input_website.grid(column=2, row=2, columnspan=2)

label_username = Label(text='Email/Username:', font=FONT)
label_username.grid(column=1, row=3)

input_username = Entry(width=51)
input_username.insert(10, 'alan.arechiga')
input_username.grid(column=2, row=3, columnspan=2)

label_password = Label(text='Password', font=FONT)
label_password.grid(column=1, row=4)

input_password = Entry(width=33)
input_password.grid(column=2, row=4)

generate_pass_button = Button(text='Generate Password', border=0.4, command=generate_password)
generate_pass_button.grid(column=3, row=4)

add_button = Button(text='Add', width=43, command=save)
add_button.grid(column=2, row=5, columnspan=2)

window.mainloop()
