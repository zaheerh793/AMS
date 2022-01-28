import StudentsPage
import pyodbc
from tkinter import filedialog
from PIL import ImageTk, Image
import os


class Data:
    def __init__(self):
        conn_str = (
            r'DRIVER={SQL Server};'
            r'SERVER=DESKTOP-FVO55IN;'
            r'DATABASE=AMS;'
            r'Trusted_Connection=yes;'
        )
        global cnxn
        cnxn = pyodbc.connect(conn_str)
        global cursor
        cursor=cnxn.cursor()
        cnxn.commit()

    def Registrations1(self,un,n,e,cn,p,image):
        print(image)
        self.__init__()
        cursor.execute('''insert into Student(username,NAMES,Email,contactNo,passwords)values(?,?,?,?,?)''',(un,n,e,cn,p))
        print(image,"zaheer RE")
        cursor.execute("update Student set img='" + image + "'WHERE username=?",(un))
        cnxn.commit()
    def ckdbu(self, username):
        count = True
        self.__init__()
        cursor.execute("select username from Student")
        records = cursor.fetchall()
        for row in records:
            if row[0] == username:
                count = False
                break
        cnxn.commit()
        return count
    #Sreach the Student and pass the profile data
    def SreachS(self,username):
        count=False
        self.__init__()
        cursor.execute("select username from Student")
        records = cursor.fetchall()
        for row in records:
            if row[0] == username:
                count=True
                break
        if count==True:
            cursor.execute("select * from Student where username='zaheer55'")
            record = cursor.fetchall()
            for row in record:
                un=(row[0])
                name=(row[1])
                Email=(row[2])
                Contact=(row[3])
                Password=(row[4])
        StudentsPage.StudentView().__init__(un,name,Email,Contact,Password)

        cnxn.commit()
    #function images



    #for login Student
    def login(self,username,password):
     self.__init__()
     cursor.execute("select username,passwords from Student")
     records = cursor.fetchall()
     count=False
     for row in records:
       if row[0]==username and row[1]==password:
         count=True
         break
     cnxn.commit()
     return count

    def sharingTakeStudentData(self,username):
        self.__init__()
        cursor.execute("SELECT * FROM Student WHERE username=?", (username))
        records = cursor.fetchall()
        return records

    def showAttendanceS(self,username):
        self.__init__()
        cursor.execute("SELECT * FROM Attendance where username=?",(username))
        records = cursor.fetchall()
        print(len(records))
        return records
    def showAttendance(self):
        self.__init__()
        cursor.execute("SELECT * FROM Attendance")
        records = cursor.fetchall()
        print(len(records))
        return records
    def storeleaveA(self,username,name,date,description):
        print("leaveStoreA")
        leave="Leave"
        count=False
        if username!="" and name!="" and date!="":
            self.__init__()
            print("kj")
            cursor.execute("insert into leaveAttendance(username,name,date,description)values(?,?,?,?)",(username,name,date,description))
            cnxn.commit()
            count=True
        else:
            count=False
        return count

    #store the attendances
    def storeAttendance(self,username,name,attend,date,description):
        print(username,name,attend,date,description)
        count=False
        count2=False
        if username!="":
            print(username,"form database")
            self.__init__()
            cursor.execute("select username, date from Attendance ")
            records = cursor.fetchall()
            print(records)
            for row in records:
               if row[0]==username:
                   count2=False
                   break
               else:
                   count2=True
            if count2==False:
                for row1 in records:
                    if row1[1]==date:
                        count2=False
                        break
                    else:
                        count2=True
            cnxn.commit()

        if username!="" and name!="" and date!="" and count2==True:
            self.__init__()
            print("kj")
            cursor.execute("insert into Attendance(username,name,attendance,date,description)values(?,?,?,?,?)",(username,name,attend,date,description))
            cnxn.commit()
            count=True
        else:
            count=False
        return count

    def updateProfile(self,username,name,Email,contact,password):
        self.__init__()
        cursor.execute("update Student set NAMES='"+name+"',Email='"+Email+"',contactNo='"+contact+"',passwords='"+password+"' WHERE username=?",username)
        cursor.close()
        cnxn.commit()
    def uploadimageDS(self,username,image):
        print(image)
        self.__init__()
        cursor.execute(
            "update Student set img='" + image + "'WHERE username=?",username)
        cursor.close()
        cnxn.commit()
    def showleavetoAdmin(self):
        self.__init__()
        cursor.execute("select * from leaveAttendance")
        record=cursor.fetchall()
        cursor.close()
        cnxn.commit()
        return record
    def leaveDecisions(self,username,name,Decision,date,description):
        self.__init__()
        cursor.execute("DELETE FROM leaveAttendance WHERE username = '"+username+"' and name = '"+name+"' and date = '"+date+"' and description = '"+description+"';")
        cursor.execute("insert into Attendance(username,name,attendance,date,description)values(?,?,?,?,?)",(username, name, Decision, date, description))
        cursor.close()
        cnxn.commit()

    #show all Student to admin
    def viewallStudent(self):
        self.__init__()
        cursor.execute("select username,NAMES,Email,contactNo from Student")
        records=cursor.fetchall()
        cursor.close()
        cnxn.commit()
        return records
    def countAttendanceCR(self,username):
        countAbsent=0
        countPresent=0
        countLeave=0
        self.__init__()
        cursor.execute("select attendance from Attendance where username='" + username + "' and attendance='Absent'")
        recordAbsent = cursor.fetchall()
        countAbsent=len(recordAbsent)
        cursor.execute("select attendance from Attendance where username='"+username+"' and attendance='Present'")
        recordPresent=cursor.fetchall()
        countPresent=len(recordPresent)
        cursor.execute("select attendance from Attendance where username='" + username + "' and attendance='Leave'")
        recountLeave=cursor.fetchall()
        countLeave=len(recountLeave)
        list=[countPresent,countAbsent,countLeave]
        print(list)
        cursor.close()
        cnxn.commit()
        return list
    def DeleteStudentsB(self,username):
        print(username)
        cursor.execute("DELETE FROM Student WHERE username = '" + username + "'")
        cursor.close()
        cnxn.commit()
    def sharingupdateStudentData(self,username):
        self.__init__()
        cursor.execute("SELECT * FROM Student WHERE username=?", (username))
        records = cursor.fetchall()
        return records









