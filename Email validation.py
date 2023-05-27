e=input("Enter ur email :- ")#g@g.in ,wscube@gmail.com
k,j,d=0,0,0
if len(e)>=6:#1
    if e[0].isalpha():#2
        if ("@" in e) and (e.count("@")==1):#3 #XOR Operator Bitwise xor operator: Returns 1 if one of the bits is 1 and the other is 0 else returns false.
           if (e[-4]==".") ^ (e[-3]=="."):#4 # Not in both position tt=f, FF=f,tf=t,ft=t
               for i in e:
                   if i==i.isspace():#5 #space contain
                       k=1
                   elif i.isalpha():#alphabet
                       if i==i.upper():#5 # Uppercase w--W==w, W--W==W
                           j=1
                   elif i.isdigit():# Digit avalible
                       continue
                   elif i=="_" or i=="." or i=="@":
                       continue
                   else:#5
                       d=1
                       
               if k==1 or j==1 or d==1:
                   print("5. Inaccurate Email address")
               else:
                   print("Accurate Email address")
           else:
               print("4. Inaccurate Email address")
        else:
            print("3. Inaccurate Email address")
    else:
        print("2. Inaccurate Email address")
else:
    print("1. Inaccurate Email address")
    
'''
Python 3.7.7 (bundled)
>>> %Run 'Email validation.py'
Enter ur email :- sukhpreet.saini2020@gmail.com
>>> %Run 'Email validation.py'
Enter ur email :- wcube
1. Inaccurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- 1wscube@gmail.com
2. Inaccurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- ws@cube@gmail.com
3. Inaccurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- wscube@gmail.p
4. Inaccurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- ws cube@gmail.com
5. Inaccurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- Wscube@gmail.com
5. Inaccurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- ws#cube@gmail.com
5. Inaccurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- ws_cube@gmail.com
>>> %Run 'Email validation.py'
Enter ur email :- ws_cube@gmail.com
Accurate Email address
>>> %Run 'Email validation.py'
Enter ur email :- ws.cube@gmail.com
Accurate Email address
'''