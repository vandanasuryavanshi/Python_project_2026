#object is single unit of class its real world entity while class is template or blueprint of object every class has atributed or property and behqvaior 
#opps concepts are class , object ,abstartion , inheritance , polymorphism ,encapsulation
#abstarction is technique to show only essential things to user and hiding other details
#encapsulation is process of binding all the data in single unit 
#inhertence meanse inherit the property of parent class into child class
#polymorphism means one name many work same class method will work differnt for differnt object .it means differnt class object can share same method name


#create a student class with some atrribute and create 1 method 

class Student():  # creating class
    def __init__(self ,id ,name, age , city , cls,):   # created constuructor its special methao craete atributes 
        self.id =id
        self.name=name
        self.age=age
        self.city=city
        self.cls=cls

     # created method or define behavior pf classs
    def study(self):
        print(f"{self.name} study in {self.cls} .\n liv in {self.city}")
        return ' '

# createing object of class   
ram=Student(101,"ram",12,'pune','5th')
siya=Student(102,"siya",11,'bombay','5th')

print(ram.study())

###we can also addd atribute to an object like below
ram.like="saomsa"
print(ram.like)



### here we are creating another human to understand class varible concept

class Human():
    #here we are defining a class varible called population so that will give me information how many instances are created
    population=0
    # creating one more varible that will have all list of humans creatd as below
    data=[]

    def __init__(self,name, age,hobby,alive=True):
        self.name=name
        self.age=age
        self.hobby=hobby
        self.alive=alive

        #here we will incremant class varibale population everytime a human object is created 
        Human.population+=1
        Human.data.append(self.name)

    def greet(self):
        print(f"hello everyone i am {self.name} ,\n Good morning !!! ")

    ## craeting one more method dead to understand how varible will update
    def dead(self):
        if self.alive:
            print(f"sorry {self.name} is no more ")
            Human.population-=1
            Human.data.remove(self.name)
            self.alive=False 
        else :

            print(f"{self.name } passed away ")


Mohan=Human("Mohan",25,'singing')
Riya=Human("Riya",28,"Dancing")
Shivm=Human("Shivam",24,'Cooking')
Bhoot=Human('Bhoot',79,'ghoting')

###here above we created  4 human object so 4 should be population as 4 time construcor executed and we can verify it as below
print(Human.population)
print(Human.data)
    
## calling method dead 
print(Bhoot.dead())


## calling method again to check codintion are working fine or not 
print(Bhoot.dead())


