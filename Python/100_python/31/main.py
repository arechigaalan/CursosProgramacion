
from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

#! Data 
data = pd.read_csv('./data/french_words.csv')
french_words = data.French.to_list()
english_word = data.English.to_list()

data2 = pd.read_csv('./data/palabras_aprendidas.csv')
know_words = data2.French.to_list()

known_words = [_ for _ in french_words if _ not in know_words]

#! Choise a random french word
def change_word():
    global flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(known_words)
    canvas.itemconfig(word_text, text=word, fill='black')
    canvas.itemconfig(title_text, fill='black', text='French')
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, show_translation)

def translation(word):
    index = known_words.index(word)
    return(english_word[index])

def show_translation():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(title_text, fill='white', text='English')
    word = canvas.itemcget(word_text, 'text')
    canvas.itemconfig(word_text, fill='white', text=translation(word))

def agregar_palabras_aprendidas():
    word = canvas.itemcget(word_text, 'text')
    index = english_word.index(word)
    french_word = known_words[index]
    with open(file='./data/palabras_aprendidas.csv', mode='a') as pa:
        pa.write(f'{french_word},{word}\n')

def agrupar_funciones():
    agregar_palabras_aprendidas()
    change_word()

#! Interfaz
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50)
window.config(background=BACKGROUND_COLOR)

flip_timer = window.after(3000, show_translation)

front_img = PhotoImage(file='./images/card_front.png')
back_img = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=800, height=526, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.config(background=BACKGROUND_COLOR)
canvas.grid(column=1, row=1, columnspan=2)

title_text = canvas.create_text(400, 150, text='French', fill='black', font=('Arial', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', fill='black', font=('Arial', 46, 'bold'))

wrong_image = PhotoImage(file='./images/wrong.png')
button_right = Button(image=wrong_image, highlightthickness=0, command=change_word)
button_right.grid(column=1, row=2)

right_image = PhotoImage(file='./images/right.png')
button_right = Button(image=right_image, highlightthickness=0, command=agrupar_funciones)
button_right.grid(column=2, row=2)

change_word()

window.mainloop()
