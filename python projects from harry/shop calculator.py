'''Writea python program which willkeep adding a stream of
numbers inputed by the user. the adding stops as soon as
user presses q key on the keyboard.'''

sum=0
while(True):
    userInput = input("Enter the item price or press q to quit: \n")
    if(userInput!='q'):
        sum=sum + int(userInput)
        print(f"Order total so far: {sum}")

    else:
        print(f"Your Bill total is {sum}. Thanks for shopping with us!...")
        break
#receipt printer
'''

Enter the item price or press q to quit: 
23
Order total so far: 23
Enter the item price or press q to quit: 
123
Order total so far: 146
Enter the item price or press q to quit: 
1234
Order total so far: 1380
Enter the item price or press q to quit: 
12345
Order total so far: 13725
Enter the item price or press q to quit: 
q
Your Bill total is 13725. Thanks for shopping with us!...
'''
