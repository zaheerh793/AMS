import tkinter.messagebox
from tkinter import *
import DataBase
import LoginAdmin


class AdminView:
    countVA=0
    countlb = 0
    countSr = 0
    countVS=0

    def __init__(self):
        global windowA
        windowA=Tk()
        windowA.title("Attendance Management System ")
        windowA.minsize(width=1000, height=500)
        windowA.maxsize(width=1000, height=500)
        Button(windowA, text="view Attendance",fg='blue', font=('Arial Bold', 10),command=lambda :self.viewAttendance()).place(x=100, y=10)
        Button(windowA, text=" Leave Approval request ", fg='blue', font=('Arial Bold', 10),command=lambda :self.Approvalleave()).place(x=250, y=10)
        Button(windowA, text=" view a one Student record", fg='blue', font=('Arial Bold', 10),command=lambda :self.onerecordStudent()).place(x=450, y=10)
        Button(windowA, text=" view Students ", fg='blue', font=('Arial Bold', 10),command=lambda :self.viewStudents()).place(x=680, y=10)
        Button(windowA, text=" Log out ", fg='blue', font=('Arial Bold', 10),
               command=lambda: self.logout()).place(x=10, y=450)

        windowA.mainloop()
        #logout
    def logout(self):
        windowA.destroy()
        LoginAdmin.AdminPageL().__init__()

    #show Attendance
    def viewAttendance(self):
        global  frameva
        if self.countlb==1:
            framelv.destroy()
            self.countlb =0

        if self.countVS==1:
            framevs.destroy()
            self.countVS =0

        if self.countSr == 1:
            framers.destroy()
            self.countSr =0

        if self.countVA==1:
            frameva.destroy()
            self.countVA =0

        self.countVA = 1
        k = DataBase.Data()
        list = k.showAttendance()
        frameva = Frame(windowA)
        frameva.place(x=200, y=100)
        # Table heading
        Label(frameva, text=" User name ", font=('Arial', 10, 'bold')).grid(row=0, column=0)
        Label(frameva, text=" Name ", font=('Arial', 10, 'bold')).grid(row=0, column=1)
        Label(frameva, text=" Attendance ", font=('Arial', 10, 'bold')).grid(row=0, column=2)
        Label(frameva, text=" Date ", font=('Arial', 10, 'bold')).grid(row=0, column=3)
        Label(frameva, text=" Description ", font=('Arial', 10, 'bold')).grid(row=0, column=4)

        i = 1
        for list1 in list:
            for j in range(len(list1)):
                self.e = Label(frameva, fg='blue', text=list1[j], font=('Arial', 10, 'bold'), ).grid(row=i, column=j)
            i += 1
    #show leave table
    def Approvalleave(self):
        if self.countVA==1:
            self.countVA =0
            frameva.destroy()
        if self.countVS==1:
            self.countVS =0
            framevs.destroy()
        if self.countSr==1:
            self.countSr =0
            framers.destroy()


        self.countlb=1
        k = DataBase.Data()
        list = k.showleavetoAdmin()
        global framelv
        framelv = Frame(windowA)
        framelv.place(x=200, y=100)
        # Table heading
        Label(framelv, text=" User name ", font=('Arial', 10, 'bold')).grid(row=0, column=0)
        Label(framelv, text=" Name ", font=('Arial', 10, 'bold')).grid(row=0, column=1)
        Label(framelv, text=" Date ", font=('Arial', 10, 'bold')).grid(row=0, column=2)
        Label(framelv, text=" Description ", font=('Arial', 10, 'bold')).grid(row=0, column=3)
        Label(framelv, text=" Decision ", font=('Arial', 10, 'bold')).grid(row=0, column=4)
        Label(framelv, text=" TAke Decision ", font=('Arial', 10, 'bold')).grid(row=0, column=5)




        i = 1
        for list1 in list:
            for j in range(len(list1)):
                self.e = Label(framelv, fg='blue', text=list1[j], font=('Arial', 10, 'bold'), ).grid(row=i, column=j)
            options = ["Leave", "Absent", ]
            clicked = StringVar(framelv)
            clicked.set(options[0])
            drop = OptionMenu(framelv, clicked, *options)
            drop.grid(row=i, column=4)
            self.e = Button(framelv, fg='blue', text="Decision", font=('Arial', 10, 'bold'),command= lambda u=list1[0]:self.takeDecisionLeave(u,list1[1],list1[2],list1[3],clicked.get())).grid(row=i, column=5)
            i += 1
        i=1
    def takeDecisionLeave(self,username,name,dates,descp,Desisions):
        print(username,name,dates,descp)
        k=DataBase.Data()
        k=k.leaveDecisions(username,name,Desisions,dates,descp)
        self.Approvalleave()
        tkinter.messagebox.showinfo("Decision is taken",Desisions)
    #create recods
    def onerecordStudent(self):
        global framers
        if self.countlb == 1:
            self.countlb =0
            framelv.destroy()
        if self.countVA == 1:
            self.countVA =0
            frameva.destroy()
        if self.countVS == 1:
            self.countVS =0
            framevs.destroy()


        self.countSr=1

        framers = Frame(windowA)
        framers.place(x=200, y=100)
        # Table heading
        Label(framers, text=" Create Reports ", fg='blue',font=('Arial', 10, 'bold'),).grid(row=0, column=0,)
        Label(framers, text=" Entery user name of Student ", font=('Arial', 10, 'bold'), ).grid(row=1, column=0)
        username=StringVar()
        Entry(framers, textvariable=username, font=('Arial', 10, 'bold'), ).grid(row=2, column=0)
        Button(framers, text="Create Report", font=('Arial', 10, 'bold'),fg='blue',command=lambda :countAttendance(username.get())).grid(row=7, column=0)
        def countAttendance(username):
            if username!="":
                k=DataBase.Data()
                k=k.countAttendanceCR(username)
                Label(framers, text=" Total present =  "+str(k[0]), font=('Arial', 10, 'bold')).grid(row=3, column=0)
                Label(framers, text=" Total Absent =  " + str(k[1]), font=('Arial', 10, 'bold')).grid(row=4, column=0)
                Label(framers, text=" Total Leave =  " + str(k[2]), font=('Arial', 10, 'bold')).grid(row=5, column=0)
                if k[0]>26:
                    Label(framers, text=" A grade  ", font=('Arial', 10, 'bold')).grid(row=6, column=0)
                elif k[0]>20 and k[0]<26:
                    Label(framers, text=" B grade  " , font=('Arial', 10, 'bold')).grid(row=6, column=0)
                elif k[0]>15 and k[0]<20:
                     Label(framers, text=" C grade  " , font=('Arial', 10, 'bold')).grid(row=6, column=0)
                elif k[0]>5 and k[0]<15:
                     Label(framers, text=" D grade  " , font=('Arial', 10, 'bold')).grid(row=6, column=0)
                else:
                   Label(framers, text=" F grade  ", font=('Arial', 10, 'bold')).grid(row=6, column=0)
            else:
                tkinter.messagebox.showinfo("Enter username","Please Enter a username")
        print("onerecordStudent")

        #view all students
    def viewStudents(self):
        if self.countlb==1:
            self.countlb =0
            framelv.destroy()
        if self.countVA==1:
            self.countVA =0
            frameva.destroy()
        if self.countSr == 1:
            self.countSr =0
            framers.destroy()

        self.countVS=1
        k = DataBase.Data()
        list = k.viewallStudent()
        global framevs
        framevs = Frame(windowA)
        framevs.place(x=100, y=100)
        # Table heading
        Label(framevs, text=" User name ", font=('Arial', 10, 'bold'),width=20).grid(row=0, column=0)
        Label(framevs, text=" Name ", font=('Arial', 10, 'bold'),width=20).grid(row=0, column=1)
        Label(framevs, text=" Email ", font=('Arial', 10, 'bold'),width=20).grid(row=0, column=2)
        Label(framevs, text=" Contact No ", font=('Arial', 10, 'bold'),width=20).grid(row=0, column=3)
        Label(framevs, text=" Delete ", font=('Arial', 10, 'bold'), width=20).grid(row=0, column=4)

        i = 1
        for list1 in list:
            for j in range(len(list1)):
                self.e = Label(framevs, fg='blue', text=list1[j], font=('Arial', 10, 'bold'),width=20 ).grid(row=i, column=j)
                Button(framevs, fg='blue', text="Delete", font=('Arial', 10, 'bold'),
                       command=lambda u=list1[0]: self.DeleteStudent(u)).grid(row=i, column=4)
            i += 1
        i=0
    def DeleteStudent(self,username):
        respose=tkinter.messagebox.askquestion("Delete",message="Are you sure to Delete the student")
        print(respose)
        if respose=="yes":
            k = DataBase.Data()
            k = k.DeleteStudentsB(username)
