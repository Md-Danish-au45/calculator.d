from tkinter import *
root = Tk()
root.geometry("300x600")
root.title("calculator bby danish")
root.wm_iconbitmap("note.ico")


def click(event):
    global danishvalue
    text =event.widget.cget("text")
    print(text)

    if text =="=":
        if danishvalue.get().isdigit():
            value = int(danishvalue.get())
        else:
            value=eval(screen.get())
        danishvalue.set(value)
        screen.update()
    elif text == "C":
        danishvalue.set("")
        screen.update()

    else:
        danishvalue.set(danishvalue.get() + text)
        screen.pdate()


Label(root,text="Personal Calculator",bg="black",fg="white",font="Helvetica 18 bold",pady=8).pack(fill=X)
    

danishvalue = StringVar()
danishvalue.set("")

screen = Entry(root,textvar=danishvalue,relief = SUNKEN,font="Helvetica 40 bold")
screen.pack(fill=X,ipadx=8,padx=10)

f= Frame(root,bg="grey",)
b=Button(f,text="9",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="8",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text="7",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


f.pack()

f= Frame(root,bg="grey",)
b=Button(f,text="6",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="5",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text="4",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


f.pack()
f= Frame(root,bg="grey",)
b=Button(f,text="3",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="2",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text="1",padx=14,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


f.pack()
f= Frame(root,bg="grey",)
b=Button(f,text="0",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="-",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text="+",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

f.pack()
f= Frame(root,bg="grey",)
b=Button(f,text="*",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="%",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

b=Button(f,text="/",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

f.pack()
f= Frame(root,bg="grey",)
b=Button(f,text="C",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text=".",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)


b=Button(f,text="=",padx=15,pady=12,font = "lucida 16 bold")
b.pack(side=LEFT,padx=8,pady=8)
b.bind("<Button-1>",click)

f.pack()


root.mainloop()