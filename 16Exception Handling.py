#Error vs Exceptions
#error(unfixable)     #Exceptions(handleable)
#   print("hello how are you"  - Syntax error
#a=12
#if a==12:
#  print ("hello") - bad spacing - Indentation error
#a=10
#b=0
#int(input("please tell a number:-"))
#print(a/b) 
#zeroDivision error


#a="10"
#b=5
#print(a+b)   - Type error

#num=int("hello")   - Value error


#Handling Exception
#try:
#    result = 10 / 0
#except ZeroDivisionError:
 #   print("Can't divide by the zero!")
#else:
 #   print("Succes:", result)
#finally:
 #   print("this always runs")

#a=int(input("please tell your 1st number:-"))
#b=int(input("please tell your 2nd number:-"))

#try:
 #   print(a/b)
#except Exception as err:
 #   print(f"Sorry an error occurred: {err}")
  #  name=input("tell your name:-")
   # print(f"hello your name is {name}")
#a = int(input("please tell your 1st number:-"))
#b = int(input("please tell your 2nd number:-"))

#try:
 #   print(a / b)
#except Exception as err:
 #   print(f"Sorry an error occurred as {err}")
#else:
 #   print("no errors occurred")
  #  name = input("tell your name:-")
   # print(f"Hello your name is {name}")
#finally:
 #   print("This always runs")             
#a= int(input("please tell your 1st number:-"))
#b = int(input("please tell your 2nd number:-"))


#try:
 #   print(a / b)
#except Exception as err:
 #   print(f"Sorry an error occured as {err}")
#finally:
 #   print("if there are errors or there are no errors I will run no matter what")
  #  name = input("tell your name:-")
  #  print(f"Hello your name is {name}")
  
  #Raise- manually throw your owb exception
  
age = int(input("tell your age:-"))
if age < 18:
    raise TypeError("you are not eligible")
print("you are eligible")
               
    
    
    
    
    
    