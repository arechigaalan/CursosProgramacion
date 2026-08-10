from tkinter import *

window = Tk()
window.title('Mile to Km Converter')
window.minsize(400, 250)
window.config(padx=20, pady=20)

label1 = Label(text='is equal to', font=('Arial', 20, 'bold'))
label1.config(padx=10, pady=10)
label1.grid(column=0, row=1)

label2 = Label(text='Miles', font=('Arial', 20, 'bold'))
label2.config(padx=10, pady=10)
label2.grid(column=2, row=0)

result = Label(text=0, font=('Arial', 20, 'bold'))
result.config(padx=10, pady=10)
result.grid(column=1, row=1)

label3 = Label(text='Km', font=('Arial', 20, 'bold'))
label3.config(padx=10, pady=10)
label3.grid(column=2, row=1)

input = Entry(width=10)
input.grid(column=1, row=0)

def conver_mile_km():
    convertion = 1.609344
    miles_to_convert = float(input.get())
    km = miles_to_convert * convertion
    result.config(text=round(km, 2))

button = Button(text='Calculate', command=conver_mile_km)
button.grid(column=1, row=2)



window.mainloop()
