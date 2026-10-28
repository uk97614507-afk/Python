#Check whether a person is eligible for vote?
person=input("Please tell your name:-")
age=int(input("Please tell your age:-"))
if(age>=18):
    print(f"Hello,{"person"} you are  eligible for vote")
else:
    print("You are not eligible for to vote")