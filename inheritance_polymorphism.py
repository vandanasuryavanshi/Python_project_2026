###here we are craeting super class or parent class family to understand inheritance base class or parent class
class Family ():
    def __init__(self,family_name,father ,mother,religion):
        self.family_name=family_name
        self.father=father
        self.mother=mother
        self.religion=religion
    
    def happy_family(self):
        print(f'we are {self.family_name } happy happy family  ')

kapoor=Family("Kapoor","Ram","Siya","Hindu")
Khan=Family("Khan","Asif","Arifa","Muslim")
Singh=Family("Singh",'Kuldeep',"roshanpreet",'sikh')


print(kapoor.happy_family())
print(Khan.father)

## creating child class or drived class from parent class

class Child(Family):
    def __init__(self,family_name,father,mother,religion,name,gender,age):
        super().__init__(family_name,father,mother,religion)
        self.name=name
        self.gender=gender
        self.age=age
    def study(self):
        print(f"{self.name}  {self.family_name} is son of mr {self.father} and mrs {self.mother}")



shyam=Child("verma","sohan","shikha","Hindu",'shyam',"male",14)

print(shyam.study())


## here we are createing multiple in inhertance 
#class 1 Animal class

class Animal():
    def __init__(self ,animal,food):
        self.animal=animal
        self.food=food


    def info(self):
        print(f"{self.animal} like to eat {self.food}")

    
class Pet():
    def __init__(self,owner):
        self.owner=owner

    def work(self):
        print(f"hey I am pet owener {self.owner} ")



class Dog(Animal,Pet):
    def __init__(self,animal,food,owner,color,language,name):
        Animal.__init__(self,animal,food)
        Pet.__init__(self,owner)
        self.color=color
        self.language=language
        self.name=name

    def speak(self):
        print(f"hey I am {self.name } a {self.animal}  I {self.language} and I eat {self.food} myowner is {self.owner }")



Tom=Dog('Dog','milk and bread',"herry",'brown','bark','Tom')

print(Tom.speak())

#when same methods work differently for different object non as 
#types of polymorphism as functional level polymorphism or opertor level polymorphism

## operational polymophism

print(6+6 ,"\n" "6"+"6")
print(4*4)
print("*"*4)

#funcational polymorphism
def mul(*arg):
    total=1
    for i in arg:
        total*=i
    return total


print(mul(5))
print(mul(2,5,4))


#### special methods underscore used in class as belwo 

class Book():
    def __init__(self,name,auther,pages):
        self.name=name
        self.auther=auther
        self.pages=pages

    def __str__(self):
        return f"{self.name} is created by {self.auther} have page {self.pages}"

b1=Book("book1",'a1',100)
print(b1)



#### classs challeng create a class account have two attributes owner and amount and two methods depsote and withdrwa

class Account ():
    transaction=0
    details=[]
    def __init__(self,owner,balanace):
        self.owenr =owner
        self.balance=balanace
    
    def deposit(self ,dep_amount):
        self.balance =self.balance+dep_amount
        Account.transaction+=1
        res= f"your have deposite {dep_amount} rupees \n your total balance is {self.balance}"
        Account.details.append(res)
        return res
    
    def withdraw(self,wit_amount):

        if self.balance > wit_amount:
            self.balance=self.balance-wit_amount
            Account.transaction+=1
            res=f"your have withdraw {wit_amount} rupees \n your total balance is {self.balance}"
            Account.details.append(res)
            return res 
        else :
            print("insufficant balance ")
    
sam=Account("sam",30000)
print(sam.deposit(15000))
print(sam.withdraw(5000))