import re

# . - any char #it will match with any character except newline
# [a-z] - char class # it will match only lowercase letter
# [A-Z] - char class # it will match only upper letter
# [0-9] - char class # it will match only digits letter
#
#     If we want to multiple occuerance to be matched we used + * operator
#     + means atleast one Ex: [a-z]+ : it will match atleast one alphabet/ if  no alphabet i will get empty result
#     * means zero or more
#
#     ^ - start of the string to be matched
#     $ - start of the string to be matched
#
#     ? - is used to specify something optional
#
#     [a-z]{4} it means there have to be 4 occurances of character
#     [a-z]{2,4} it means it will expect atleast 2 alphabet and max 4

s="ABCDE1234A"
r=re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l=re.findall(r,s)
print(l)

s="ABCDEEE12354A"
r=re.compile("[A-Z]{5}[0-9]{4}[A-Z]")
l=re.findall(r,s)
print(l)

# r=re.compile("^[A-Z]{5}[0-9]{4}[A-Z]")#it will find a pattern from the beginning and at last characters will be ignored
# r=re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")#it will find a pattern from the beginning and there must have no extra characters

#dd-mm-yyyy
s="12-05-2020"
r=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
l=re.findall(r,s)
print(l)

#search method

s="12-05-2020"
r=re.compile("^[0-9]{2}-[0-9]{2}-[0-9]{4}$")
m=re.search(r,s)# return MatchObject if matched with the pattern else none
print(m)
if m:
  print(m.group())#it will return entire match string/ if not matched it will give an error/ so it is handled with if condition
else :
    print("Pattern not found")

# further validation of the date

s="12-05-2020"
r=re.compile("^([0-9]{2})-([0-9]{2})-([0-9]{4})$")# groups are in the parenthesis
m=re.search(r,s)
# group-0 is the entire string
# group-1 is the date in string
# group-2 is the month in string
# group-3 is the year in string
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))

r=re.compile("^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$")# group name can be given like this
m=re.search(r,s)
print(m.group("date"))
print(m.group("month"))
print(m.group("year"))

num="+88 01781949541"
rr=re.compile("^(\+88)?\s(01)[3-9]{1}[0-9]{8}$") #\s is used for space
mm=re.search(rr,num)
if mm:
    print(mm.group())
else:
    print("Not matched")

num="+88 01181949541"
rr=re.compile("^(\+88\s)?(01)[3-9]{1}[0-9]{8}$") #\s is used for space
mm=re.search(rr,num)
if mm:
    print(mm.group())
else:
    print("Not matched")

# rr=re.compile("^(?:\+88)?\s(01)[3-9]{1}[0-9]{8}$") ?: non capturing group

# \d can be used instead of [0-9]
# \D can be used instead of [^0-9]
# \w can be used instead of [a-zA-Z0-9]
# \D can be used instead of [^a-zA-Z0-9]