#Class Variable
#class Student:
 #   College="GU" #Class Variable
  #  def __init__(self,name):
   #     self.name=name #Instance Variable
#
 #   def display(self):
  #      """Return the student's name and college."""
   #     return f"{self.name} studies at {self.College}"


#s1=Student("Uttam")
#s2=Student("Munna")
#print(s1.name)
#print(s2.name)
#print(s1.College)
#print(s2.College)


#Class Variable
#class Student:
 # def change_college(cls,new_college):
  #      cls.college=new_college
   #print(Student.college)


#class Car:
    #company = "Toyota"

    #@classmethod
    #def show_company(cls):
        #print(cls.company)


#Car.show_company()


#Static Method?
# Static method=Aisa method jo class ke andar hota hai,but self ya cls ki zaruat nahi hoti
#iske liye @staticmethod use karte he
#class Calculator:
    #@staticmethod
    #def add(a,b):
        #return a+b

#print(Calculator.add(10,20))

#Life example
#class Calculator:
 #   @staticmethod
  #  def square(n):
   #     return n*n

#print(Calculator.square(5))


#Q1.Program-Student
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def introduce(self):
        print("My name is", self.name)
        print("My age is",self.age)

s1=Student("Uttam",18)
s1.introduce()

#Program2-Inheritance
class Vehicle:
    def start(self):
        print("Vehical starts")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

c = Car()
c.start()
c.drive()


#Program3o