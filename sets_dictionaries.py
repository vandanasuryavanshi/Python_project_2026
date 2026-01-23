#set is unordered collection of unique values it is defined as {} curly brasis 
s1={1,1,2,2,3,3,3,4,4,4,4,4}
print(s1,type(s1))

s2={2,4,6,8}

### sets methods 
s1.add(5)
print(s1)
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
s3=s1.union(s2)
k=s3.pop()
print(k)

s3.remove(5)
print(s3)
s3.discard(9)
print(s3)

s1.update([6,7,8])
print(s1)


## Dictionaries are key value pair unordered collection of elemensts that is retrived by keys 
#create a dictioaries with fruits name and with valeus as its price \
fruits ={}
n=int(input('enter how many fruits you want to enter >> '))
for i in range(n):
    f=input('enter fruit name >> ')
    fruits[f]=int(input("enter price of fruit >>"))

print(fruits)

#### dictionaries comprehension

d={x:x*x for x in range(1,6)}
print(d)

## craete dictiories to count word
msg='hello world how are u will connect u soon'
m={}
for ch in msg:
    if ch in m:
        m[ch]+=1
    else:
        m[ch]=1

print(m)


# craete a program to find the length of word
msg=msg.split()
d2={word:len(word)for word in msg}
print(d2)

## craete a solution of given probelem 
data=[{'apple':5,"banana":7},{'banana' :3,'mango':4},{'garpes':12,"apple":2},{'mango':4,'papaya':7}]
new={}
for d in data :
    for k,v in d.items():
        if k in new:
            new[k]+=v
        else :
            new[k]=v

print(new)


# dictionaries operation 

print(new['mango'])

print(new.get('cherry','not found in dictionaries'))
new['cherry']=500

print(new)
print(new.keys())
print(new.values())
print(new.items())

