def add():
    l=[]
    n=int(input("total no.ofelem.s= "))
    i=1
    while i<=n:
        a=int(input("enter a elem.= "))
        if a%2==0:
           l.append(a)
           i=i+1
    print(l)

def removeven():
    l=input("Enter a list: ")
    l=[]
    for i in l:
        if i%2==0:
           l.remove(i)
    print(l)

def linear():           
    l=input("Enter a list: ")
    l=[]
    n=int(input("enter a no."))
    f=False
    p=0
    while p <len(l) and not f:
         if l[p]==n:
             f= True
             p=p+1
    if f:
        print(n,"is present at position ",p-1)
    else:
        print(n,"is not present")

def freq():
    l=input("Enter a list: ")
    l=[]
    l1=[]
    l2=[]
    for i in l:
        if i not in l2:
           x=l.count(i)
           l1.append(x)
           l2.append(i)
    print("elem.",",","\t\t","freq.")
    for i in range (len(l1)):
        print(l2[i],"\t\t\t",l1[i])
#Menu
while True:
   print("1.Adding elem.s in the list")             
   print("2.To remove all even no.") 
   print("3.Freq. of all elem.")
   print("4.Linear Search")
   print("5.Exit")
   c=int(input("Enter the choice: "))             
   if c==1:
      add()
   elif c==2:
       removeven()
   elif c==3:
       freq()
   elif c==4:
       linear()
   elif c==5:
      break
   else:
       print('''Incorrect Choice!
                 Enter Ur Choice AGAIN... ''')
'''
1.Addingelem.s in the list
2.To remove all even no.
3.Freq. of all elem.
4.Linear Search
5.Exit
Enter the choice: 1
totalno.ofelem.s= 2
enter a elem.= 4
[4]
enter a elem.= 6
[4, 6]
1.Addingelem.s in the list
2.To remove all even no.
3.Freq. of all elem.
4.Linear Search
5.Exit
Enter the choice: 2
[7, 5, 12, 23, 15, 10]
[7, 5, 23, 15, 10]
[7, 5, 23, 15]
1.Addingelem.s in the list
2.To remove all even no.
3.Freq. of all elem.
4.Linear Search
5.Exit
Enter the choice: 3
elem. ,          freq.
3            2
21           2
5            1
6            2
8            1
1.Addingelem.s in the list
2.To remove all even no.
3.Freq. of all elem.
4.Linear Search
5.Exit
Enter the choice: 4
enter a no.10
10 is present at position  0
1.Addingelem.s in the list
2.To remove all even no.
3.Freq. of all elem.
4.Linear Search
5.Exit
Enter the choice: 8
Incorrect Choice!
                 Enter Ur Choice AGAIN... 
1.Addingelem.s in the list
2.To remove all even no.
3.Freq. of all elem.
4.Linear Search
5.Exit
Enter the choice: 5
'''
