#Check wheather a year is leap year.
year=int(input("Please enter a year:_"))
if(year%4==0):
    print("This is a leap year")
elif(year%100==0):
    print("Not leap year")
elif(year%400==0):
    print("This is a leap year")
else:
    print("Not leap year")
