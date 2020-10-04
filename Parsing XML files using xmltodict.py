import xmltodict

handle=open("xml_input.xml","r")
content=handle.read()
print(content)

d=xmltodict.parse(content)#converting to dictionary
print(d)

#dict to xml
x=xmltodict.unparse(d)
print(x)