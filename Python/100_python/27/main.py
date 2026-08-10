from tkinter import *

window = Tk()
window.title('My first GUI Program')
window.minsize(width=500, height=300)
window.config(padx=10, pady=10) #! Añadir padding a los márgenes de la ventana..

#! Label
my_label = Label(text='I Am a Label', font=('Arial', 24, 'bold'))
my_label['text'] = 'New Text'
my_label.config(text='Final text')
my_label.grid(column=0, row=0)

#! Button
def button_clicked():
    my_label.config(text=input.get())

button = Button(text='Click me', command=button_clicked)
button.config(padx=10, pady=10)
button.grid(column=1, row=1)

button2 = Button(text='Click me 2', command=button_clicked)
button2.grid(column=2, row=0)

#! Entry
input = Entry(width=10)
input.grid(column=3, row=2)

#! TextBox
text = Text(height=5, width=30)
text.focus()
text.insert(END, 'Example of multi-line text entry.') #! El END siempre debe ir, no cambiar
print(text.get('1.0', END))
# text.pack()

#! Spinbox
def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

#! Scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()

#! Checkbutton
def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
# checkbutton.pack()

#! Radiobutton
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text='Option 1', value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text='Option 2', value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()

#! listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ['Apple', 'Pear', 'Orange', 'Banana']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind('<<ListboxSelect>>', listbox_used)
# listbox.pack()

window.mainloop() #! Mantiene la ventana abierta. Siempre va al final.
