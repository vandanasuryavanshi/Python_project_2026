def zero_error():
    n=int(input('enter a value >>  '))
    b=int(input("enter a value >>  "))
    if b==0:
        try :
            n/b
        except ZeroDivisionError :
            print("you enter wrong input number cant be divided by zero ")

    else:
        print(n/b)
    return ""

print(zero_error())    

def add(n1,n2):
    try :
        c=n1+n2
        print(c)
    except TypeError :
        print("intiger cant add to string value ")

    finally:
        print (f"code run sucessfully ")

n1=10
n2="2"
print(add(n1,n2))
add(9,10)