class Animal:
    a = 12 #class attributes

    def __init__(self,name):
        self.name = name  #object/instance attribute

    def hello(self):
        print(f"how are you my name is {self.name}")

    @classmethod
    def details(self): #class method 
        print(f"how are you my name is {self.name}")
        obj = Animal("lion")
        obj.details()

         