from tkinter import *


def converting_miles():
    text_amount_of_km = Label(text=round(int(amount_miles.get()) * 1.60394, 1))
    text_amount_of_km.grid(column=1, row=1)


window = Tk()
window.minsize(width=300, height=100)
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)

amount_miles = Entry()
amount_miles.grid(column=1, row=0)
amount_miles.config(width=10)

text_miles = Label(text="Miles")
text_miles.grid(column=2, row=0)

text_equal = Label(text="is equal to")
text_equal.grid(column=0, row=1)

text_amount_of_km = Label(text=0)
text_amount_of_km.grid(column=1, row=1)

text_km = Label(text="Km")
text_km.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=converting_miles)
calculate_button.grid(column=1, row=2)
window.mainloop()
