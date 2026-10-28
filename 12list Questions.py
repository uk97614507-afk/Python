#1.Print all positive and negative elements separately.
l=[3,-1,4,-5,9]
pos=[]
neg=[]
for i in l:
    if i>=0:
        pos.append(i)
    else:
        neg.append(i)
        print(f"your positive elements are{pos}")
        print(f"your negative elements are{neg}")


#2.Find the mean (average) of all list elements.

l=[10,20,30,40]                  #10+20+30+40 rout/4
                              # 25.0
                               
sum=0
for i in l:
    sum=sum+i
    avg=sum/len(l)
    print(f"your average is {avg}")
    #OR
    print(f"your average is{sum/len(l)}")
    
    
    #3. Find the greatest element and print its  index.
    a=[20,43,17,68,29,90,47]
    largest=a[0]
    for i in a:
        if i>largest:
            largest=i
            print(f"your largest value is {largest}")
            
     #OR
a=[20,43,17,100,68,29,90,47]
largest=a[0]
index=0
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
        index=i
        print(f"your largest value is {largest} at index {index}")
        
        
        
   #5.Check if the list is already sorted.

a=[10,20,30,40,60,50]
for i in range(len(a)-1):
    if a[i]>a[i+1]:
        print("your list is not sorted")
        break
    else:
        print("your list is sorted")
        
  

