from tkinter import *
import base64


screen = Tk()
screen.geometry("420x420")
screen.title("Encrryption and Decryption")
screen.configure(bg="black")

#Text
Label(screen,text="enter text",font="impack 14 bold",bg="blue").place(x=160,y=6)
text1=Text(screen,font="20")
text1.place(x=5,y=45,width=410,height=120)

#Label
Label(screen,text="Enter Secret Key",font="impack 13 bold").place(x=130,y=180)

#entry
Entry(screen,bd=4,font="20",show="*").place(x=110,y=220)

#Button
Button(screen,text="Encrypt",font="arial 15 bold").place(x=15,y=280)
Button(screen,text="Decrypt",font="arial 15 bold").place(x=320,y=280)
Button(screen,text="Reset",font="arial 15 bold").place(x=103,y=350,width=220)

mainloop()
