print("Question1")
class Animal:
    def animal_attribute(self,name,legs,color):
        self.name = name
        self.legs = legs
        self.color = color
class Tiger(Animal):
    def display(self):
        print("ANIMAL NAME:",self.name)
        print("LEG COUNT:",self.legs)
        print("BODY COLOR:",self.color)
y = Tiger()
y.animal_attribute('Tiger',4,'Yellowish orange')
y.display()
print("*"*10)
print('\n')

print("Question2")      
'''class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print (a.f(), b.f())
print (a.g(), b.g())'''
#ANSWER IS A B
#          A B

print("Question3")
class Cop:
    def __init__(self,name,age,work,experience,designation):
        self.name =name
        self.age = age
        self.work = work
        self.experience = experience 
        self.designation = designation
    def add_details(self):
        self.name =input("enter name:")
        self.age = int(input("enter age:"))
        self.work = input("enter work:")
        self.experience = input("enter experience:")
        self.designation = input("enter designation:")
    def display_detail(self):
        print("COP NAME:",self.name)
        print("COP AGE:",self.age)
        print("WORK:",self.work)
        print("EXPERIENCE:",self.experience)
        print("DESIGNATION:",self.designation)
    def update_details(self):
        self.name =input("enter name:")
        self.age = int(input("enter age:"))
        self.work = input("enter work1:")
        self.experience = input("enter experience:")
        self.designation = input("enter designation:")
class Mission(Cop):
    def add_mission_details(self):
        self.mission_name = input("enter mission name:")
        self.mission_year = int(input("enter mission year:"))
    def display_mdetail(self):
        print("Mission Details:")
        print( "MISSION NAME:",self.mission_name)
        print("MISSION YEAR:",self.mission_year)
c1 = Cop('rohit',34,'senior',3,'chief')
c1.display_detail()
print("\n")
print("mission class")
y1 = Mission('rohit',34,'senior',3,'chief')
y1.display_detail()
print("\n")
y1.add_mission_details()
print("\n")
y1.display_mdetail()
print("*"*10)
print('\n')

print("Question4")
class Shape:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def Area(self):
        if(self.length == self.breadth):
            return(self.length*self.length)
        else :
            return(self.length*self.breadth)
class Rectangle(Shape):
    def display_rarea(self):
        print("AREA OF RECTANGLE:",self.Area())
class Square(Shape):
    def display_sarea(self):
        print("AREA OF SQUARE:",self.Area())
#a1 = Shape(2,1)
b1 = Rectangle(2,5)
b1.Area()
b1.display_rarea()
c1 = Square(5,5)
c1.Area()
c1.display_sarea()
print("*"*10)
