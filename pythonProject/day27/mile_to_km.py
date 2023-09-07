from tkinter import *


def convert():
    miles = box_input.get()
    int_miles = int(miles)
    killometers = int_miles * 1.609344
    r_km = round(killometers, 2)
    my_KM.config(text=r_km)


window = Tk()
window.title("MILE TO KILOMETER CONVERTER")
window.minsize(width=400, height=200)
window.config(padx=50, pady=50)

my_miles = Label(text="")
my_miles.config(padx=5, pady=5)
my_miles.grid(column=1, row=1)

box_input = Entry(width=20)
box_input.insert(END, string="0")
box_input.grid(column=3, row=1)

my_miles = Label(text="Miles")
my_miles.config(padx=5, pady=5)
my_miles.grid(column=4, row=1)

m_text = Label(text="is equal to")
m_text.grid(column=2, row=2)

my_KM = Label(text="0")
my_KM.config(padx=5, pady=5)
my_KM.grid(column=3, row=2)

my_end = Label(text="Km")
my_end.config(padx=5, pady=5)
my_end.grid(column=4, row=2)

button = Button(text="Calculate", command=convert)
button.grid(column=3, row=3)
window.mainloop()
