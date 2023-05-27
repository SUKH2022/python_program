import random

max_num = 30

random_number = random.randint(1, max_num)
guess = 0
while guess != random_number:
    guess = int(input(f"Guess the number between 1 & {max_num}: "))
    if guess < random_number:
        print("Wrong! Too low...")
    elif guess > random_number:
        print("Wrong! Too high...")
print(f"Thats Right! Random number is {random_number}")

'''
Guess the number between 1 & 30: 15
Wrong! Too low...
Guess the number between 1 & 30: 1
Wrong! Too low...
Guess the number between 1 & 30: 16
Wrong! Too low...
Guess the number between 1 & 30: 30
Wrong! Too high...
Guess the number between 1 & 30: 20
Wrong! Too low...
Guess the number between 1 & 30: 25
Thats Right! Random number is 25         
'''