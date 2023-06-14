from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    heading.config(text='Timer')
    canvas.itemconfig(timer_text, text='00:00')
    checkmark.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        heading.config(text='Work', fg=GREEN)
    elif reps % 8 == 0:
        count_down(long_break_sec)
        heading.config(text='Break', fg=RED)
    else:
        count_down(short_break_sec)
        heading.config(text='Short Break', fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps/2)):
            mark += '✔'
        checkmark.config(text=mark)
    # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(pady=50, padx=100, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=image)
timer_text = canvas.create_text(100,130,text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

heading = Label(text='Timer',fg=GREEN, bg=YELLOW, font=(FONT_NAME,35,'bold'))
heading.grid(column=1, row=0)

start = Button(text='Start', font=(FONT_NAME), bg='White', command=start_timer)
start.grid(column=0, row=2)

reset = Button(text='Reset', font=(FONT_NAME), bg='White', command=reset)
reset.grid(column=2, row=2)

checkmark = Label(font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()