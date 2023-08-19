d={"abc":"123"}
global frame2
from tkinter import *
window=Tk()
window.title("Login if you can")
window.geometry("500x500")
tv1=StringVar()
tv2=StringVar()
def sign_up():
    d[tv1.get()]=tv2.get()
    print(d)
    frame3=Frame(window,width=250,height=50,background="grey",highlightbackground="black",highlightthickness=2).place(x=120,y=390)
    label6=Label(frame3,text="Click on sign in again",font=('Arial 12'),background="grey",foreground="white").place(x=135,y=402)
def sign_in():
    if(tv1.get() in d.keys() and tv2.get() in d.values()):
        window.destroy()
        tab=Tk()
        tab.geometry("500x500")
        label5=Label(tab,text="Successfully logged in",font=('Arial 30')).place(x=50,y=250)
        tab.mainloop()
    else:
        frame2=Frame(window,width=250,height=50,background="grey",highlightbackground="black",highlightthickness=2).place(x=120,y=390)
        label4=Label(frame2,text="User not found",font=('Arial 12'),background="grey",foreground="white").place(x=135,y=402)
        button2=Button(frame2,width=10,height=1,background="white",foreground="grey",activeforeground="white",text="Sign up",command=sign_up).place(x=270,y=402)
frame1=Frame(window,width=250,height=250,background="white",highlightbackground="grey",highlightthickness=2).place(x=120,y=120)
label1=Label(frame1,text="Login",font=('Arial 20'),background="white").place(x=210,y=125)
label2=Label(frame1,text="Username:",font=('Arial 15'),background="white").place(x=135,y=170)
entry1=Entry(frame1,width=19,font=('Arial 15'),highlightbackground="grey",highlightthickness=1,textvariable=tv1).place(x=135,y=200)
label3=Label(frame1,text="Password:",font=('Arial 15'),background="white").place(x=135,y=240)
entry2=Entry(frame1,width=19,font=('Arial 15'),highlightbackground="grey",highlightthickness=1,textvariable=tv2).place(x=135,y=270)
button1=Button(frame1,width=10,height=2,background="grey",foreground="white",activeforeground="grey",text="Sign in",command=sign_in).place(x=205,y=315)
window.mainloop()