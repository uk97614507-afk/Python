#Find the largest of three numbers?
num1=int(input("Please tell your first number:-"))
num2=int(input("Please tell your second number:-"))
num3=int(input("Please tell your third number:-"))
if num1 > num2 and num1 > num3:
    print("Number 1 is largest")
elif num2 >  num1 and num2 > num3:
    print("Number 2 is largest")
elif num3> num1 and num3> num2:
    print("Number 3 is largest")
else:
    print("Both are equal")