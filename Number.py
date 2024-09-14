import tkinter as tk
from tkinter import *
import random
import os
#from PIL import Image, ImageTk

win = tk.Tk()
win.configure(bg="#065569")
win.geometry("650x550")
win.title("Number Guessing Game")

# Variables
result = StringVar()
chances = IntVar()
displaych1 = IntVar()
displaych2 = IntVar()
displaych3 = IntVar()
choice = IntVar()

# Congratulation Method


def congrat():
    msg = Label(win, text=str(choice.get()),
                font=("Courier", 25), relief=GROOVE)
    msg.place(relx=0.5, rely=0.3, anchor=CENTER)

    result.set("Congratulation YOU WON!!!")


# Second Page Method
def Page2():
    no = random.randint(1, 1000)
    result.set("Guess a number between 1 to 1000 ")
    chances.set(5)

    StartBtn.destroy()
    stopBtn.destroy()
    Intro.destroy()
    Intro1.destroy()
    Intro2.destroy()

# Between Display
    displaych1.set(no - 7),  displaych3.set(no + 7)

    # Main Method
    def main():

        if chances.get() != 0:
            if choice.get() > 1000 or choice.get() < 0:
                result.set("You have to Guess Between 1 to 1000")
                chances.set(chances.get()-1)
                chances.get()

            elif no == choice.get():
                choiceinput.destroy()
                GuessBtn.destroy()
                ChanceDisplay.destroy()
                ch1.destroy()
                ch2.destroy()
                ch3.destroy()
                DisplayRemains.destroy()
                congrat()

            elif no > choice.get():
                result.set("Your guess was too low: Guess a number higher ")
                chances.set(chances.get()-1)

            elif no < choice.get():
                result.set(
                    "Your guess was too High: Guess a number Lower ")
                chances.set(chances.get()-1)
        else:
            result.set("Game Over You Lost")

    # Second Page Button and input Entries

    choiceinput = Entry(win, textvariable=choice, width=3,
                        font=('Ubuntu', 30), relief=GROOVE)
    choiceinput.place(relx=0.5, rely=0.3, anchor=CENTER)

    ch1 = Entry(win, textvariable=displaych1, width=3,
                font=('Ubuntu', 20), relief=GROOVE)
    ch1.place(relx=0.2, rely=0.5, anchor=CENTER)

    ch2 = Label(win, text='Guess Between ',
                font=("Arial", 12, "normal", "italic"), fg="White", bg="#065569",)
    ch2.place(relx=0.5, rely=0.5, anchor=CENTER)

    ch3 = Entry(win, textvariable=displaych3, width=3,
                font=('Ubuntu', 20), relief=GROOVE)
    ch3.place(relx=0.8, rely=0.5, anchor=CENTER)

    StatusDisplay = Entry(win, textvariable=result, width=45,
                          font=('Courier', 15), relief=GROOVE)
    StatusDisplay.place(relx=0.5, rely=0.7, anchor=CENTER)

    ChanceDisplay = Entry(win, text=chances, width=2,
                          font=('Ubuntu', 20), relief=GROOVE)
    ChanceDisplay.place(relx=0.50, rely=0.85, anchor=CENTER)

    Header = Label(win, text='Guess a number between 1 to 1000 ',
                   font=("Arial", 20), fg="#fffcbd", bg="#065569")
    Header.place(relx=0.5, rely=0.09, anchor=CENTER)

    DisplayRemains = Label(win, text='Remaninig Chances :',
                           font=("Arial", 15, "normal", "italic"), fg="White", bg="#065569",)
    DisplayRemains.place(relx=0.3, rely=0.85, anchor=CENTER)

    GuessBtn = Button(win, width=8, command=main, text='Guess', font=(
        "Arial", 13), fg="#13d675", bg="Black")
    GuessBtn.place(relx=0.5, rely=0.6, anchor=CENTER)

    ExitBtn = tk.Button(win, text='Exit', width=20, command=win.destroy,
                        font=("Arial", 10), fg="White", bg="#b82741")
    ExitBtn.place(relx=0.25, rely=1, anchor=S)

    RestartBtn = tk.Button(win, text='Restart', width=20, command=Page2,
                           font=("Arial", 10, "bold"), fg="Black", bg="#29c70a")
    RestartBtn.place(relx=0.75, rely=1, anchor=S)


# First Page Texts and Button
Intro = Label(win, text='Welcome IN',
              font=("Arial", 20), fg="#fffcbd", bg="#065569")
Intro.place(relx=0.5, rely=0.09, anchor=CENTER)

Intro1 = Label(win, text='Number Guessing Game Between 1 To 1000',
               font=("Arial", 17), fg="#fffcbd", bg="#065569")
Intro1.place(relx=0.5, rely=0.29, anchor=CENTER)

Intro2 = Label(win, text='Click Start Button To Start',
               font=("Arial", 24), fg="#fffcbd", bg="#065569")
Intro2.place(relx=0.5, rely=0.49, anchor=CENTER)


stopBtn = tk.Button(win, text='Exit', width=20, command=win.destroy,
                    font=("Arial", 10), fg="White", bg="#b82741")
stopBtn.place(relx=0.25, rely=0.80, anchor=S)

StartBtn = tk.Button(win, text='Start', width=20, command=Page2,
                     font=("Arial", 10, "bold"), fg="Black", bg="#29c70a")
StartBtn.place(relx=0.75, rely=0.80, anchor=S)


win.mainloop()
