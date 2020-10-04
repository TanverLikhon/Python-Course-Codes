#json file is wildely used in field of development
'''
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
 It is easy for humans to read and write. It is easy for machines to parse and
 generate. It is based on a subset of the JavaScript Programming Language
 Standard ECMA-262 3rd Edition - December 1999.

 light weght
 '''
# Json vs python
# Json objects         dict{"key":"value"}
# numbers 10 10.55     int float
# array[10,"string"]   list
#
# " "                 ' ' " "etc

import json

handle=open("json_input.json","r")
content=handle.read()
print(content)
handle.close()
d=json.loads(content)
# d=json.loads(content) #converting to python dictionary
print(d)
print(d['database']['port'])

d['database']['port']=3330
print(d)
print(d['files']['log'])
d['files']['log']=("/log/app.log","/log/app.log")#adding tuple to dictionary
print(d)

# j=json.dumps(d)#convert dictionary to json file
# print(j)

# handle=open("json_input.json","w")
# handle.write(j)
# handle.close()

