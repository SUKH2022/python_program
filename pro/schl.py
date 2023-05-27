import mysql.connector as m
mydb=m.connect(host="localhost",user="root",passwd=" ",database="schl")

if mydb.is_connected()==False:
 print("Error connecting to MySQL database")
 
c=mydb.cursor()
               
def creatab():
    c=mydb.cursor()
    a="create  if not exists stuinfo(Rollno int not null primary key,Name varchar(20) not null,Gender char(1),Section char(1),Class int,Stream varchar(20),Fname varchar(30),DOB date)"
    print("Table created if not exists")
    c.execute(a)
    c.close()
    
def showtab():
 c=mydb.cursor()
 c.execute("show Tables")
 for i in c:
    print(i,"\n")   
 c.close()
 
def insrec():
 c=mydb.cursor()
 ch="Y"
 while ch=="Y":
     r=int(input("Enter Rollno: "))
     n=input("Enter Name: ")
     g=input("Enter Gender: ")
     sec=input("Enter Section: ")
     c=int(input("Enter Class: "))
     s=input("Enter Stream: ")
     Fname=input("Enter Fname: ")
     d=input("Enter DOB: ")
     q="insert into stuinfo values({},'{}','{}','{}',{},'{}','{}','{}')".format(r,n,g,sec,c,s,Fname,d)
     c.execute(q)
     mydb.commit()
     c=input("Do u want to add more Records(Y/N): ").upper()
 c.close()
 
def showrec():
 c=mydb.cursor()
 c.execute("select * from stuinfo")
 rec=c.fetchall()
 print("Rollnono"," ","Name"," ","Gender"," ","Section"," ","Class"," ","Stream"," ","Fname"," ","DOB")
 for r in rec:
       print(r[0]," ",r[1]," ",r[2]," ",r[3]," ",r[4]," ",r[5]," ",r[6]," ",r[7],"\n")

def delerec():
 r=int(input("Enter the Rollnono whose Record is to be deleted:" ))
 c.execute("delete from stuinfo where Rollnono=%s"%(r,))
 mydb.commit()
 print("All Records:- ")
 c.execute("select * from stuinfo")
 for x in c:
     print(x)
 c.close()
 
def search1():
 r=int(input("Enter Rollnono to search: "))
 c=mydb.cursor()
 c.execute("Select * from stuinfo where Rollnono={}".format(r))
 rec=c.fetchone()
 if c.rowcount==1:
       print("Rollnono"," ","Name"," ","Gender"," ","Section"," ","Class"," ","Stream"," ","Fname"," ","DOB")
       print(rec[0]," ",rec[1]," ",rec[2]," ",rec[3]," ",rec[4]," ",rec[5]," ",rec[6]," ",r[7],"\n")
 else:
       print("Record not found....")
       
def search2():
 s=input("Enter Stream: ")
 c=mydb.cursor()
 c.execute("Select * from stuinfo where Stream='{}'".format(s))
 rec=c.fetchone()
 if c.rowcount==1:
       print("Rollnono"," ","Name"," ","Gender"," ","Section"," ","Class"," ","Stream"," ","Fname"," ","DOB")
       print(rec[0]," ",rec[1]," ",rec[2]," ",rec[3]," ",rec[4]," ",rec[5]," ",rec[6]," ",r[7],"\n")
 else:
       print("Record not found....")
       
def search3():
 g=input("Enter Gender: ")
 c=mydb.cursor()
 c.execute("Select * from stuinfo where Gender='{}'".format(g))
 rec=c.fetchone()
 if c.rowcount==1:
       print("Rollnono"," ","Name"," ","Gender"," ","Section"," ","Class"," ","Stream"," ","Fname"," ","DOB")
       print(rec[0]," ",rec[1]," ",rec[2]," ",rec[3]," ",rec[4]," ",rec[5]," ",rec[6]," ",r[7],"\n")
 else:
       print("Record not found...")
       
def modirec():
 r=input("Enter Rollnono to modify: ")
 c=mydb.cursor()
 c.execute("Select * from stuinfo where Rollnono={}".format(r))
 rec=c.fetchone()
 if c.rowcount==1:
       print("Rollnono"," ","Name"," ","Gender"," ","Section"," ","Class"," ","Stream"," ","Fname"," ","DOB")
       print(rec[0],"\t",rec[1],"\t",rec[2],"\t",rec[3],"\t",rec[4],"\t",rec[5],"\t",rec[6]," ",r[7],"\n")
       n=input("Enter new Name: ")
       g=input("Enter new Gender: ")
       sec=input("Enter new Section: ")
       c=input("Enter new Class: ")
       s=input("Enter new Stream: ")
       Fname=input("Enter new Fname: ")
       d=input("Enter new DOB: ")
       a="update stuinfo set name='{}' where Rollnono={}".format(r,n,g,sec,c,s,Fname,d)
       c.execute()
       print("Record modified")
 else:
       print("Record not found")
       c.close()
       mydb.close()
print("""__________________WELCOME TO SCHOOL MANAGEMENT__________________""")
ch="Y"
while ch=="Y":
 print("1.Create Table")
 print("2.Show Tables")
 print("3.Insert Record")
 print("4.Show Records")
 print("5.Search Record by Rollnowise")
 print("6.Search Record by Streamwise")
 print("7.Search Record by Genderwise")
 print("8.Delete Records")
 print("9.Modify Records")
 print("10.Exit.")
 ch=int(input("Enter your choice: "))
 if ch==1:
    creatab()
 elif ch==2:
    showtab()
 elif ch==3:
    insrec()
 elif ch==4:
    showrec()
 elif ch==5:
    search1()
 elif ch==6:
    search2()
 elif ch==7:
    search3()
 elif ch==8:
    delerec()
 elif ch==9:
    modirec()
 elif ch==10:
     break
 else:
     print('''Incorrect Option!
        Try Again......''')
 ch=input("Do You Want To Continue(Y/N): ").upper() 
