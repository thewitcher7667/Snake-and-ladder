
from tkinter import *
import random
from tkinter import messagebox
import tkinter as tk
import os
import time
import math

def play():
    playwindow = Tk()  # the start menue contain buttons
    playwindow.geometry("750x750")
    playwindow.title("snake and ladder")
    playwindow.resizable(False, False)
    playwindow.config(bg="#DB7D01")
    frameplaywindw = Frame(playwindow)


    lolo = []
    xp, yp = 11, 21
    for bzbezo in range(5):
        for x in range(xp, yp):
            lolo.append(x)
        xp += 20
        yp += 20

    canvas_wall2 = Canvas(playwindow, width=617, height=610)
    canvas_wall2.place(x=0, y=0)
    wal2 = PhotoImage(file="game.png")
    wall2 = canvas_wall2.create_image(308, 305, image=wal2)








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

                if ll in range(100):
                    if ll in [95, 96, 97, 98, 99]:
                        z = str(random.choice(range(1, 101 - ll)))
                    else:
                        z = random.choice(thedie)
                elif ll == 100:
                    clear()
                    messagebox.showinfo("snake and ladder", " Congratulations you have WON\n Try again?")

                totalzh2t.close()
                Label(playwindow, text=f"Player 1: {z}").place(x=620, y=400)
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
                    messagebox.showinfo("snake and ladder", " Congratulations you have LOST\n Try again? ")
                print("this is z comp", z)
                totalzh2t.close()
                Label(playwindow, text=f" Computer: {z}").place(x=620, y=450)
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
                    totkh = total
                    totall = str(totkh)
                bew.close()
                if total in [1,4,8,21,28,32,36,48,50,62,71,80,88,95,97]:
                    if total == 1:
                        total = 38
                        totall = "9" * 4 + "2"
                    elif total == 4:
                        total = 14
                        totall = "7" * 2
                    elif total == 8:
                        total = 30
                        totall = "5" * 6
                    elif total == 21:
                        total = 42
                        totall = "7" * 6
                    elif total == 28:
                        total = 76
                        totall = "7" * 10 + "6"
                    elif total == 32:
                        total = 10
                        totall = "5" * 2
                    elif total == 36:
                        total = 6
                        totall = "6"
                    elif total == 48:
                        total = 26
                        totall = "5" * 5 + "1"
                    elif total == 50:
                        total = 67
                        totall = "5" * 13 + "3"
                    elif total == 62:
                        total = 18
                        totall = "9" * +2
                    elif total == 71:
                        total = 92
                        totall = "9" * 10 + "2"
                    elif total == 80:
                        total = 99
                        totall = "9" * 10 + "9"
                    elif total == 88:
                        total = 24
                        totall = "6" * 4
                    elif total == 95:
                        total = 56
                        totall = "5" * 11 + "1"
                    elif total == 97:
                        total = 78
                        totall = "7" * 10 + "8"
                    wb3den = open("./imp files/player1.txt", 'w')
                    wb3den.write(totall)
                    wb3den.close()
                totalzh2t.write(str(total))
                totalzh2t.close()

                diedraw(total, "red", 0)

            player1()

            def comp():
                bew = open("./imp files/comp.txt", 'r')
                dew = bew.read()
                total = 0
                totalzh2t = open("./imp files/totalcomp.txt", "w")
                for ele in range(0, len(dew)):
                    total = total + int(dew[ele])

                bew.close()
                if total in [1,4,8,21,28,32,36,48,50,62,71,80,88,95,97]:
                    if total == 1:
                        total = 38
                        totall = "9" * 4 + "2"
                    elif total == 4:
                        total = 14
                        totall = "7" * 2
                    elif total == 8:
                        total = 30
                        totall = "5" * 6
                    elif total == 21:
                        total = 42
                        totall = "7" * 6
                    elif total == 28:
                        total = 76
                        totall = "7" * 10 + "6"
                    elif total == 32:
                        total = 10
                        totall = "5" * 2
                    elif total == 36:
                        total = 6
                        totall = "6"
                    elif total == 48:
                        total = 26
                        totall = "5" * 5 + "1"
                    elif total == 50:
                        total = 67
                        totall = "5" * 13 + "3"
                    elif total == 62:
                        total = 18
                        totall = "9" * +2
                    elif total == 71:
                        total = 92
                        totall = "9" * 10 + "2"
                    elif total == 80:
                        total = 99
                        totall = "9" * 10 + "9"
                    elif total == 88:
                        total = 24
                        totall = "6" * 4
                    elif total == 95:
                        total = 56
                        totall = "5" * 11 + "1"
                    elif total == 97:
                        total = 78
                        totall = "7" * 10 + "8"
                    wb3den = open("./imp files/comp.txt", 'w')
                    wb3den.write(totall)
                    wb3den.close()
                totalzh2t.write(str(total))
                totalzh2t.close()

                diedraw(total, "black", 20)

            comp()

        elif opti[1] == "11":  # 2players are involved
            pass
        elif opti[1] == "12":  # 3players are involved
            pass


    def diedraw(total, col, see):
        if total <= 10:
            xcord = (62 * total) - 31
            ycord = 550

            letsdrawrec(xcord, ycord, col, see)
        elif total > 10:
            ycord = 560 - (math.floor(total / 10)) * 60
            xbeforcord = math.modf(total / 10)
            xcordd = xbeforcord[0]

            if total in lolo:
                if total in [20,40,60,80,100]:
                    letsdrawrec(31, ycord+60, col, see)
                else:
                 xcord = 620 - ((62 * (xcordd * 10)) - 31)

                 letsdrawrec(xcord, ycord, col, see)

            else:
                if total in [30,50,70,90]:
                    letsdrawrec(589, ycord+60, col, see)
                xcord = (62 * (xbeforcord[0] * 10)) - 31

                letsdrawrec(xcord, ycord, col, see)


    def letsdrawrec(xcord, ycord, col, see):
        hawhaw = tk.Canvas(playwindow, width=20, height=20)
        hawhaw.create_rectangle(30, 10, 120, 80, outline=col, fill=col, width=160)
        hawhaw.place(x=xcord, y=(ycord + see))

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
    frameplaywindw.pack(anchor=NW)
    playwindow.mainloop()
