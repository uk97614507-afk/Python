# The range() function
# Note: range(start, stop, step)
# ranges
# 10-100
print(list(range(10, 101, 10)))
# 0-45
print(list(range(0, 46, 5)))

range(46)
for i in range(46):
    print(i)

for i in range(5, 51, 5):
    print(i)

# input by the user
# table print 
n = int(input("please tell your number:-"))
for i in range(n, (n * 10) + 1, n):
    print(i)
    
    
    #For loop with strings
    a="Student" #or "STUDENT"
    for i in a:
        print(i)
        
        
        #or
        #for i in range(len(a)):
        #print(f"{i}:{a[1]}")
        
        
        
        
        
        
 