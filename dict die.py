import stat
from tkinter import *
import random
from tkinter import Tk
import time

window_die = Tk()
window_die.geometry("300x300")
window_die.focus()
window_die.resizable(False,False)
window_die.title("snacks and ladders")
window_die.config(bg="#e2e38f")


frame_the_die = Frame(window_die, bg='BLACK', bd=5, relief="groove", width=110, height=104)
frame_the_die1 = Frame(window_die, bg="black", bd=5, relief="groove", width=110, height=115)
def player1():
 for widget in frame_the_die1.winfo_children():
        widget.forget()

 thedie = ["1","2","3","4","5","6"]
 z = random.choice(thedie)
 print(z)

 if z == "1" :
     c1 = Canvas(frame_the_die, width=106, height=99)
     c1.create_oval(54, 50, 53, 54, outline="black", fill="black",width=20)
     c1.pack()
 elif z == "2" :
     c2 = Canvas(frame_the_die, width=106, height=99)
     c2.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
     c2.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
     c2.pack()
 elif z == "3" :
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

 elif z == "6" :
     c6 = Canvas(frame_the_die, width=106, height=99)
     c6.create_oval(26, 50, 26, 54, outline="black", fill="black", width=20)
     c6.create_oval(79, 50, 79, 54, outline="black", fill="black", width=20)
     c6.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
     c6.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
     c6.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
     c6.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
     c6.pack()
 else:print("error")
frame_the_die.pack(anchor=NE , pady=20 , side=RIGHT)




def player2() :
 for widget in frame_the_die.winfo_children():
        widget.forget()

 thedie = ["1","2","3","4","5","6"]
 z = random.choice(thedie)
 print(z)

 if z == "1" :
     c1 = Canvas(frame_the_die1, width=106, height=99)
     c1.create_oval(54, 50, 53, 54, outline="black", fill="black",width=20)
     c1.pack()
 elif z == "2" :
     c2 = Canvas(frame_the_die1, width=106, height=99)
     c2.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
     c2.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
     c2.pack()
 elif z == "3" :
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

 elif z == "6" :
     c6 = Canvas(frame_the_die1, width=106, height=99)
     c6.create_oval(26, 50, 26, 54, outline="black", fill="black", width=20)
     c6.create_oval(79, 50, 79, 54, outline="black", fill="black", width=20)
     c6.create_oval(79, 80, 79, 84, outline="black", fill="black", width=20)
     c6.create_oval(26, 80, 26, 84, outline="black", fill="black", width=20)
     c6.create_oval(79, 20, 79, 24, outline="black", fill="black", width=20)
     c6.create_oval(26, 20, 26, 24, outline="black", fill="black", width=20)
     c6.pack()
 else:print("error")
frame_the_die1.pack(anchor=E , pady=20 )

roll = Button(window_die,command=player1,text="PLAYER 1",font=20 )
roll.pack( side=TOP , anchor=NW)

roll1 = Button(window_die,command=player2,text="PLAYER 2",font=20)
roll1.pack(anchor=W )

button_p4 = Button(window_die,text="QUIT",font=20,relief="groove",bg="#eaf2bf", )
button_p4.pack(anchor=SE , side=BOTTOM)





window_die.mainloop()
