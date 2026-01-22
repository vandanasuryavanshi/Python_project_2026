# take input and print string
name =input("please enter your name >> ")
print(name, type(name))
print(len(name))

#all string methods 
print(name.upper())
print(name.lower())
print(name.title())
print(name.title().swapcase())
print("follow".count('o'))
print('follow'.find('l'))
print(name.split())
print("i love python".replace('python','Python'))
# write a program to reverse a string is 
name='vandana'
rev=name[::-1]
print(rev)


# write a program to reverse a string 
n="i like to read python programming books in evning ".split()
print(n)
n2=n[::-1]
print(n2)
n2=" ".join(n2)
print(n2)

# craete a funtion that take string and give 
from collections import Counter
s=input("please enetr a string >> ")
def frequecny_count(s):
    res=dict(Counter(s))
    return res

print(frequecny_count(s))
# creating program by logic 
test={}
for ch in s:
    if ch in test:
        test[ch]+=1


    else :
        test[ch]=1
    
print(test)


## craete a python program to find the longest word in string 
msg="i like to read python programming books in evning "
m=msg.split()
l={}
for word in m:
   l[word]=len(word)
print(l)
print(max(l,key=l.get))

#craete a python program to create a list 

data=[{'apple':5,"banana":7},{'banana' :3,'mango':4},{'garpes':12,"apple":2},{'mango':4,'papaya':7}]
new_dict={}
for d in data :
    for k,v in d.items():
        if k in new_dict:
            new_dict[k]+=v
        else :
            new_dict[k]=v

print(new_dict)
print(max(new_dict,key=new_dict.get))

# reemove all repeated words froma string 
word='aaaabbbbcccccdddddeeeeee'
s=''
for ch in word :
    if ch not in s:
        s +=ch

print(s)