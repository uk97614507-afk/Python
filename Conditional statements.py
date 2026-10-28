#making Decisions in Code
if True:
     print("hello how are you")
     if False:
         print("hello how are you")
         if 12==12:
             print("hello how are you")
             
 #You have to take input of age and tell the person can vote or not


age = int(input("please tell your age:-"))
if age >= 18:
    print("hello brother you can vote")
else:
    print("hello you can not vote sorry")
                
#Question2
rupees=int(input("give money-"))
if rupees==10:
         print("I will have a machine")
elif rupees==50:
             print("I will have a phone")
elif rupees==100:
             print("UYC")
elif rupees==500:
    print("5 star dhaba")  
else:
    print("comment")                        
         
         
         
#Q.1 Accept two numbers and print the greatest between them.
num1=int(input("please give me first number :-"))
num2=int(input("please give me second number:-"))
if num1>num2:
    print(f"{num1} is greater than {num2}")
elif num2>num1:
    print(f"{num2} is greater than {num1}")
else:
    print("both the numbers are equal")
    
    
    
#Q.2.accept gender from user and print a greeting message
gen = input("please tell your gender in (M or F): ")
if gen == "M" or gen=="m":
    print("hello sir")
elif gen == "F" or gen=="f":
    print("hello mam")
else:
    print("others")    
    
    
    
#Q.3.Accept an integer and check if it is even or odd
a=int(input("please tell your number:-"))
if a%2==0:
    print("even number")
else:
    print("the number is odd")         
    
    
#Q.4.Accept name and age-check if the user is a valid voter(+18)
name=input("please tell your name:-")
age=int(input("please tell your age:-"))
if age>=18:
    print(f"hello {name} you are a valid voter")
else:
    print(f"hello{name} you are not a valid voter")
    #print(f"hello {name} you can vote after {18-age}years")    
    
    
    
#Q.5.accept a year and check if it is a leap year
year=int(input("please tell your year:-"))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("not a leap year")    
    
    
    
    
    
    
    
    #Q.6.accept temperature in celcius and print a description
    temp=int(input("please tell your temperature:-"))
    if temp>=5 and temp<=5:
        print("very cold")
    elif temp>=6 and tem<=18:
        print("cold")
    elif temp>=19 and temp<=30:
        print("hot")
    else:
        print("very hot")