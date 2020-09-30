# like map in c++
#also called as hash map
#mutable
#unordered data structure  , no indexing
# key should be unique and immutable
#in background python will create a hashtable
studentId={
    #key:value,
    "1702028": "Tanver Ahmed Likhon",
    "1702029": "Saroyar Ahmed",
    "1702029": "OverLap",
    1702065:"Hasanul Bari"
}



print(studentId["1702029"])
print(studentId.get("1702028"))
print(studentId.get("1702030"))#print none if not found
#print(studentId["1702030"])#will print and error if not found
print(studentId.get("1702030",-1))#print -1 if not found

print(studentId.get("1702022","Message"))#print message if not found
print(studentId[1702065])

#in setdefault method if the key doesn't exist it will create the key and assign value as none
print(studentId.setdefault("1702015"))
print(studentId)

#in setdefault method if the key doesn't exist it will create the key and assign value ""hello""
print(studentId.setdefault("1702015","hello"))
print(studentId)

#iteration
for x in studentId:
    print(x)##it will print keys only
    print(x,studentId[x])#it will print keys and values

d={}
for value in range(1,11):
    d[value]=value*value
print(d)
print(d.keys())
print(d.values())
print(d.items())#iteration


#update and delete
l1=[1,2,3,4,5]
l2=[1,4,9,16,25]
d=dict(zip(l1,l2))
print(d)

l=[1,2,3,4,5]
#fromkeys(keylist,value) value is optional
d1=dict.fromkeys(l,20)
print(d1)


#merging two dictionaries
d1={1:1,2:4,3:9,4:16}
d2={5:25,6:36,7:59,8:64}
d1.update(d2)# it will not return anything but uptdate
print(d1)

#delete methods
#pop popitem clear del

r=d1.pop(2)#key 2
print(r)
print(d1)
print("Hello")
r=d1.popitem()#randomly remove last item insert into the dictionary nd will return key and value
print(d1,r)

#d1.clear()
#del d1