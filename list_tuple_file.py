#list are ordered collection of hetrogenoue elements this are mutable and represent by []
# create a list ask user to give input and take list elemets from usee and find max min of list and perform other operatio
size=int(input("enter numer  u want to enter in list "))
l=[]
for i in range(size):
    x=int(input("enter your list element >> "))
    l.append(x)

print(l)

print(max(l))
print(min(l))

#### sort list and reverse it 
l.sort()
print(l)
l.reverse()
print(l)

l.insert(3,10000)

k=l.pop()
print(k)

l.remove(50)
print(l)


print(l.count(50))



### craete a list of color and craete a guess if u find color program will end or if not find color should print color not found in list 

color=['red',"white",'black','yellow','green','purple','blue','pink']
cl=input('please enter color of your choice >> ')
count=0

for col in color:
    if col==cl:
        print(f"color {col} found on index  {count}")
        break
    count +=1

else :
    print(f'{cl} color not found in list ')

print(type(color),len(color))

#list methods 
color.append("brown")
color.extend(['golden','silver','margenta'])
print(color)

## write a program using list comprehension to print square of list
nums=[i for i in range(1,6)]
print(nums)
sq=[i*i for i in range(1,6)]
print(sq)
n=int(input('enter a number >> '))
tab=[n*i for i in range(1,6)]
print(tab)

t=tuple(['r', 'w', 'b', 'y', 'g', 'p', 'b', 'p', 'b', 'g', 's', 'm'])
print(t.count('p'))
print(t.index('w'))