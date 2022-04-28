import os
from tkinter import *
from tkinter import Tk
import random
import tkinter as tk


#######################################################################
######################################################################
#####################################################################
#player 1 only vs comp
#######################################################################
######################################################################
#####################################################################

    #main window


window_wall =tk.Tk()
window_wall.geometry("726x700")
window_wall.title("snacks and ladders")
window_wall.resizable(False,False)
canvas_w =tk.Canvas(window_wall,width=726,height=700)
canvas_w.place(x=0, y=0)
snake = PhotoImage(file="wallmain.png")
snakew = canvas_w.create_image(355, 350, image=snake,)






#die options for the exterior window
window_die = Toplevel()
window_die.geometry("300x120")
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
        with open("player1.txt", 'a') as file :
          file.write(z)
          file.close()
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

    def move1():
        with open("player1.txt") as file:
            dew = file.read()
            total = 0
            for ele in range(0, len(dew)):
                total = total + int(dew[ele])
                print(total)

                # start of map from one to hundred player 1
                if total == 1:
                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=660)
                    tk.Misc.lift(one)
                elif total == 2:
                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=660)
                    tk.Misc.lift(two)

                elif total == 3:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=660)
                    tk.Misc.lift(three)
                elif total == 4:
                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=660)
                    tk.Misc.lift(four)
                elif total == 5:
                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=660)
                    tk.Misc.lift(five)

                elif total == 6:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=660)
                    tk.Misc.lift(six)
                elif total == 7:
                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=660)
                    tk.Misc.lift(seven)

                elif total == 8:
                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=660)
                    tk.Misc.lift(eight)

                elif total == 9:
                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=660)
                    tk.Misc.lift(nine)

                elif total == 10:
                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=660)
                    tk.Misc.lift(ten)


                #######################################################################
                ######################################################################
                # multi by 11 to 20
                ####################################################################
                elif total == 11:
                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=590)
                    tk.Misc.lift(one)

                elif total == 12:
                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=590)
                    tk.Misc.lift(two)

                elif total == 13:
                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=590)
                    tk.Misc.lift(three)

                elif total == 14:
                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=590)
                    tk.Misc.lift(four)

                elif total == 15:
                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=590)
                    tk.Misc.lift(five)

                elif total == 16:
                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=590)
                    tk.Misc.lift(six)

                elif total == 17:
                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=590)
                    tk.Misc.lift(seven)

                elif total == 18:
                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=590)
                    tk.Misc.lift(eight)

                elif total == 19:
                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=590)
                    tk.Misc.lift(nine)

                elif total == 20:
                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=590)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 21 to 30
                ####################################################################
                elif total == 21:
                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=520)
                    tk.Misc.lift(one)


                elif total == 22:
                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=520)
                    tk.Misc.lift(two)


                elif total == 23:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=520)
                    tk.Misc.lift(three)

                elif total == 24:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=520)
                    tk.Misc.lift(four)

                elif total == 25:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=520)
                    tk.Misc.lift(five)

                elif total == 26:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=520)
                    tk.Misc.lift(six)

                elif total == 27:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=520)
                    tk.Misc.lift(seven)

                elif total == 28:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=520)
                    tk.Misc.lift(eight)

                elif total == 29:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=520)
                    tk.Misc.lift(nine)

                elif total == 30:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=520)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 31 to 40
                ####################################################################
                elif total == 31:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=450)
                    tk.Misc.lift(one)

                elif total == 32:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=450)
                    tk.Misc.lift(two)

                elif total == 33:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=450)
                    tk.Misc.lift(three)

                elif total == 34:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=450)
                    tk.Misc.lift(four)

                elif total == 35:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=450)
                    tk.Misc.lift(five)

                elif total == 36:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=450)
                    tk.Misc.lift(six)

                elif total == 37:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=450)
                    tk.Misc.lift(seven)

                elif total == 38:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=450)
                    tk.Misc.lift(eight)

                elif total == 39:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=450)
                    tk.Misc.lift(nine)

                elif total == 40:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=450)
                    tk.Misc.lift(ten)


                #######################################################################
                ######################################################################
                # multi by 41 to 50
                ####################################################################
                elif total == 41:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=380)
                    tk.Misc.lift(one)

                elif total == 42:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=380)
                    tk.Misc.lift(two)

                elif total == 43:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=380)
                    tk.Misc.lift(three)

                elif total == 44:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=380)
                    tk.Misc.lift(four)

                elif total == 45:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=380)
                    tk.Misc.lift(five)

                elif total == 46:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=380)
                    tk.Misc.lift(six)

                elif total == 47:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=380)
                    tk.Misc.lift(seven)

                elif total == 48:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=380)
                    tk.Misc.lift(eight)

                elif total == 49:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=380)
                    tk.Misc.lift(nine)

                elif total == 50:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=380)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 51 to 60
                ####################################################################
                elif total == 51:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=310)
                    tk.Misc.lift(one)

                elif total == 52:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=310)
                    tk.Misc.lift(two)

                elif total == 53:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=310)
                    tk.Misc.lift(three)

                elif total == 54:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=310)
                    tk.Misc.lift(four)

                elif total == 55:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=310)
                    tk.Misc.lift(five)

                elif total == 56:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=310)
                    tk.Misc.lift(six)

                elif total == 57:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=310)
                    tk.Misc.lift(seven)

                elif total == 58:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=310)
                    tk.Misc.lift(eight)

                elif total == 59:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=310)
                    tk.Misc.lift(nine)

                elif total == 60:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=310)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 61 to 70
                ####################################################################
                elif total == 61:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=240)
                    tk.Misc.lift(one)

                elif total == 62:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=240)
                    tk.Misc.lift(two)

                elif total == 63:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=240)
                    tk.Misc.lift(three)

                elif total == 64:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=240)
                    tk.Misc.lift(four)

                elif total == 65:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=240)
                    tk.Misc.lift(five)

                elif total == 66:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=240)
                    tk.Misc.lift(six)

                elif total == 67:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=240)
                    tk.Misc.lift(seven)

                elif total == 68:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=240)
                    tk.Misc.lift(eight)

                elif total == 69:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=240)
                    tk.Misc.lift(nine)

                elif total == 70:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=240)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 71 to 80
                ####################################################################
                elif total == 71:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=170)
                    tk.Misc.lift(one)

                elif total == 72:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=170)
                    tk.Misc.lift(two)

                elif total == 73:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=170)
                    tk.Misc.lift(three)

                elif total == 74:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=170)
                    tk.Misc.lift(four)

                elif total == 75:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=170)
                    tk.Misc.lift(five)

                elif total == 76:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=170)
                    tk.Misc.lift(six)

                elif total == 77:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=170)
                    tk.Misc.lift(seven)

                elif total == 78:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=170)
                    tk.Misc.lift(eight)

                elif total == 79:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=170)
                    tk.Misc.lift(nine)

                elif total == 80:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=170)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 81 to 90
                ####################################################################
                elif total == 81:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=100)
                    tk.Misc.lift(one)

                elif total == 82:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=100)
                    tk.Misc.lift(two)

                elif total == 83:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=100)
                    tk.Misc.lift(three)

                elif total == 84:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=100)
                    tk.Misc.lift(four)

                elif total == 85:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=100)
                    tk.Misc.lift(five)

                elif total == 86:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=100)
                    tk.Misc.lift(six)

                elif total == 87:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=100)
                    tk.Misc.lift(seven)

                elif total == 88:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=100)
                    tk.Misc.lift(eight)

                elif total == 89:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=100)
                    tk.Misc.lift(nine)

                elif total == 90:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=100)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 91 to 100
                ####################################################################
                elif total == 91:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    one.place(x=30, y=30)
                    tk.Misc.lift(one)

                elif total == 92:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    two.place(x=100, y=30)
                    tk.Misc.lift(two)

                elif total == 93:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    three.place(x=170, y=30)
                    tk.Misc.lift(three)

                elif total == 94:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    four.place(x=240, y=30)
                    tk.Misc.lift(four)

                elif total == 95:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    five.place(x=310, y=30)
                    tk.Misc.lift(five)

                elif total == 96:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    six.place(x=380, y=30)
                    tk.Misc.lift(six)

                elif total == 97:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    seven.place(x=450, y=30)
                    tk.Misc.lift(seven)

                elif total == 98:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    eight.place(x=520, y=30)
                    tk.Misc.lift(eight)

                elif total == 99:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    nine.place(x=590, y=30)
                    tk.Misc.lift(nine)

                elif total == 100:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="black", fill="black", width=160, )
                    ten.place(x=660, y=30)
                    tk.Misc.lift(ten)


    def player2():



        thedie = ["1", "2", "3", "4", "5", "6"]
        z = random.choice(thedie)
        print(z)
        with open("player2.txt", 'a') as file:
          file.write(z)
          file.close()









    def move2():

        with open("player2.txt") as file:
            dew1 = file.read()
            total2 = 0
            for ele1 in range(0, len(dew1)):
                total2 = total2 + int(dew1[ele1])
                print(total2)

                # start of map from one to hundred player 1
                if total2 == 1:
                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=660)
                    tk.Misc.lift(one)
                elif total2 == 2:
                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=660)
                    tk.Misc.lift(two)

                elif total2 == 3:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=660)
                    tk.Misc.lift(three)
                elif total2 == 4:
                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=660)
                    tk.Misc.lift(four)
                elif total2 == 5:
                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=660)
                    tk.Misc.lift(five)

                elif total2 == 6:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=660)
                    tk.Misc.lift(six)
                elif total2 == 7:
                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=660)
                    tk.Misc.lift(seven)

                elif total2 == 8:
                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=660)
                    tk.Misc.lift(eight)

                elif total2 == 9:
                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=660)
                    tk.Misc.lift(nine)

                elif total2 == 10:
                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=660)
                    tk.Misc.lift(ten)


                #######################################################################
                ######################################################################
                # multi by 11 to 20
                ####################################################################
                elif total2 == 11:
                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=590)
                    tk.Misc.lift(one)

                elif total2 == 12:
                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=590)
                    tk.Misc.lift(two)

                elif total2 == 13:
                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=590)
                    tk.Misc.lift(three)

                elif total2 == 14:
                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=590)
                    tk.Misc.lift(four)

                elif total2 == 15:
                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=590)
                    tk.Misc.lift(five)

                elif total2 == 16:
                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=590)
                    tk.Misc.lift(six)

                elif total2 == 17:
                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=590)
                    tk.Misc.lift(seven)

                elif total2 == 18:
                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=590)
                    tk.Misc.lift(eight)

                elif total2 == 19:
                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=590)
                    tk.Misc.lift(nine)

                elif total2 == 20:
                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=590)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 21 to 30
                ####################################################################
                elif total2 == 21:
                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=520)
                    tk.Misc.lift(one)


                elif total2 == 22:
                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=520)
                    tk.Misc.lift(two)


                elif total2 == 23:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=520)
                    tk.Misc.lift(three)

                elif total2 == 24:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=520)
                    tk.Misc.lift(four)

                elif total2 == 25:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=520)
                    tk.Misc.lift(five)

                elif total2 == 26:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=520)
                    tk.Misc.lift(six)

                elif total2 == 27:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=520)
                    tk.Misc.lift(seven)

                elif total2 == 28:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=520)
                    tk.Misc.lift(eight)

                elif total2 == 29:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=520)
                    tk.Misc.lift(nine)

                elif total2 == 30:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=520)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 31 to 40
                ####################################################################
                elif total2 == 31:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=450)
                    tk.Misc.lift(one)

                elif total2 == 32:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=450)
                    tk.Misc.lift(two)

                elif total2 == 33:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=450)
                    tk.Misc.lift(three)

                elif total2 == 34:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=450)
                    tk.Misc.lift(four)

                elif total2 == 35:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=450)
                    tk.Misc.lift(five)

                elif total2 == 36:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=450)
                    tk.Misc.lift(six)

                elif total2 == 37:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=450)
                    tk.Misc.lift(seven)

                elif total2 == 38:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=450)
                    tk.Misc.lift(eight)

                elif total2 == 39:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=450)
                    tk.Misc.lift(nine)

                elif total2 == 40:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=450)
                    tk.Misc.lift(ten)


                #######################################################################
                ######################################################################
                # multi by 41 to 50
                ####################################################################
                elif total2 == 41:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=380)
                    tk.Misc.lift(one)

                elif total2 == 42:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=380)
                    tk.Misc.lift(two)

                elif total2 == 43:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=380)
                    tk.Misc.lift(three)

                elif total2 == 44:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=380)
                    tk.Misc.lift(four)

                elif total2 == 45:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=380)
                    tk.Misc.lift(five)

                elif total2 == 46:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=380)
                    tk.Misc.lift(six)

                elif total2 == 47:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=380)
                    tk.Misc.lift(seven)

                elif total2 == 48:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=380)
                    tk.Misc.lift(eight)

                elif total2 == 49:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=380)
                    tk.Misc.lift(nine)

                elif total2 == 50:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=380)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 51 to 60
                ####################################################################
                elif total2 == 51:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=310)
                    tk.Misc.lift(one)

                elif total2 == 52:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=310)
                    tk.Misc.lift(two)

                elif total2 == 53:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=310)
                    tk.Misc.lift(three)

                elif total2 == 54:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=310)
                    tk.Misc.lift(four)

                elif total2 == 55:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=310)
                    tk.Misc.lift(five)

                elif total2 == 56:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=310)
                    tk.Misc.lift(six)

                elif total2 == 57:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=310)
                    tk.Misc.lift(seven)

                elif total2 == 58:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=310)
                    tk.Misc.lift(eight)

                elif total2 == 59:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=310)
                    tk.Misc.lift(nine)

                elif total2 == 60:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=310)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 61 to 70
                ####################################################################
                elif total2 == 61:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=240)
                    tk.Misc.lift(one)

                elif total2 == 62:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=240)
                    tk.Misc.lift(two)

                elif total2 == 63:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=240)
                    tk.Misc.lift(three)

                elif total2 == 64:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=240)
                    tk.Misc.lift(four)

                elif total2 == 65:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=240)
                    tk.Misc.lift(five)

                elif total2 == 66:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=240)
                    tk.Misc.lift(six)

                elif total2 == 67:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=240)
                    tk.Misc.lift(seven)

                elif total2 == 68:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=240)
                    tk.Misc.lift(eight)

                elif total2 == 69:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=240)
                    tk.Misc.lift(nine)

                elif total2 == 70:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=240)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 71 to 80
                ####################################################################
                elif total2 == 71:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=170)
                    tk.Misc.lift(one)

                elif total2 == 72:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=170)
                    tk.Misc.lift(two)

                elif total2 == 73:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=170)
                    tk.Misc.lift(three)

                elif total2 == 74:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=170)
                    tk.Misc.lift(four)

                elif total2 == 75:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=170)
                    tk.Misc.lift(five)

                elif total2 == 76:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=170)
                    tk.Misc.lift(six)

                elif total2 == 77:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=170)
                    tk.Misc.lift(seven)

                elif total2 == 78:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=170)
                    tk.Misc.lift(eight)

                elif total2 == 79:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=170)
                    tk.Misc.lift(nine)

                elif total2 == 80:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=170)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 81 to 90
                ####################################################################
                elif total2 == 81:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=100)
                    tk.Misc.lift(one)

                elif total2 == 82:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=100)
                    tk.Misc.lift(two)

                elif total2 == 83:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=100)
                    tk.Misc.lift(three)

                elif total2 == 84:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=100)
                    tk.Misc.lift(four)

                elif total2 == 85:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=100)
                    tk.Misc.lift(five)

                elif total2 == 86:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=100)
                    tk.Misc.lift(six)

                elif total2 == 87:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=100)
                    tk.Misc.lift(seven)

                elif total2 == 88:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=100)
                    tk.Misc.lift(eight)

                elif total2 == 89:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=100)
                    tk.Misc.lift(nine)

                elif total2 == 90:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=100)
                    tk.Misc.lift(ten)
                #######################################################################
                ######################################################################
                # multi by 91 to 100
                ####################################################################
                elif total2 == 91:

                    # one
                    one = tk.Canvas(window_wall, width=30, height=30)
                    one.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    one.place(x=30, y=30)
                    tk.Misc.lift(one)

                elif total2 == 92:

                    # two
                    two = tk.Canvas(window_wall, width=30, height=30)
                    two.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    two.place(x=100, y=30)
                    tk.Misc.lift(two)

                elif total2 == 93:

                    # three
                    three = tk.Canvas(window_wall, width=30, height=30)
                    three.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    three.place(x=170, y=30)
                    tk.Misc.lift(three)

                elif total2 == 94:

                    # four
                    four = tk.Canvas(window_wall, width=30, height=30)
                    four.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    four.place(x=240, y=30)
                    tk.Misc.lift(four)

                elif total2 == 95:

                    # five
                    five = tk.Canvas(window_wall, width=30, height=30)
                    five.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    five.place(x=310, y=30)
                    tk.Misc.lift(five)

                elif total2 == 96:

                    # six
                    six = tk.Canvas(window_wall, width=30, height=30)
                    six.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    six.place(x=380, y=30)
                    tk.Misc.lift(six)

                elif total2 == 97:

                    # seven
                    seven = tk.Canvas(window_wall, width=30, height=30)
                    seven.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    seven.place(x=450, y=30)
                    tk.Misc.lift(seven)

                elif total2 == 98:

                    # eight
                    eight = tk.Canvas(window_wall, width=30, height=30)
                    eight.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    eight.place(x=520, y=30)
                    tk.Misc.lift(eight)

                elif total2 == 99:

                    # nine
                    nine = tk.Canvas(window_wall, width=30, height=30)
                    nine.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    nine.place(x=590, y=30)
                    tk.Misc.lift(nine)

                elif total2 == 100:

                    # ten
                    ten = tk.Canvas(window_wall, width=30, height=30)
                    ten.create_oval(54, 50, 53, 54, outline="red", fill="red", width=160, )
                    ten.place(x=660, y=30)
                    tk.Misc.lift(ten)







    roll = Button(window_die, command=lambda: [player1(), move1(),player2(),move2(),], text="PLAYER 1", font=20)

    roll.pack(side=TOP, anchor=NW)

    roll1 = Button(window_die, state=DISABLED,text="PLAYER 2", font=20)
    roll1.pack(anchor=W)


    def qd():
        open("player1.txt", 'w').close()
        open("player2.txt", 'w').close()
        window_die.destroy()
        window_wall.destroy()


    button_qd = Button(window_die, text="EXIT", font=20, relief="groove", bg="#eaf2bf", command=qd)
    button_qd.pack(side=TOP, anchor=W)
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
