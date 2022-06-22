from tkinter import *
from tkinter import messagebox
start = Tk()  # the start menue contain buttons
start.geometry("780x720")
start.title("snake and ladder")
start.resizable(False, False)
start.config(bg="#e1e3de")
bg = PhotoImage(file="wall2.png") # image 2 the background
bg1 = Label(start, image=bg)  # to display the image
bg1.place(x=0, y=25)  # to size the image on x and y axis
icon1 = PhotoImage(file='icon1.png')
start.iconphoto(True,icon1)
frame1 = Frame(start)
frame1.config(bg="#e1e3de")

# ############################################################button 1 to play start
def play():
    playwindow = Tk()  # the start menue contain buttons
    playwindow.geometry("700x700")
    playwindow.title("snake and ladder")
    playwindow.resizable(False, False)
    playwindow.config(bg="red")
    a = 101
    b = [[1,3,5,7,9],[2,4,6,8,10]]
    for r in range(1,11):
        if r in b[0]:
            for c in range(1,11):
                a = a - 1
                Label(playwindow, text=a, bg="red", width=2, relief=SOLID, fg="white").grid(row=r, column=c+1, ipadx=19.5,
                                                                                            ipady=19.5)
        if r in b[1]:
            for cd in range(11,1,-1):
                a = a - 1
                Label(playwindow, text=a, bg="red", width=2, relief=SOLID, fg="white").grid(row=r, column=cd ,
                                                                                            ipadx=19.5,
                                                                                            ipady=19.5)


    playwindow.mainloop()

button1 = Button(frame1, text="play", command=play, font=20, pady=20, relief="sunken", bg="#eaf2bf", width=10,
                 activebackground="#e1e3de", bd=1, cursor="hand2")
button1.pack(side=TOP, pady=30)

# ############################################################button 1 to play end
# ############################################################button 2 to options start
# The command for the button 2 start

def gametype():
    # command for child button in the game type window to save the option that player chooses and to quit yhe window

    def savegametype():
        save = [(v.get()), (vv.get())]  # save the value of the option default value = 0 : I die , player 1
        print(save)   # to ensure from result for me
        gametypewindow.destroy()
    gametypewindow = Toplevel(start)
    gametypewindow.title("snake and ladder")
    gametypewindow.geometry("250x250")
    gametypewindow.resizable(False, False)
    gametypewindow.config(bg="#81d12c")
    icon1 = PhotoImage(file='icon1.png')
    gametypewindow.iconphoto(True, icon1)
    Label(gametypewindow, text="choose game type :", fg="black", bg="#e1e3de", font=20).pack()
    # frames to contain options and separate die from player , place , label them.
    framegametype1 = LabelFrame(gametypewindow,text='Die')
    framegametype1.config(bg="#81d12c")
    framegametype2 = LabelFrame(gametypewindow, text='Player')
    framegametype2.config(bg="#81d12c")
    # frames pack at the end of def
    value1 = {"I die":0,"II die":1}   # dict one for dies
    value2 = {"I player":0,"II player":11,"III player":22} # dict 2 for players
    v = IntVar()   # get value of choice of die
    # display the radiobutton die
    for (text, value) in value1.items():
        Radiobutton(framegametype1, text=text, variable=v,
                    value=value,pady=10,width=5).pack(pady=5)
    vv = IntVar() # get value of choice of player
    # display the radiobutton player
    for (text, value) in value2.items():
        Radiobutton(framegametype2, text=text, variable=vv,
                    value=value,pady=10,width=8,cursor="hand2",bd=1,).pack(pady=5)
    # buttons to save the options and quit
    # but it above all for the v.get and vv.get to be enabled
    Button(gametypewindow,text="Save",pady=10, relief="sunken", bg="#eaf2bf", width=8,
                 activebackground="#e1e3de", bd=1, cursor="hand2", command=savegametype).place(x=15,y=170)

    # end of save button
    # strict if player opens it must choose or it will give birth
    gametypewindow.protocol("WM_DELETE_WINDOW", gametype)
    framegametype1.place(x=15,y=40)
    framegametype2.place(x=150,y=40)
    gametypewindow.mainloop()


    # end of button 2 def command

button2 = Button(frame1, text="Game type", command=gametype, font=20, pady=20, relief="sunken", bg="#eaf2bf", width=10,
                 activebackground="#e1e3de", bd=1, cursor="hand2")
button2.pack(side=TOP, pady=30)

# ############################################################button 2 to game type end

# ############################################################button 3 to options start

button3 = Button(frame1, text="Options", command="", font=20, pady=20, relief="sunken", bg="#eaf2bf", width=10,
                 activebackground="#e1e3de", bd=1, cursor="hand2")
button3.pack(side=TOP, pady=30)
# ############################################################button 3 to options end
# ############################################################button 4 to about start
def about():
    messagebox.showinfo("snake and ladder game",
                        "coded by kerolos ayman small project to practise python link to the code will be found in github")


button4 = Button(frame1, text="About", command=about, font=20, pady=20, relief="sunken", bg="#eaf2bf", width=10,
                 activebackground="#e1e3de", bd=1, cursor="hand2")
button4.pack(side=TOP, pady=30)
# ############################################################button 4 to about end
# ############################################################button 5 to quit start

def quitall():
   ans = messagebox.askyesno("snake and ladder", "are you really want to quit the game", icon='question')
   if ans == True:
       quit()
   else:print("")


button5 = Button(frame1, text="Quit", command=quitall, font=20, pady=20, relief="sunken", bg="#eaf2bf", width=10,
                 activebackground="#e1e3de", bd=1, cursor="hand2")
button5.pack(side=BOTTOM, pady=30)
# ############################################################button 5 to quit end
frame1.place(x=620, y=25)
start.mainloop()
