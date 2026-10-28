#Tuple-The Immutable List
#EXAMPLE-
        #days=("Mon","Tue","Wed")
        #print(day[0])   #Mon
        #days[0]="x"     #X Type error- tuples are immutable
        
a=["monday","tuesday",123,567]        
tup=tuple(a)
print(tup[-1])
#it has immutable nature-you cannot change any values inside your tuple

#Tuple Methods(only2!)
t=(1,2,3,2,1)
t.index(2)
t.count(2)

a=["monday","tuesday",123,567,123,123,123]
tup=tuple(a)
print(tup[-1])

print(tup.index("tuesday"))
print(tup.count(123))



#Real life use

def students():
    return "uttam",17,"uk9761450@gmail.com"
info=students()
name,age,mail=info
print(mail,name)