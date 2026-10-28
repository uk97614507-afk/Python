#How Strings work Internally
a="u"
print(ord(a))
#every character a unick code

a="8"
print(ord(a))
#every character a unick code


a="@"
print(ord(a))
#unick code




#STRING INDEXING

    #  0123456
#Note:-COLLEGE
    #  -7_ _-1
a="COLLEGE"
print(a[1])

print(a[6],a[-1])
           
           
           
    #STRING SLICING
    
    
    #Note-a[start:stop:step]
a="COLLEGE"
#print that CLEE
print(a[0:7:2])
print(a[::2])
#print that LEG
print(a[3:6:1])


a="Hello how are you "
#print that how
print(a[6:9:1])



#TYPE CONVERSION
a="12"
a=int(a)
print(type(a))

#Or
a=12.4
a=int(a)
print(type(a))
  #Or
#a="12.4"
#a=int(a)
#print(a)
#you can convert string if it holds valid integer
#you can convert float values to int


#2.Change run he to-

a="12.4"
a=float(a)
print(type(a))


a=143
a=float(a)
print(a)



