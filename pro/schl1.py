import mysql.connector

myconn=mysql.connector.connect(host="localhost",user="root",passwd=" ",database="test")

def creatab():
 cur=myconn.cursor()
 a='create table if not exists project(roll int, name varchar(20),gender char(1),section char(1),class varchar(4),stream varchar(10),fname varchar(20))'
 print('Table created if not exists')
 cur.execute(a)
 cur.close()

def showtab():
 cur=myconn.cursor()
 cur.execute('show tables')
 for i in cur:
     print(i)
 cur.close()

def insrec():
 cur=myconn.cursor()
 c='Y'
 while c=='Y':
     r=int(input('enter rollno: '))
     n=input('enter name: ')
     g=input("enter gender: ")
     sec=input("enter section : ")
     c=input("enter class : ")
     s=input("enter stream : ")
     fname=input("enter fname : ")
     value=(r,n,g,sec,c,s,fname)
     a='insert into project values(%s,%s,%s,%s,%s,%s,%s)'
     cur.execute(a,value)
     myconn.commit()
     c=input('Do u want to add more records(Y/N):').upper()
 cur.close()

def showrec():
 cur=myconn.cursor()
 cur.execute('select * from project')
 rec=cur.fetchall()
 print('Rollno',' ','Name',' ','gender',' ','section',' ','class',' ','stream',' ','fname')
 for r in rec:
     print(r[0],' ',r[1],' ',r[2],' ',r[3],' ',r[4],' ',r[5],' ',r[6])

def delerec():
 r=int(input('enter rollno to delete :'))
 value=r,
 cur=myconn.cursor()
 a='delete from project where roll=%s'
 cur.execute(a,value)
 if cur.rowcount>=1:
     myconn.commit()
     print('Total records deleted',cur.rowcount)
 else:
     print('not found')
 cur.close()
 
def search1():
 r=int(input('enter rollno to search :'))
 value=r,
 cur=myconn.cursor()
 a='Select * from project where roll=%s'
 cur.execute(a,value)
 rec=cur.fetchone()
 if cur.rowcount==1:
     print('Rollno',' ','Name',' ','gender',' ','section',' ','class',' ','stream',' ','fname')
     print(rec[0],' ',rec[1],' ',rec[2],' ',rec[3],' ',rec[4],' ',rec[5],' ',rec[6])
 else:
     print('record not found')

def search2():
 s=input("enter stream : ")
 value=s,
 cur=myconn.cursor()
 a='Select * from project where stream=%s'
 cur.execute(a,value)
 rec=cur.fetchone()
 if cur.rowcount==1:
     print('Rollno',' ','Name',' ','gender',' ','section',' ','class',' ','stream',' ','fname')
     print(rec[0],' ',rec[1],' ',rec[2],' ',rec[3],' ',rec[4],' ',rec[5],' ',rec[6])
 else:
     print('record not found')

def search3():
 g=input("enter gender: ")
 value=g,
 cur=myconn.cursor()
 a='Select * from project where gender=%s'
 cur.execute(a,value)
 rec=cur.fetchone()
 if cur.rowcount==1:
     print('Rollno',' ','Name',' ','gender',' ','section',' ','class',' ','stream',' ','fname')
     print(rec[0],' ',rec[1],' ',rec[2],' ',rec[3],' ',rec[4],' ',rec[5],' ',rec[6])
 else:
     print('record not found')

def modirec():
 r=input('enter rollno to modify :')
 value=r,
 cur=myconn.cursor()
 a="Select * from project where roll=%s"
 cur.execute(a,value)
 rec=cur.fetchone()
 if cur.rowcount==1:
     print('Rollno',' ','Name',' ','gender',' ','section',' ','class',' ','stream',' ','fname')
     print(rec[0],'\t',rec[1],'\t',rec[2],'\t',rec[3],'\t',rec[4],'\t',rec[5],'\t',rec[6])
     n=input('enter new name')
     g=input("enter new gender: ")
     sec=input("enter new section : ")
     c=input("enter new class : ")
     s=input("enter new stream : ")
     fname=input("enter new fname : ")
     value=n,g,sec,c,s,fname,r
     a='update project set name=%s where roll=%s'
     cur.execute(a,value)
     print('record modified')
 else:
     print('record not found')
     cur.close()
print(''' SHAHEED BISHAN SINGH MEMORIAL SR. SEC. SCHOOL
 *** WELCOME
TO SCHOOL MANAGEMENT***
 1. Create table
6. Search by streamwise
 2. Show Tables
7. search by genderwise
 3. Insert record
8. Delete records
 4. Show records
9. Modify records
 5. Search by rollnowise
10. Exit
''')
ch='Y'
while ch=='Y':
 print('1.Create table')
 print('2.Show Tables')
 print('3.insert record')
 print('4.show records')
 print("5.search record by rollnowise")
 print("6.search record by streamwise")
 print("7.search record by genderwise")
 print('8.delete records')
 print('9.Modify records')
 print('10 Exit')
 ch=int(input('enter your choice :'))
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
 ch=input('continue Y/N :').upper() 
