import tkinter.messagebox
from tkinter import *
from datetime import date
import DataBase
import LoginPage
from PIL import ImageTk, Image
from tkinter import filedialog
import os

#Student profile class
from Tools.scripts.var_access_benchmark import A

class StudentView:
	def __int__(self,username,name,Email,Contact,Password,images):
		print(images)
		global window
		window=Tk()
		window.title("Attendance Management System ")
		window.minsize(width=1000, height=500)
		window.maxsize(width=1000, height=500)
	#Student profile setting
		x = images
		img = Image.open(x)
		img = img.resize((150, 150), Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		panel = Label(window, image=img)
		panel.image = img
		panel.place(x=0,y=0)
		Label(window, text="userName", font=('Arial Bold', 10)).place(x=30, y=190)
		Label(window, text=username, font=('Arial Bold', 10)).place(x=100, y=190)
		Label(window, text="Name", font=('Arial Bold', 10)).place(x=30, y=220)
		Label(window, text=name, font=('Arial Bold', 10)).place(x=100, y=220)
		Label(window, text="Email", font=('Arial Bold', 10)).place(x=30, y=250)
		Label(window, text=Email, font=('Arial Bold', 10)).place(x=100, y=250)
		Label(window, text="Contact", font=('Arial Bold', 10)).place(x=30, y=280)
		Label(window, text=Contact, font=('Arial Bold', 10)).place(x=100, y=280)
		Button(window, text="Edit your profile info", font=('Arial Bold', 12),command=lambda :self.EditProfile(username,name,Email,Contact,Password,images)).place(x=50, y=340)
		Button(window, text="Mark Attendance", font=('Arial Bold', 10),command=lambda :self.addAttendance(username,name)).place(x=460, y=50)
		Button(window, text="Mark leave", font=('Arial Bold', 10),command=lambda :self.LeaveMark(username,name)).place(x=600, y=50)
		Button(window, text="Mark View", font=('Arial Bold', 10),command=lambda :self.ViewAddentance(username)).place(x=700, y=50)
		Button(window, text="Log Out", font=('Arial Bold', 10), command=lambda: self.signout()).place(x=50, y=400)

		window.mainloop()

	def signout(self):
		window.destroy()
		k=LoginPage.mainwindow()
		k.__init__()


	def ViewAddentance(self,username):
		k=DataBase.Data()
		list=k.showAttendanceS(username)
		frameva=Frame(window)
		frameva.place(x=350,y=100)
		#Table heading
		Label(frameva, text=" User name ", font=('Arial', 10, 'bold')).grid(row=0,column=0)
		Label(frameva, text=" Name ", font=('Arial', 10, 'bold')).grid(row=0, column=1)
		Label(frameva, text=" Attendance ", font=('Arial', 10, 'bold')).grid(row=0, column=2)
		Label(frameva, text=" Date ", font=('Arial', 10, 'bold')).grid(row=0, column=3)
		Label(frameva, text=" Description ", font=('Arial', 10, 'bold')).grid(row=0, column=4)

		i=1
		for list1 in list:
			for j in range(len(list1)):
				self.e = Label(frameva, fg='blue', text=list1[j], font=('Arial', 10, 'bold'), ).grid(row=i,column=j)
			i+=1



	def LeaveMark(self,username,name):
		global framelm
		framelm = Tk()
		framelm.title("Mark Leave")
		framelm.minsize(width=500, height=350)
		framelm.maxsize(width=500, height=350)
		e=Label(framelm, width=10, fg='blue',text=" Mark Leave ",font=('Arial', 16, 'bold')).place(y=10,x=200)
		today = date.today()
		Label(framelm, text=" Date ", font=('Arial', 10, 'bold')).place(x=20, y=50)
		Label(framelm, text= today, font=('Arial', 10, 'bold')).place(x=100, y=50)

		Label(framelm, text=" UserName ", font=('Arial', 10, 'bold')).place(x=20, y=90)
		Label(framelm, text=username, font=('Arial', 10, 'bold')).place(x=100, y=90)

		Label(framelm, text=" Description ", font=('Arial', 10, 'bold')).place(x=20, y=130)
		un=StringVar(framelm)
		Entry(framelm, font=('Arial', 10, 'bold'),textvariable=un).place(x=20, y=170,height=100,width=200)
		Button(framelm,background='blue',text=" Add Leave ", font=('Arial', 10, 'bold'),command=lambda :self.leavedataStore(username,name,today,un)).place(x=200, y=290)

#LEAVE ATTENTANCE STORE ON DATABASE
	def leavedataStore(self,username,name,date,description):
		print(description.get())
		k=DataBase.Data()
		l=k.storeleaveA(username,name,str(date), description.get())
		print("after me")
		if l==True:
			tkinter.messagebox.showinfo("Leave Attendance","your request has been add ")
			framelm.destroy()
		else:
			tkinter.messagebox.showinfo("Leave Attendance", "Error plz try again")
			framelm.destroy()



	def addAttendance(self,username,name):
		global framelm
		framelm = Tk()
		framelm.title("Mark Attendance")
		framelm.minsize(width=500, height=350)
		framelm.maxsize(width=500, height=350)
		e=Label(framelm, width=10, fg='blue',text=" Mark Leave ",font=('Arial', 16, 'bold')).place(y=10,x=200)

		Label(framelm, text=" Date ", font=('Arial', 10, 'bold')).place(x=20, y=50)
		today = date.today()
		Label(framelm, text= today, font=('Arial', 10, 'bold')).place(x=100, y=50)

		Label(framelm, text=" UserName ", font=('Arial', 10, 'bold')).place(x=20, y=90)
		Label(framelm, text=username, font=('Arial', 10, 'bold')).place(x=100, y=90)

		Label(framelm, text=" Description ", font=('Arial', 10, 'bold')).place(x=20, y=130)
		des=StringVar(framelm)
		Entry(framelm, font=('Arial', 10, 'bold'),textvariable=des).place(x=20, y=170,height=100,width=200)
		#options
		options = ["Present","Absent",]
		clicked = StringVar(framelm)
		clicked.set(options[0])
		drop = OptionMenu(framelm, clicked, *options)
		drop.place(x=300, y=220)
		Label(framelm, text=" Select present or Absent ", font=('Arial', 10, 'bold')).place(x=300, y=180)
		Button(framelm,background='blue',text=" Add Attendance ", font=('Arial', 10, 'bold'),command=lambda :self.sendAttendance(username,name,clicked.get(),today,des.get())).place(x=200, y=290)
		framelm.mainloop()


	def sendAttendance(self,username,name,attend,date,description):
		print(username,name,attend,date,description)
		k = DataBase.Data()
		l = k.storeAttendance(username, name,attend, str(date), description)
		print("after me")
		if l == True:
			tkinter.messagebox.showinfo("Add Attendance", "your request has been add ")
			framelm.destroy()
		else:
			tkinter.messagebox.showinfo("Add Attendance", "Recrod  exist")
			framelm.destroy()


	def EditProfile(self,username,name,Email,Contact,Password,image):
		window.destroy()
		global framelme
		framelme = Tk()
		framelme.title("EditProfile")
		framelme.minsize(width=500, height=350)
		framelme.maxsize(width=500, height=350)
		Label(framelme, text="userName can't change", font=('Arial Bold', 10)).place(x=30, y=10)
		Label(framelme, text=username, font=('Arial Bold', 10)).place(x=30, y=40)
		Label(framelme, text="Name", font=('Arial Bold', 10)).place(x=30, y=70)
		name1=StringVar(framelme)
		Entry(framelme, textvariable=name1, font=('Arial Bold', 10)).place(x=30, y=100)
		Label(framelme, text="Email", font=('Arial Bold', 10)).place(x=30, y=130)
		Email1=StringVar(framelme)
		Entry(framelme, textvariable=Email1, font=('Arial Bold', 10)).place(x=30, y=160)
		Label(framelme, text="Contact No", font=('Arial Bold', 10)).place(x=30, y=190)
		contact=StringVar(framelme)
		Entry(framelme, textvariable=contact, font=('Arial Bold', 10)).place(x=30, y=210)
		Label(framelme, text="Password", font=('Arial Bold', 10)).place(x=30, y=240)
		password=StringVar(framelme)
		Entry(framelme, textvariable=password, font=('Arial Bold', 10),show="*").place(x=30, y=270)
		#adding images


		Button(framelme,text="update",font=('Arial Bold', 10),command=lambda :checking(username,name,Email,Contact,Password,image)).place(x=80, y=300)
		Button(framelme, text="Edit Image", font=('Arial Bold', 10),command=lambda :self.uploadimage(username)).place(x=250, y=300)

		def checking(username,name,Email,Contact,Password,image):
			print(username,name,Email,Contact,Password)
			if name1.get()!="":
				name=name1.get()
			if Email1.get()!="":
				Email=Email1.get()
			if contact.get()!="":
				Contact=contact.get()
			if password.get()!="":
				Password=password.get()
			self.editProfileStore(username,name,Email,Contact,Password,image)


	def editProfileStore(self,username,name,Email,contact,password,image):
		print(username, name, Email, contact, password)
		k=DataBase.Data()
		k.updateProfile(username,name,Email,contact , password)
		framelme.destroy()
		obj = StudentView()
		list=k.sharingupdateStudentData(username)
		for row in list:
			obj.__int__(row[0], row[1], row[2], row[3], row[4], row[5])

		print("Function editProfileStore")

	def uploadimage(self,username):
		filename = filedialog.askopenfilename(title='open')
		Label(framelme,text=filename,font=('Arial Bold',10)).place(x=250,y=280)
		k=DataBase.Data()
		k.uploadimageDS(username,filename)
		print("Functions uploadimage")




