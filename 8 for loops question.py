#1. Print "Heloo World"n times?
n=int(input("please tell your number:-"))
for i in range(n):
    print("Hello World")
    
#2.Print natural numbers from 1 to n?
n=int(input("please tell you number:-"))
for i in range(1,n+1):
    print(i)    
    
    
 #3.Reverse for loop -print n down to 1?
 
 
n=int(input("Please tell your number:-"))
for i in range(n,0,-1):
     print(i)
     
     
 #4. Print the multiplication table of a number?


n=int(input("Please tell your number:-"))
for i in range(1,11):
    print(f"{n}*{i} = {n*i}")    
    
    
#5.Sum of first n natural number?

sum_value = 0
n = int(input("till where you want your sum:-"))
for i in range(1, n + 1):
    sum_value += i

print(sum_value)



#6. Factorial of a number:
n = int(input("tell your number:-"))
f = 1
for i in range(1, n + 1):
    f = f * i
print(f)


#7.Print sum of all even odd numbers in a range separately?
n=int(input("please tell your number:-"))
oddsum=0
evensum=0
for i in range(1,n+1):
    if i%2==0:
        evensum += i
    else:
        oddsum += i
print(f"your even sum is {evensum} and odd sum is {oddsum}")
        


#8. Print all factors of a number?

n=int(input("tell your number:-"))
for i in range(1,n+1):
    if n%i==0:
        print(i)


#9. Check if a number is perfect (sum of factors = the number itself)

n = int(input("please tell your number:-"))
s = 0
for i in range(1, n):
    if n % i == 0:
        s += i

if s == n:
    print("perfect Number")
else:
    print("not a perfect number")     
    
    
 #10. check if a number is prime:
n = int(input("please tell your number:-"))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("prime number")
else:
    print("composite number")   
    
    
#11. reverse a string without using built in functions?
a="python"
print(a[::-1])    
#OR
#a="python"
#rev=""
#for i in range(len(a) -1,-1,-1):
#rev=rev+a[i]
#print(rev)



#12. Check if a string is a palindrome?

a = "python"
rev = ""
for i in range(len(a) - 1, -1, -1):
    rev = rev + a[i]

if rev == a:
    print("yes palindrome")
else:
    print("no not a palindrome")


#13. Count letters, digits, and special symbols in a string?
a = "P@#yn5"
letters = 0
digits = 0
special = 0

for ch in a:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print(f"letters = {letters}, digits = {digits}, special symbols = {special}")