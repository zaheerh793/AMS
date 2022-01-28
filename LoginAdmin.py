import tkinter.messagebox
from  tkinter import *

import Admin
import LoginPage


class AdminPageL:
    def __init__(self):
        global windowM
        windowM = Tk()
        windowM.title("Attendance Management System ")
        screen_width = windowM.winfo_screenwidth()
        screen_height = windowM.winfo_screenheight()
        windowM.minsize(width=1000, height=500)
        windowM.maxsize(width=1000, height=500)
        # adding frame on the window
        frame = Frame(windowM)
        Label(frame, text="Attendance Management System ", font=('Arial Bold', 16)).grid(column=0, row=1, columnspan=2,
                                                                                         pady=(0, 20))

        Label(frame, text="Enter Username", font=('Arial Bold', 9)).grid(column=0, row=2, sticky=W, pady=(0, 20))
        username = StringVar()
        Entry(frame, width=60, textvariable=username).grid(column=1, row=2, pady=(0, 20))

        Label(frame, text="Enter Password", font=('Arial Bold', 10)).grid(column=0, row=3, sticky=W, pady=(0, 20))
        password = StringVar()
        Entry(frame, width=60, textvariable=password,show="*").grid(column=1, row=3, pady=(0, 20))

        login = Button(frame, text='Login', bd='5', width=30,
                       command=lambda: self.login(username, password)).grid(column=0, row=4, columnspan=2, pady=(0, 20))
        Button(windowM, text=' Go Back ', bd='5', width=30,command=lambda :self.goback()).place(x=0,y=0)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        windowM.mainloop()
    def login(self,username,password):
        if username.get()=="Admin" and password.get()=="vvv":
            windowM.destroy()
            k=Admin.AdminView()
            k.__init__()
        else:
            tkinter.messagebox.showinfo("Error","incorrect password and username")
    def goback(self):
        windowM.destroy()
        l=LoginPage.mainwindow()
        l.__init__()

