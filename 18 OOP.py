class Student:
  def study(self):
    print("Student is studying")

s2 = Student()
s2.study()
#Student -class
#s1-object
#study()-method
#s1.study()-Object ne method ko call kiya



#5. __init__() - Very important
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Now, create an instance and access its attributes outside the class definition
s1 = Student("Uttam", 18)
print(s1.name)
print(s1.age)



class Student:
  def study(self):
    print("I am studying")

# Create an instance outside the method
my_student = Student()
# Call the method on the instance
my_student.study()



#Complete example
class Student:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def study(self):
    print(self.name, "is studying")

# Create an instance of Student
s1 = Student("Uttam", 18)

# Access attributes and call methods
print(s1.name)
print(s1.age)
s1.study()





#1.-Current Object
class Student:
  def show(self):
    print("Hello")

# Create an instance of the Student class
s1 = Student()
# Call the show method on the instance
s1.show()
#s1-Object
#self-s1ko refer krt






#2. __init__()-Starting Data
class Student:
  def __init__(self):
    print("Student created")

# To see the __init__ method execute, create an instance of the Student class:
s1 = Student()





#self+__init__() Together ab dono ko ek sath dekho
class Student:
  def __init__(self,name):
    self.name=name

# Create an instance of the Student class outside the definition
s1 = Student("Uttam Kumar")
# Access and print the name attribute of the created instance
print(s1.name)






class Student:
  def __init__(self,name):
    self.name = name

# Create instances of the Student class outside the definition
s1 = Student("Uttam")
s2 = Student("Munna")

# Access and print the name attribute of the created instances
print(s1.name)
print(s2.name)







# 4.Instance Variable
class Student:
  def __init__(self,name,age):
    self.name = name
    self.age = age

# Create instances outside the class definition
s1 = Student("Uttam",18)
s2 = Student("Munna",18)

# Access and print attributes of the instances
print(s1.name)
print(s1.age)
print(s2.name)
print(s2.age)






# Simple example
class Animal:  # Corrected to uppercase 'A' for consistency and to match inheritance
  def eat(self):
    print("Animal is eating")

class Dog(Animal): # Dog inherits from Animal
  def bark(self):
    print("Dog is barking")

# Create an instance of Dog outside the class definitions
d = Dog()
d.eat() # Call the inherited method
d.bark() # Call the Dog's specific method






# 2. Parent+Child ko identify karo
class Animal:
  def eat(self):
    print("Eating")

class Dog(Animal): # Dog inherits from Animal, not nested
  def bark(self):
    print("Barking")

# Create an instance of Dog outside the class definitions
d = Dog()
d.eat() # Call the inherited method from Animal
d.bark() # Call the Dog's specific method






# Corrected inheritance with __init__()
class Animal:
  def __init__(self, name):
    self.name = name

  def eat(self):
    print(f"{self.name} is eating")

class Dog(Animal): # Dog inherits from Animal, defined at top level
  # Dog can have its own __init__ or use Animal's __init__
  # For now, let's explicitly call the parent's __init__
  def __init__(self, name, breed=None): # Added breed as an example
    super().__init__(name) # Call the parent Animal's __init__
    self.breed = breed # Add Dog-specific attribute

  def bark(self):
    print(f"{self.name} is barking") # Access self.name inherited from Animal

# Create instances and call methods outside the class definitions
animal_instance = Animal("Generic Animal")
animal_instance.eat()

my_dog = Dog("Buddy", "Golden Retriever") # Pass name and breed
my_dog.eat() # Inherited method
my_dog.bark() # Dog's specific method

print(f"{my_dog.name} is a {my_dog.breed}.")








# Method Overriding
class Animal:
  def sound(self):
    print("Animal makes sound")

class Dog(Animal): # Dog inherits from Animal, defined at the top level
  def sound(self): # Dog's own implementation of the sound method
    print("Dog barks")

# Create instances outside the class definitions
animal = Animal()
animal.sound() # Calls Animal's sound method

dog = Dog()
dog.sound()   # Calls Dog's overridden sound method






# Same method + child ka nya implementation = Overriding
class Vehicle:
  def start(self):
    print("Vehicle starts")

class Car(Vehicle): # Class name corrected to convention
  def start(self):
    print("Car starts with button") # This method overrides Vehicle's start

# Create instances outside the class definitions
v = Vehicle()
v.start() # Calls Vehicle's start method

c = Car() # Create a Car object
c.start() # Calls Car's overridden start method


# Polymorphism
# Polymorphism = Same method, different behaviour
# Different classes, same method

class Dog:
  def sound(self):
    print("Bark")

class Cat:
  def sound(self):
    print("Meow")

# Create instances
d=Dog()
c=Cat()
d.sound()
c.sound()


#Funtion Work for other Objects
class Dog:
  def sound(self):
    print("Bark")
class Cat:
  def sound(self):
    print("Meow")

def make_sound(animal):
  animal.sound()

d=Dog()
c=Cat()
make_sound(d)
make_sound(c)


#Encapsulation

#Basis Encapsulation
class Student:
  def __init__(self,name):
    self.name=name

  def show_name(self):
    print(self.name)

s=Student("Uttam")
s.show_name()

#Private variable
class Bank:
  def __init__(self):
    self.__balance=1000

  def show_balance(self):
    print(self.__balance)

b=Bank()
b.show_balance()




#Controlled Access
class Bank:
  def __init__(self):
    self._balance=1000

  def deposit(self,amount):
    self._balance+=amount

  def show_balance(self):
    print(self._balance)

b=Bank()
b.deposit(500)
b.show_balance()



#Abstraction
#simple example
class Car:
  def start(self):
    print("Car started")

  def drive(self):
    print("car is driving")

c = Car()
c.start()
c.drive()



#Actual abstruction
from abc import ABC, abstractmethod
class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass

class Dog(Animal):
  def sound(self):
    print("Bark")

d = Dog()
d.sound()
      