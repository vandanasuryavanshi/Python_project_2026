# create a decorator function pass a main function and pass in  decorator 

def my_decortor(my_func):
    print("this is first line of decorator  ")
    print(my_func())
    print("this  is  last line of decorator")

    return "both functions executed "


@my_decortor
def my_func():
    print("hello this is main function")
    return "Thanks to use it "


## create a generotor # poit to remeber generotor dont work out of list
def num():
    n=1
    while n < 6:
        yield n
        n+=1


print(list(num()))


l=[1,2,3,4,5]
it=iter(l)
for i in range(len(l)):
    print(next(it))