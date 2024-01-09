
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(width=100, height=100, bg= YELLOW)

canvas = Canvas(width=200, height = 200)
tomato_img = PhotoImage("./D28_tkinter_Pomodoro/tomato.png")
canvas.create_image(100, 112, image = tomato_img)
canvas.create_text(100, 130, text="00:00", fill = "white", font=("Courier",40, "bold"))
canvas.pack()





window.mainloop()