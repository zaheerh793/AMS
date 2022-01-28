from tkinter import *
import tkinter.messagebox
import DataBase
import LoginPage
from tkinter import filedialog
#class for registration

class Register:
	image = ""

	def __init__(self):
		global windowR
		windowR=Tk()
		windowR.title("Registration")
		windowR.minsize(width=1000,height=500)
		windowR.maxsize(width=1000,height=500)



		#registration form
		frame=Frame(windowR)
		frame.place(width=1000,height=500)
		Label(frame,text="Register here ",font=('Arial Bold',16)).place(x=450,y=10)

		Label(frame,text="First Name ",font=('Arial Bold',10)).place(x=200,y=50)
		Label(frame,text="Last Name ",font=('Arial Bold',10)).place(x=600,y=50)
		fn=StringVar()
		Entry(frame,font=('Arial Bold',10 ),width=30,textvariable=fn).place(x=200,y=80)
		ln=StringVar()
		Entry(frame,font=('Arial Bold',10 ),width=30,textvariable=ln).place(x=600,y=80)

		Label(frame,text="Contact No ",font=('Arial Bold',10)).place(x=200,y=110)
		Label(frame,text="Email Address",font=('Arial Bold',10)).place(x=600,y=110)
		cn=StringVar()
		Entry(frame,font=('Arial Bold',10 ),width=30,textvariable=cn).place(x=200,y=140)
		email=StringVar()
		Entry(frame,font=('Arial Bold',10 ),width=30,textvariable=email).place(x=600,y=140)

		Label(frame,text="UserName(must be unique )",font=('Arial Bold',10)).place(x=200,y=180)
		un=StringVar()
		Entry(frame,font=('Arial Bold',10,),width=30,textvariable=un).place(x=200,y=210)

		Label(frame,text="Password",font=('Arial Bold',10)).place(x=600,y=180)
		l=Label(frame,text="Confrom",font=('Arial Bold',10)).place(x=200,y=240)
		p=StringVar()
		Entry(frame,font=('Arial Bold',10 ,),width=30,textvariable=p,show="*").place(x=600,y=210)
		cp=StringVar()
		Entry(frame,font=('Arial Bold',10 ),width=30,textvariable=cp,show="*").place(x=200,y=270)

		Button(frame, font=('Arial Bold', 10),text="Select Image ",command=lambda :self.uploadimage()).place(x=600, y=270)



		Button(frame,text="  Register  ",font=('Arial Bold',16),command=
		   lambda  : self.Vilatiation(un,fn,ln,email,cn,p,cp,self.image)).place(x=450,y=300)
		v=StringVar()
		Button(frame,text="    Login   ",font=('Arial Bold',16),command=
		lambda  : self.login(v)).place(x=450,y=350)

		def uploadimage():
			image = filedialog.askopenfilename(title='open')
			Label(frame, text=image, font=('Arial Bold', 10)).place(x=700, y=280)
			print(image)



		windowR.mainloop()

	def uploadimage(self):
		self.image = filedialog.askopenfilename(title='open')
		Label(windowR, text=self.image, font=('Arial Bold', 10)).place(x=700, y=280)
		print(self.image)
	def login(self,l):
		windowR.destroy()
		k=LoginPage.mainwindow()
		k.__init__()
		print("")

	#Registration function

	def Vilatiation(self,username,firstname , lastname,Email,contactNo,password,confromPassword,image):
		print(self.image)
		if image!="":
			tkinter.messagebox.showinfo("Error","plz select Image")
		count=False
		em=0
		if username.get()!="" and firstname.get()!="" and contactNo.get()!="" and Email.get()!="" and password.get()!="" and lastname.get()!="":
			print(username.get())
			count =True
		if len(contactNo.get())==11:
			print(contactNo.get())
			em+=1
		if password.get()==confromPassword.get():
			print(password.get())
			em+=1
		k=DataBase.Data()
		k=k.ckdbu(username.get())

		if count==True and em==2 and k==True:
			print("zaheer")
			b=DataBase.Data()
			b.Registrations1(username.get(),firstname.get()+" "+lastname.get(),Email.get(),contactNo.get(),password.get(),image)
			tkinter.messagebox.showinfo("Registration", "Registration Successfully")
			count=False
			em=0
			print("hussain")
		else:
		  tkinter.messagebox.showinfo("Registration", "Invalite Data")



