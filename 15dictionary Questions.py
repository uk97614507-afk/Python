#dictionary methods in python
#metods approach
#1.clear() Removes all the elements from the dictionary.
d={10:100,20:200,30:300,40:400}
d.clear()
print(d)

#2.fromkeys() return a dictionary with the specified keys and values.

d={10:100,20:200,30:300,40:400}
q = d.fromkeys([10,20,30,60,70],50)
print(q)

#3.get() returns the value of the specified key
d={10:100,20:200,30:300,40:400}
print(d.get(10))

#4.items() Returns a list countaining a tuple  for each key value pair.

d={10:100,20:200,30:300,40:400}
print(d.items())

#5. keys() return a list containing the dictionary's keys.
d={10:100,20:200,30:300,40:400}
print(d.keys())
print(d.values())

#6.pop() Removes the element  with the specified key.

d={10:100,20:200,30:300,40:400}
print(d.pop(20))
print(d)

#7.pop item() Removes the last inserted key -values pair
d={10:100,20:200,30:300,40:400}
d.popitem()
print(d)

#8. Set default() reurns the value of the specified key If the key does not exits insert the key, with the specified value.
d={10:100,20:200,30:300,40:400}
print(d.setdefault(60,3000))
print(d)

#9. update() updates the dictionary with the specified key-value pairs.
d={10:100,20:200,30:300,40:400}
d.update({10:1000}) or d.update({70:700})
print(d)


#10. values() Returns a list of all the values in the dictionary.
#traversing(loops)
d={10:100,20:200,30:300,40:400}
for i in d:
    print(f"key{i}:value{d[i]}")
    
#11. Merge two dictionaryies into one d1={a:1},d2={b:2} {a:1,b:2}
d1={"a":10,"b":20,"c":30}    
d2={"d":40,"e":50,"f":60}
for i in d2:
    d1[i]=d2[i]
    print(d1)
    
#12.Sum all values in a dictionary.
# {"a":10,"b":20,"c":30}
d1={"a":10,"b":20,"c":30}
sum=0
for i in d1:
        sum=sum+d1[i]
        print(sum)
        
        
 #13.Count the frequency of each element in a list using  a dictionary.
 # ["a","b","a","c","b","a"]      {"a":3,"b":2,"c":1}
l=["a","b","a","c","b","a","c","b","a"]
d={}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
#14. Combne two digits,adding values for common keys.
# Example: d1={"a":5,"b":3}, d2={"b":4,"c":2} -> {"a":5,"b":7,"c":2}
d1={"a":10,"b":20,"c":30}    
d2={"c":40,"d":50,"e":60}
for i in d2:
    if i in d1.keys():
        d1[i]=d1[i]+d2[i]
    else:
        d1[i]=d2[i]
        print(d1)
        