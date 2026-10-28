a=[12,23,45,67,89]
print(a)
print(type(a))
print(a[-1])

#-5,-4,-3,-2,-1
#[12,23,45,67,89]
#0,1,2,3,4,


#mutable nature-you can change any values on your list
l=[10,22,30,40,50]
l[1]=20
print(l)

#Duplicates- you can have duplicate values
#t=[1,1,1,2,2,2,2,3,3,3,3]


#traversing on list
a=[10,20,30,40,50]
for i in a:
    print(i)

#traversing on index
for i in range(0, len(a)):
    print(f"{i}:{a[i]}")

#Creating and Accessing Lists
fruits=["apple","banana","mango"]
print(fruits[0])#apple
print(fruits[-1])#mango
print(fruits[0:2])#['apple','banana']
fruits[1] = "grape"#mutation-lists allow this
print(fruits)

#Key list method
#lst=[3,1,4,1,5]
#lst.append(9)
#lst.insert(0,0)         [3,1,4,1,5,9] add to end
#lst.remove(1)           [0,3,1,4,1,5,9] insert at index
#lst.pop()               removes first1
#lst.sort()              removes last element
#lst.reverse()           sort ascending
#len(lst)                number  of items

#CRUD
# Create   #Read   # Update # Delete
#1. add to end
a=[10,20,30,40,50]
a.append(60)
a.append("hello")
print(a)


#add values in the middle
a=[10,20,40,50]
a.insert(2,30)
print(a)
   
   
#Removes last element
l=[10,20,30,40,55,50]#up 0,1,2,3,4,5
a=l.pop()
print(l)  

print(a)
a=l.pop(4)
print(l)



#Removes first1:
l=[10,20,55,30,40,55,50]
l.remove(55)
print(l)

l.remove(30)
print(l)
l.clear()
print(l)


#Sort ascending
l=[29,45,67,12,90,34]
l.sort()
print(l)


l.sort(reverse=True)
print(l)