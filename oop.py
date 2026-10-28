# class Car:
#     print("hello how are you")

class Car:
    a = 12  # attribute

    def hello():  # method
        print("how are you")
        # you can access attributes and methods after accessing the class
        print(Car.a)


Car.hello()