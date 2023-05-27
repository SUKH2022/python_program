from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error=error+1
        except :
                error=error+1
        return error        

def speed_time(time_s,time_e,userinput):
    time_delay=time_e - time_s
    time_r= round(time_delay,2) #2- digit, round
    speed= len(userinput)/time_r
    return round(speed)

if __name__ == "__main__":
    while True:
        ck=input("Ready to test : Yes/No ::-")
        if  ck=="Yes":
            test=["A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.","my name is sukhpreet saini","welcome to my webpage, India"]
            test1 = r.choice(test)
            print("   *********Typing Speed***********")
            print(test1)
            print()
            print()
            time_1=time()
            testinput=input(" Enter :- ")
            time_2=time()
            
            print("Speed : ", speed_time(time_1,time_2,testinput),"w/sec")
            print("Error: ", mistake(test1,testinput))
        elif ck== "No":
            print("__________Thank You___________")
            break
        else:
            print("******Wrong Input*****")