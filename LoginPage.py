from tkinter import *

import DataBase
import LoginAdmin
import Registration
import StudentsPage


from tkinter import ttk
import tkinter.messagebox


class mainwindow:
   def __init__(self):
        global windowM
        windowM = Tk()
        windowM.title("Attendance Management System ")
        screen_width = windowM.winfo_screenwidth()
        screen_height = windowM.winfo_screenheight()
        windowM.minsize(width=1000,height=500)
        windowM.maxsize(width=1000,height=500)
        # adding frame on the window
        frame=Frame(windowM)
        Label(frame,text="Attendance Management System ",font=('Arial Bold',16)).grid(column=0,row=1,columnspan=2,pady=(0,20))

        Label(frame,text="Enter Username",font=('Arial Bold',9)).grid(column=0,row=2,sticky=W,pady=(0,20))
        username=StringVar()
        Entry(frame,width=60,textvariable=username).grid(column=1,row=2,pady=(0,20))


        Label(frame,text="Enter Password",font=('Arial Bold',9)).grid(column=0,row=3,sticky=W,pady=(0,20))
        password=StringVar()
        Entry(frame,width=60,textvariable=password,show="*").grid(column=1,row=3,pady=(0,20))


        login = Button(frame, text = 'Login', bd = '5', width=30,
                       command= lambda  : self.Login(username,password)).grid(column=0, row=4, columnspan=2, pady=(0, 20))
        registration = Button(frame, text = 'Registration', bd = '5',width=30,
                              command= lambda  : self.Reg("")).grid(column=0,row=5,columnspan=2,pady=(0,20))


        frame.place(relx=0.5,rely=0.5,anchor=CENTER)
        login = Button(windowM,fg='blue', text='Admin login', bd='5', width=30,command=lambda :self.AdminLogin()).place(x=700, y=20)


        windowM.mainloop()
   def Login(self,usernames,passwords):
       k=DataBase.Data()
       k.__init__()
       k=k.login(usernames.get(),passwords.get())
       if k==True:
           self.sharingStudentData(usernames.get())
       else:
           tkinter.messagebox.showinfo("Login","invalite Username and Password ")
   def Reg(self,u):
       windowM.destroy()
       k=Registration.Register()
       k.__init__()
       print("s ")

   #sharing data to StudentPage
   def sharingStudentData(self,username):
       print("function sharingStudentData")
       objs = StudentsPage.StudentView()
       k=DataBase.Data()
       list=k.sharingTakeStudentData(username)
       windowM.destroy()
       for row in list:
           objs.__int__(row[0],row[1],row[2],row[3],row[4],row[5])
           break
   def AdminLogin(self):
       windowM.destroy()
       k=LoginAdmin.AdminPageL()
       k.__init__()










