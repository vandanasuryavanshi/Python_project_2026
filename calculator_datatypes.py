

def calc():
    a=int(input("enter number 1 >> "))
    b=int(input("enter number 2 >> "))
    choice =int(input(" enter 1 for addition \n enter 2 for subraction \n enter 3 for multipilcation \n enter 4 for division \n enter 5 for mod or reminder   "))
    if choice == 1:
        print(f"sum of number {a+b}")
    elif choice == 2 :
        print(f"subraction of number {a-b}")
    elif choice == 3 :
        print(f"multiplication of number {a*b} ")
    elif choice == 4 :
        print(f"division of {a/b}")
    elif choice == 5 :
        print(f"modulous of {a%b}")
    elif choice == 6 :
        print(f"power of number {a**b}")
    else :
        print("please enter a valid choice ")

    
    return "thank u "

res =calc()
print(res)
