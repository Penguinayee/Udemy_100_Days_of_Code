from tkinter import *

window = Tk()
window.title("Mile to Km converter")
#window.minsize(width=200, height=100)
window.config(padx = 20, pady = 20)

def button_clicked():
    miles = float(input.get())
    km = miles * 1.6
    km_result.config(text = f"{km}")


input = Entry(width = 10)
input.grid(column = 1, row = 0)

miles_label = Label(text='Miles', font=('Arial', 20))
miles_label.grid(column = 2, row = 0)

is_equal_to = Label(text='is equal to', font=('Arial', 20))
is_equal_to.grid(column = 0, row = 1)

km_result = Label(text='0', font=('Arial', 20))
km_result.grid(column = 1, row = 1)

km_label = Label(text='Km', font=('Arial', 20))
km_label.grid(column = 2, row = 1)


calculate_button = Button(text='Calculate', command = button_clicked)
calculate_button.grid(column = 1, row = 2)



window.mainloop()