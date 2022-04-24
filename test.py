import os
from tkinter import *
from tkinter import Tk
import random
import stat
import time


    #main window


window_wall = Tk()
window_wall.geometry("726x700")
window_wall.title("snacks and ladders")
window_wall.resizable(False,False)
canvas_w = Canvas(window_wall,width=726,height=700)
canvas_w.pack()
snake = PhotoImage(file="wallmain.png")
snakew = canvas_w.create_image(355, 350, image=snake,)




#die options for the exterior window
window_die = Tk()
window_die.geometry("300x300")
window_die.focus()
window_die.resizable(False, False)
window_die.title("snacks and ladders")
window_die.config(bg="#e2e38f")

path = "gameT.txt"
with open("gameT.txt") as file:
    i = file.read()
if i == "1die" :
    frame_the_die = Frame(window_die, bg='BLACK', bd=5, relief="groove", width=110, height=115)
    frame_the_die1 = Frame(window_die, bg="black", bd=5, relief="groove", width=110, height=115)


    def player1():
        for widget in frame_the_die1.winfo_children():
            widget.forget()

        thedie = ["1", "2", "3", "4", "5", "6"]
        z = random.choice(thedie)
        print(z)

        if z == "1":
            c1 = Canvas(frame_the_die, width=106, height=99)
            c1.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
            c1.pack()
        elif z == "2":
            c2 = Canvas(frame_the_die, width=106, height=99)
            c2.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c2.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c2.pack()
        elif z == "3":
            c3 = Canvas(frame_the_die, width=106, height=99)
            c3.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c3.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
            c3.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c3.pack()

        elif z == "4":
            c4 = Canvas(frame_the_die, width=106, height=99)
            c4.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
            c4.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c4.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c4.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
            c4.pack()

        elif z == "5":
            c5 = Canvas(frame_the_die, width=106, height=99)
            c5.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
            c5.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
            c5.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c5.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c5.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
            c5.pack()

        elif z == "6":
            c6 = Canvas(frame_the_die, width=106, height=99)
            c6.create_oval(26, 50, 26, 54, outline="black", fill="black", width=20)
            c6.create_oval(79, 50, 79, 54, outline="black", fill="black", width=20)
            c6.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
            c6.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c6.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c6.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
            c6.pack()
        else:
            print("error")


    frame_the_die.pack(anchor=NE, pady=20, side=RIGHT)


    def player2():
        for widget in frame_the_die.winfo_children():
            widget.forget()

        thedie = ["1", "2", "3", "4", "5", "6"]
        z = random.choice(thedie)
        print(z)

        if z == "1":
            c1 = Canvas(frame_the_die1, width=106, height=99)
            c1.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
            c1.pack()
        elif z == "2":
            c2 = Canvas(frame_the_die1, width=106, height=99)
            c2.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c2.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c2.pack()
        elif z == "3":
            c3 = Canvas(frame_the_die1, width=106, height=99)
            c3.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c3.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
            c3.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c3.pack()

        elif z == "4":
            c4 = Canvas(frame_the_die1, width=106, height=99)
            c4.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
            c4.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c4.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c4.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
            c4.pack()

        elif z == "5":
            c5 = Canvas(frame_the_die1, width=106, height=99)
            c5.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
            c5.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
            c5.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c5.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c5.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
            c5.pack()

        elif z == "6":
            c6 = Canvas(frame_the_die1, width=106, height=99)
            c6.create_oval(26, 50, 26, 54, outline="black", fill="black", width=20)
            c6.create_oval(79, 50, 79, 54, outline="black", fill="black", width=20)
            c6.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
            c6.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
            c6.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
            c6.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
            c6.pack()
        else:
            print("error")


    frame_the_die1.pack(anchor=E, pady=20)

    roll = Button(window_die, command=player1, text="PLAYER 1", font=20)
    roll.pack(side=TOP, anchor=NW)

    roll1 = Button(window_die, command=player2, text="PLAYER 2", font=20)
    roll1.pack(anchor=W)
    def qd():
        window_die.destroy()
        window_wall.destroy()

    button_qd = Button(window_die, text="EXIT", font=20, relief="groove", bg="#eaf2bf", command=qd)
    button_qd.pack(anchor=S, side=LEFT)
    def qm():
        pass


    button_qm = Button(window_die, text="Quit to main menu", font=20, relief="groove", bg="#eaf2bf", command=qm)
    button_qm.pack(anchor=S, side=LEFT)


    print(i)


elif i == "2die":
    print(i)

else:print("error")


window_die.mainloop()

window_wall.mainloop()
