# Function
# example
def hello():
    print("hello, welcome to Python!")
    print("welcome to UYC")

hello()
hello()
#Function ko kai bar call kr skte he


#Parameters & Arguments

#The variable name in the function definition. Like a placehlder.

#def greet (name): #parameter


def addition(a, b):
    print(a + b)


addition(67, 34)
addition(67, 35)



#greet("Alice")-argument
def palindrome_checker(a):
    copy = a
    rev = 0
    while a > 0:
        rev = rev * 10 + a % 10
        a = a // 10
    if copy == rev:
        print("palindrome number")
    else:
        print("not a palindrome")


palindrome_checker(121)
palindrome_checker(125)
palindrome_checker(121)
             
             
             
# positional argument

def addition(a, b, c=12):
    print(a + b + c)


addition(5, 5)
addition(5, 5, 7)             


# Keyword argument
def subtraction(a, b, c):
    print(b - a)


subtraction(20, c=40, b=34)
    
    