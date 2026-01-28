#create a string take string from your check wheather starting and ending of string is same or not
def string_checker():
    msg=input("please enter a string >> ")
    if msg[0]==msg[-1]:
        print(True)
    else :
        print(False)

print(string_checker())

#create a function return smaller number if both number are even or one is even if both are odd give greater number 
def test1():
    n1=int(input(">> "))
    n2=int(input(">> "))
    if n1%2 ==1 and n2%2==1:
        print(max(n1,n2))
    else :
        print(min(n1,n2))


print(test1())

## predefined functions
sqr=lambda x:x*x
l=[i for i in range(1,6)]
m1=map(sqr,l)
for i in  m1:
    print(i)


#create a function take list of names if len of name is even print even or give first charater of list
name=['andy','eve','sally','ram','mohan','sita']
def len_checker(name):
    if len(name)%2==0:
        return 'EVEN'
    else:
        return name[0]
    

res=map(len_checker,name)
print(list(res))


## method two 
def test2(name):
    l1=[]
    for n in name :
        if len(n)%2==0:
            l1.append("even")
        else:
            l1.append(n[0])
    
    return l1
print(test2(name))

t1=lambda s: len(s)
print(t1("hello"))

### lambda function with conditon 
x=[i for i in range(1,11)]
check=lambda a:'even' if a%2==0 else 'odd'
l2=[]
for i in x:
    l2.append(check(i))
print(l2)

print(check(9))