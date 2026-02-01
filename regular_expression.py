### regex is used for pattern matching or string matching that is used for extract any string or data and also for mail validation it has few rules as belwo 
# [abc]    -> a ,b or c | [^abc ] -> any charecter except a,b,c | [a - z] -> a to z | [A - Z] -> A to Z
#[a-z A - Z] -> a to z , A to Z | [0-9 ] -> 0 to 9 |
#--------------------------------------------------------------------------------------------------
#quntifirs explain quantities ['anything can be here '] ? -> 0 or 1 time |[""]+ -> 1 or more timea 
#[""]* means o or more time |[]{n} -> occures n times  |[]{n,} ->occures n or more number of time []{y,z} atleast y times less then z times
#------------------------------------------------------------------------------------------------4
#regex meta charcter (if dont want o use above big peterns we can use this belwo meta characters)
#\d ->[0-9] |\D ->[^0-9](non digit) |\w ->[a-z A-Z 0-9] |\W -> [^w] ### here this \ sign tell computer to serch given pattern 
#"\s" ->white space and "\S" -> non white space
#group or alteration (abc)-> group |   a|b -> either a or b

# question one check weather the given string in phone number on not 
#solution [89][0-9]{9}]

### all meta charetctor . means a new line ; ^ means start with  ;$ means end with 
string1="my phone number in is 1234567889 i am from banglore"
import re 
match=re.finditer(f'\d{10}',string1)
for m in match:
    print(f"my number is {m}")

#question 2 first character upper case ,contains lower case alphabet one one digit is alowed
#solution [A-Z][a-z]*[0-9][a-z]*

##create regex for email id 
#[a-z A-Z 0-9]+[^w][a-z]{5}[^w][a-z]{2,3}  #correct [a-z A-Z 0-9 _\-|.]+[@][]
import re

#here this r means raw string that will indicate string is taken as it is

test_string="123abc456789abc123ABC"
#pattern=re.compile(r"abc")
#matches=pattern.finditer(test_string)

matches=re.finditer(r"abc",test_string)

for match in matches:
    print(match)

## here in re we have methods called match(), search() and findall #finditer
# findall() method will give patterns find 
m1=re.findall(r'abc',test_string)

for m in m1:
    print(m)

#match method gives only results avaible at starting so we get non output beacuse abc was not in beginig 

m2=re.match(r'abc',test_string)
print(m2)
m3=re.match(r'123',test_string)
print(m2)


# now we will use search method and will run only index where it will find  the things as 
m4=re.search(r'abc',test_string)
print(m4)


### here we will use match method agin for use other mathod like group , span start ,end

pattern=re.compile(r'abc')
matches=pattern.finditer(test_string)
for match in matches:
    print(match.span()) ## it will give starting and ending index of string of respective sub string 
    print(match.end())
    print(match.start())
    print(match.group())

#there are some meta charcter that is having special meaning in regular expression as below
import re
text ="my phone number is 9876543210 i am from banglore"
print(re.findall(r'\d{10} ',text))
## here we will use sub 

print(re.sub(r"[a-z]{5}" ,"contact",text))

m_new=re.findall(r".",test_string)
for m in m_new:
    print(m)


m1=re.finditer(r"^123",test_string)
m2=re.finditer(r"ABC$",test_string)

for m in m1:
    print(m)

for m in m2:
    print(m)