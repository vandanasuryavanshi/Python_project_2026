import random
# create car simmulator

running =False
stop =True
choice=" "

print("welcome in car rasing game ")
print("enter start to start the car \n enter stop to stop the car \n and help to get help ")

while choice != "QUIT" :
    choice=input(" >>>  ")


    if choice.upper()== "START"  and  stop and not running :
        print("your car has been started")
        stop = False ; running = True

    elif choice.upper()=="STOP" and running and not stop :
        print("your car has stopped ")
        stop= True ; running = False

    elif choice.upper() =="START" and running and not stop :
        print(".......oops......\n sorry \n your car is already running .......")
    elif choice.upper()=="STOP" and stop and not running :
        print(".......oops......\n sorry \n your car is already Stopped  .......")

    elif choice.upper() == "HELP"  :
        print("pls read below content \n Start  :-  To Start The car \n Stop :- To Stop The car  \n Quit :- To end the game \n Help :- to get the help")

    elif choice.upper() == "QUIT":
       ch1=input("do want to quit the game \n enter yes to quite and no to resume  \n > ")
       
       if ch1.upper()== "YES"  :
           print("your game has been quit .... \n Thank u for using ...")
           break
       elif ch1.upper() == "NO" :
           print("your game has been resumed \n .....Keep playing .......")
       else :
           
           print("pls enter correct input \n your game has been resumed")
        
    else :
        print("pls enter correct input")
