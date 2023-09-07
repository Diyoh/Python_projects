from tkinter import *


def add(*args):
    for n in args:
        print(n)


window = Tk()
window.title("MILE TO KILOMETER CONVERTER")
window.minsize(width=500, height=300)
window.config(padx= 100, pady=200)
#Entry


input = Entry(width=10)
input.pack()
print(input.get())


# button
def button_click():
    print(" i got clicked")
    int new_text = input.get()
    KM = new_text/1.609344
    my_label.config(text=KM)

my_label = Label(text="i am a label which has been type", font=("Arial", 24, "bold"))
my_label.pack()

my_label["text"] = "Shiloh na big boy"
my_label.config(text="Shiloh na biger boy at this level sha")


button = Button(text="Calculate", command=button_click)
button.pack()
window.mainloop()
