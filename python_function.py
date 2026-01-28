## function is block of code that can be defined once and can be used again later
#create a python basic python function 

def hello():
    print("Hello world \n how are u all \n definfig python fucntion")
    return 'Thanks'

print(hello())

# craete a function take a list of students name and print hello to all
#craete function to take name if students and give list 
def student_list(n):
    l=[]
    for i in range(n):
        name=input("enter student name >> ")
        l.append(name)
    return l

n=int(input('how many students you want to enter '))


l=student_list(n)
print(l)

def hello_new(l):
    for n in l:
        print(f"Hello {n} \n how are you \n doing great ?")

    return " "

print(hello_new(l))

new=[]

def first_ch(l):
    for i in l:
        new.append(i[0])
    
    return new

print(first_ch(l))

add=lambda a,b: a+b
print(add(9,5))

# craete a function will give even if number is even or odd if number is odd
x=[i for i in range(10)]
t=[]
def num_check(x):
    for i in x:
        if i%2==0:
            t.append(True)
        else:
            t.append(False)
    return  t

print(num_check(x))

## craete a list of tuple of product and price and again increase the price by 10%
d=[('apple',200),('samsung',300),('nokia',400),('lava',350)]
for pro,pri in d:
    pri=pri*1.1
    print(pri)

print(d)

def price_check(d):
    max_price=0
    product=''
    for pro , pri in d:
        if max_price < pri:
            product=pro
            max_price=pri
    
    return (max_price ,product)



print(price_check(d))

# create a guessing game
import random

def guess_number():
    number=[1,2,3]
    ch=random.choice(number)
    print(ch)
    count=0
    guess=""
    
    while count <3:
        guess=input('enter number between 1 to 3  >>')
        if int(guess)==ch:
            print('you won game ')
            break
        else :
            print("better luck try again")
        count+=1
    else :
        print("you lost the game thanks to use this game ")
    
print(guess_number())
def test(*args,**kwargs):
    print(f"I like {args[2]} and {kwargs['food']}")

print(test(1,2,3,4,5,food="samosa",veggie='paneer',fruit='apple'))