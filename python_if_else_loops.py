# create program to take a number and give print table
def tab():
    n=int(input("please enter number table you want to print >> "))
    for i in range(1,11):
        print(f'{n}*{i}={n*i}')
    return "table printed "


#res=tab()
#print(res)

# print all patterns
for i in range(1,6):
    print(i*'*')


## print i in pattern
for i in range (1,6):
    for j in range(1,i+1):
        print(i,end =" ")
    print()

##create pattern 
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#create pattern
c=1
for i in range(1,6):
    for i  in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()


### fibbonaci series

a=0
b=1
n=int(input("enter number to print series >> "))
for i in range (n+1):
    c=a+b
    print(c , end =" ")
    
    a=b
    b=c


#find reverse of a number method 1
num=int(input("enter  a number >  "))
n1=num
rev=0
while num > 0:
    rem=num%10
    num=num//10
    rev=rev*10+rem
print(rev)


##### method 2
n2=str(n1)
print(int(n2[::-1]))


# print factorial of a number 
fact=1
for i in range(1,7):
    fact=fact*i
print(f'fact of number is {fact}')

## craete list comprehsnion 

x=[i for i in range(1,11) if i%2==0]
print(x)

msg="hey i live in indore today is beautiful day are u ohk "

x1=[ch for ch in msg if ch in 'aeiou']
print(x1)
from collections import Counter

print(Counter(x1))


# write  a program to print whether character is volwell or consetent 
for ch in msg:
    if ch in 'aeiou':
        print('v', end =' ')
    else:
        print('c',end=' ' )
print()


## take input of 6 subject from students and tell if students pass or fail 
mark={}
subjects=["hindi",'english','sanskrit','maths','science','so.science']
for sub in subjects:
    mark[sub]=int(input(f"enter marks of {sub} >> "))

print(mark)

total_marks =sum(mark.values())
avg=total_marks/len(subjects)
print(f"percent of studnet is {avg}")


# write a program to swap a number 
n1=int(input('enter a number > '))
n2=int(input('enter a number > '))

total=n1+n2
n1=total-n1
n2=total-n2
print(n1,n2)

#swap number 
n1,n2 =n2,n1
print(n1,n2)

import random
print(random.randint( 1,50))