from tkinter import *
import random
from tkinter import messagebox
import tkinter as tk
import os
import time
import math

playwindow = Tk()  # the start menue contain buttons
playwindow.geometry("750x750")
playwindow.title("snake and ladder")
playwindow.resizable(False, False)
playwindow.config(bg="#DB7D01")
frameplaywindw = Frame(playwindow)
framehawhaw = Frame(frameplaywindw)
lolo = []
xp, yp = 11, 21
for bzbezo in range(5):
    for x in range(xp, yp):
        lolo.append(x)
    xp += 20
    yp += 20

a = 101
b = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
for r in range(1, 11):
    if r in b[0]:
        for c in range(1, 11):
            a = a - 1
            Label(frameplaywindw, text=a, bg="#EEE8AA", width=8, relief=SOLID, fg="black").grid(row=r, column=c + 1,
                                                                                            ipadx=0,
                                                                                            ipady=20, padx=0, pady=0)
    if r in b[1]:
        for cd in range(11, 1, -1):
            a = a - 1
            Label(frameplaywindw, text=a, bg="#D3D5D4", width=8, relief=SOLID, fg="black").grid(row=r, column=cd,
                                                                                            ipadx=0,
                                                                                            ipady=20, padx=0, pady=0)


def dietoss(z):
    if z == "1":
        c1 = Canvas(playwindow, width=106, height=99)
        c1.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
        c1.place(x=1, y=620)
    elif z == "2":
        c2 = Canvas(playwindow, width=106, height=99)
        c2.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
        c2.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
        c2.place(x=1, y=620)
    elif z == "3":
        c3 = Canvas(playwindow, width=106, height=99)
        c3.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
        c3.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
        c3.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
        c3.place(x=1, y=620)
    elif z == "4":
        c4 = Canvas(playwindow, width=106, height=99)
        c4.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
        c4.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
        c4.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
        c4.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
        c4.place(x=1, y=620)
    elif z == "5":
        c5 = Canvas(playwindow, width=106, height=99)
        c5.create_oval(54, 50, 53, 54, outline="black", fill="black", width=20)
        c5.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
        c5.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
        c5.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
        c5.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
        c5.place(x=1, y=620)
    elif z == "6":
        c6 = Canvas(playwindow, width=106, height=99)
        c6.create_oval(26, 50, 26, 54, outline="black", fill="black", width=20)
        c6.create_oval(79, 50, 79, 54, outline="black", fill="black", width=20)
        c6.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
        c6.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
        c6.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
        c6.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
        c6.place(x=1, y=620)
    else:
        print("error")


opti = []
saveread = open("./imp files/save.txt", "r")
global txt
for txt in saveread:
    pass
opti.append(txt[0])
opti.append(txt[1:])


def die():
    if opti[0] == "0":
        thedie = ["1", "2", "3", "4", "5", "6"]

        def player1die():
            totalzh2t = open("./imp files/totalplayer1.txt", "r")
            ll = totalzh2t.read()
            if ll == "":
                ll = 0
            else:
                ll = int(ll)
            print("this is ll", ll)
            if ll in range(100):
                if ll in [95, 96, 97, 98, 99]:
                    z = str(random.choice(range(1, 101 - ll)))

                else:
                    z = random.choice(thedie)
            elif ll == 100:
                clear()
                messagebox.showinfo("snake and ladder", " Congratulations you have won\n Try again?")
                print("win")
            print("this is z", z)
            totalzh2t.close()
            savez = open("./imp files/player1.txt", "a")
            savez.write(str(z))
            savez.close()
            dietoss(z)

        player1die()

        def compdie():
            totalzh2t = open("./imp files/totalcomp.txt", "r")
            ll = totalzh2t.read()
            if ll == "":
                ll = 0
            else:
                ll = int(ll)
            print("this is ll comp", ll)
            if ll in range(100):
                if ll in [95, 96, 97, 98, 99]:
                    z = str(random.choice(range(1, 101 - ll)))
                else:
                    z = random.choice(thedie)
            elif ll == 100:
                clear()
                messagebox.showinfo("snake and ladder", " Congratulations you have won\n Try again? comp")
                print("win")
            print("this is z comp", z)
            totalzh2t.close()
            savez = open("./imp files/comp.txt", "a")
            savez.write(str(z))
            savez.close()

        compdie()
    elif opti[0] == "1":
        thedie = ["1", "2", "3", "4", "5", "6"]
        z = random.choice(thedie)



def adddiez():
    if opti[1] == "10":  # 1player and comp are involved
        def player1():
            bew = open("./imp files/player1.txt", 'r+')
            dew = bew.read()
            total = 0
            totalzh2t = open("./imp files/totalplayer1.txt", "w")
            for ele in range(0, len(dew)):
                total = total + int(dew[ele])
            print("this is tot", total)
            totalzh2t.write(str(total))
            totalzh2t.close()
            bew.close()
            diedraw(total, "red",0)

        player1()

        def comp():
            bew = open("./imp files/comp.txt", 'r+')
            dew = bew.read()
            total = 0
            totalzh2t = open("./imp files/totalcomp.txt", "w")
            for ele in range(0, len(dew)):
                total = total + int(dew[ele])
            print("this is tot comp", total)
            totalzh2t.write(str(total))
            totalzh2t.close()
            bew.close()
            diedraw(total, "white",20)

        comp()

    elif opti[1] == "11":  # 2players are involved
        pass
    elif opti[1] == "12":  # 3players are involved
        pass


def diedraw(total, col,see):
    if total <= 10:
        xcord = (62 * total) - 31
        ycord = 550
        letsdrawrec(xcord, ycord, col,see)
    elif total > 10:
        ycord = 560 - (math.floor(total / 10)) * 60
        xbeforcord = math.modf(total / 10)
        xcordd = xbeforcord[0]
        if total in lolo:
            if xcordd == 0:
                xcordd = 10
            xcord = 620 - ((62 * (xcordd * 10)) - 31)
            letsdrawrec(xcord, ycord, col,see)
        else:
            xcord = (62 * (xbeforcord[0] * 10)) - 31
            letsdrawrec(xcord, ycord, col,see)


def letsdrawrec(xcord, ycord, col,see):
    hawhaw = tk.Canvas(playwindow, width=15, height=15)
    hawhaw.create_rectangle(30, 10, 120, 80, outline=col, fill=col, width=160)
    hawhaw.place(x=xcord, y=(ycord+see))
    hawhaw.after(1500,hawhaw.destroy)


Button(playwindow, overrelief=SOLID, command=lambda: [die(), adddiez()], text="Player 1", font=20, pady=20,
       relief="sunken", bg="#eaf2bf", width=10,
       activebackground="#e1e3de", bd=1, cursor="hand2").place(x=620, y=100)


def clear():
    bew = open("./imp files/player1.txt", 'w')
    bewcomp = open("./imp files/comp.txt", 'w')
    totalzh2t = open("./imp files/totalplayer1.txt", "w")
    totalzh2tcomp = open("./imp files/totalcomp.txt", "w")
    totalzh2tcomp.write("")
    totalzh2tcomp.close()
    totalzh2t.write("")
    totalzh2t.close()
    bewcomp.write("")
    bewcomp.close()
    bew.write("")
    bew.close()


Button(playwindow, overrelief=SOLID, command=clear, text="clear", font=20, pady=20, relief="sunken", bg="#eaf2bf",
       width=10,
       activebackground="#e1e3de", bd=1, cursor="hand2").place(x=620, y=200)
framehawhaw.place()
frameplaywindw.pack(anchor=NW)
playwindow.mainloop()
