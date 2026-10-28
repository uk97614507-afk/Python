#Set - Unique Values only
#Example
s={1,2,2,3,3,3}
print(s) #(1,2,3)-duplicates
l=[1,22,2,4,4,4,5,6,6,6,7,7,7,8]
s=set(l)
print(s)


#Logic
s = "hello"
print(hash(s))

#OR
s = (1, "hello", (1, 2, 3))
print(hash(s))

l=[10,20,30,40]
for i in range(len(l)):
    print(i)
    #OR
    print(l[i])
    
#OR
l={10,20,30,40}
for i in l:
    print(i)

#SET Operations

#add()-Adds an element to the set
s={10,20,30,40}
s.add(60)
print(s)

#2.clear()-removes all the elements from the set
s={10,20,30,40}
s.clear()
print(s)


#3.copy-Returns a copy of the set

#4.discard()-Remove the specified item
s={10,20,30,40}
s.discard(30)
print(s)
    
    
#pop()-Removes an element from the set
s={70,10,20,30,40}
a=s.pop()
print(s)
print(a)





