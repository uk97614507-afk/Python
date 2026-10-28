#6.Difference()- Returns a set contsining the difference between two or more sets

s1={10,20,30,40}   # - this is shortcut
s2={30,40,50,60}
print(s1-s2)
print(s2-s1)


#7.difference update() -= Removes the items in this set that are also included in another, specified set
#-= this is shortcut
s1={10,20,30,40}
s2={30,40,50,60}
s2-=s1
print(s2)


#8.intersection()& Return a set , that is the intersection of two other sets
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.intersection(s2))
#or
s1&=s2
print(s1)


#9.issubset()<= Return True if all items of another set is present in this set
s1={10,20,30,40}
s2={30,40,50,60}
s3={30,40,70}
print(s3<=s2)


#10.issuperset() >= Returns True if all items of another set is present in this set
s1={10,20,30,40}
s2={30,40,50,60}
s3={30,40}
print(s2>=s3)

#11. symmetric_difference() ^ Returns a set with the symmetric difference of two sets
s1={10,20,30,40}
s2={30,40,50,60}
print(s1.symmetric_difference(s2))
#or
print(s1^s2)
#or
s1^=s2
print(s1)


#12.union() | Return a set coutaining the union of sets
s1={10,20,30,40}
s2={30,40,50,60}
print(s1|s2)

#13.update() |= update the set with the union of this set and others
