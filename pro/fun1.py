def accept(lt):
            n=int(input("enter no. of elem to be input: "))
            for i in range(n):
                l=int(input("enter the list item: "))
                lt.append(l)
            print(lt)

def linearsearch(lt):
       n=int(input("Enter the no. to be search: "))
       found=False
       pos=0
       while pos < (len(lt)) and not found:
           if lt[pos]==n :
              found=True
              pos+=1
       if found :
              print(n," is present at pos.",pos-1)
       else:
         print(n,"is not present at pos.")

def bubblesort(l):
    n=len(l)
    print("Orignal list:- ")
    for i in range(n-1):
                  for j in range(n-i-1):  
                          if l[j]>l[j+1]:
                             l[j],l[j+1] =l[j+1],l[j]
    print("List after sorting:- ",l)                         

def swap(l):
    x=int(len(l/2))
    for i in range(x):
        l[i],l[x+i]=l[x+i],l[i]
    print("Swap list:-",l)    
    
def display(item):
      print("My list content")
      for i in range(len(item)):
            print(item[i],end="\t")
l=[]
   
while True:
          print("1.Input elem. in list")             
          print("2.linear Search") 
          print("3.Bubble Sort")
          print("4.Display the list")
          print("5.swap the list")
          print("6.Exit")
          c=int(input("Enter the choice: "))             
          if c==1:
             accept(l)
          elif c==2:
             linearsearch(l)
          elif c==3:
               bubblesort(l)
          elif c==4:
              display(l)
          elif c==5:
              swap(l)    
          elif c==6:
             print("Operation done !!")
             break
          else:
              print("Incorrect option! Try Again... ")