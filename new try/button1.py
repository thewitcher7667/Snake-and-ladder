from tkinter import *

save = [0, 0]
playwindow = Tk()  # the start menue contain buttons
playwindow.geometry("700x700")
playwindow.title("snake and ladder")
playwindow.resizable(False, False)
playwindow.config(bg="red")
a = 101
b = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
for r in range(1, 11):
    if r in b[0]:
        for c in range(1, 11):
            a = a - 1
            Label(playwindow, text=a, bg="red", width=2, relief=SOLID, fg="white").grid(row=r, column=c + 1, ipadx=19.5,
                                                                                        ipady=19.5)
    if r in b[1]:
        for cd in range(11, 1, -1):
            a = a - 1
            Label(playwindow, text=a, bg="red", width=2, relief=SOLID, fg="white").grid(row=r, column=cd,
                                                                                        ipadx=19.5,
                                                                                        ipady=19.5)





if save[0] == 0 :
    print("I die")
elif save[0] == 1 :
    print("II die")



playwindow.mainloop()

thedie = ["1", "2", "3", "4", "5", "6"]
z = random.choice(thedie)
print(z)
with open("player1.txt", 'a') as file:
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




