import math
import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Livvic"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
time = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(time)
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text='Timer')
    check.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        counter(long_break_sec)
        timer.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        counter(short_break_sec)
        timer.config(text='Break', fg=PINK)
    else:
        counter(work_sec)
        timer.config(text='Work', fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def counter(count):
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_sec < 10:
        count_sec = f'0{count_sec}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global time
        time = window.after(1000, counter, count - 1)
    else:
        start_timer()
        mark = ''
        for _ in range(math.floor(reps / 2)):
            mark += '🗸'
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


timer = tk.Label(text="Timer", font=(
    FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(row=0, column=1)

canvas = tk.Canvas(width=202, height=224, highlightthickness=0, bg=YELLOW)
img = tk.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(102, 130, text='00:00', font=(
    FONT_NAME, 30, 'bold'), fill='Whitesmoke')
canvas.grid(row=1, column=1)

start_btn = tk.Button(text="Start", bd=0, padx=12,
                      font=(FONT_NAME), command=start_timer)
start_btn.grid(row=2, column=0)

reset_btn = tk.Button(text="Reset", bd=0, padx=12, font=(FONT_NAME), command=reset_timer)
reset_btn.grid(row=2, column=2)

check = tk.Label(text='', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 14))
check.grid(row=2, column=1)

window.mainloop()
