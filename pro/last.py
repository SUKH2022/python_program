import pickle as p

def create():
    data={}
    f1=open("product.dat","ab") #wb/ab
    while True:
        code=input("Enter product code: ")
        name=input("Enter product name: ")
        qty=int(input("Enter product quantity: "))
        price=float(input("Enter product price: "))
        data={"code":code,"name":name,"qty":qty,"price":price}
        p.dump(data,f1)
        ans=input("Enter Y/y to continue: ")
        if ans not in "Yy":
            break
    f1.close()

def display():
    data={}
    f1=open("product.dat","rb")
    print("%50s"%"PRODUCT DETAILS")
    print("%10s"%"CODE","%20s"%"NAME","%20s"%"RATE","%15s"%"VALUES")
    while True:
        try:
            data=p.load(f1)
            v=data["qty"]*data["price"]
            print("%10s"%data["code"],"%30s"%data["name"],"%20s"%data["qty"],"%20s"%data["price"])
        except EOFError:
            break
    f1.close()
    
def search():
    scode=input("Enter code to be searched: ")
    data={}
    f1=open("product.dat","rb")
    while True:
        try:
            data=p.load(f1)
            if data["code"]==scode:
                v=data["qty"]*data["price"]
                print("\tCODE: ",scode)
                print("\tNAME: ",data["name"])
                print("\tQUANTITY: ",data["qty"])
                print("\tRATE: ",data["price"])
                print("\tVALUE: ",v)
                break
        except EOFError:
            print('''RECORD NOT FOUND
                      TRY AGAIN!!...''')
    f1.close()
    
while True:
    print('1. Create the file')
    print('2. Display the file')
    print('2. Search')
    print("0. Exit.")
    c=int(input("Enter ur choice: "))
    if c==1:
        create()
    elif c==2:
        display()
    elif c==3:
        search()
    elif c==0:
         break
    else:
        print('''Incorrect Choice!
                 Enter Ur Choice AGAIN... ''')
    
'''
3/4
4d 4hr  20hr
1w doubt
12-15
1l20th
75000
88500
'''