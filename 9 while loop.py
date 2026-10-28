#while True:
    #print("hello")
    #Non stop print 
    #stop-ctrl+c
    
    
    #Number Print
#a=1
#while True:
        #print(a)
        #a=a+1
     #Non stop number print
a=1
while a!=20:
         print(a)
         a=a+1   
#print that 1 to 19


count=1
while count<=5:
    print(count)
    count+=1
    #this is code print that for 1 to 5 no.



#Infinite loop year


#while loops also support
#Break
#Continue
#and 
#ELSE
#exactly like for loops



#1.Separate each digit of a number and print on a new line.
#a=123
#a=str(a)
#print(a[0])
#a=456
#print(a%10)
#a=a//10
#print(a%10)
#a=a//10
#print(a%10)
#a=a//10
#print(a)



#OR
a = int(input("please tell your number:-"))
while a>0:
    print(a%10)
    a = a//10
    
    
    
    
    #2#Accept a number and print its reverse?
    #a=int(inpt("please tell your number :-"))
    #rev=0
    #while a>0:
    #    print(a%10)
     #   a=a//10
     #this is wrong approch
     
     
    # Right approach
    a=int(input("please tell your number:-"))
    rev=0
    while a>0:
        rev=rev*10+a%10
        a=a//10
        print(rev)
      
      
      #3. check if  a number is palindromic (equal to reverse)
      
    a=int(input(("please tell your number:-")))
    copy=a
    rev=0
    while a>0:
        rev=rev*10+a%10
        a=a//10
        if rev == copy:
            print("palindrome")
        else:
            print("not a palindrome")
    