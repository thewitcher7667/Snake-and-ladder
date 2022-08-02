from tkinter import *



def switchButtonState():
    if (button1['state'] == NORMAL):
        button1['state'] = DISABLED
    else:
        button1['state'] = NORMAL


app = Tk()
app.geometry("300x100")
button1 = Button(app, text="Python Button 1",
                    state=DISABLED)
button2 = Button(app, text="EN/DISABLE Button 1",
                    command=switchButtonState)
button1.pack(side=LEFT)
button2.pack(side=RIGHT)
app.mainloop()