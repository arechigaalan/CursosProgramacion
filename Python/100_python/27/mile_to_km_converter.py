from tkinter import *
FONT = ('Arial', 12)
window = Tk()
window.minsize(width=400, height=200)
window.title('Mile to Km Converter')
window.config(padx=50, pady=50)

label_equal = Label(text='is equal to', font=FONT)
label_equal.grid(column=0, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

label_miles = Label(text='Miles', font=FONT)
label_miles.grid(column=2, row=0)

result = Label(text=0, font=FONT)
result.grid(column=1, row=1)

result = Label(text='Km', font=FONT)
result.grid(column=2, row=1)

def calculate(miles):
    

button = Button(text='Calculate', )

window.mainloop()
