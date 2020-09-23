first_number=10
second_number=20    #variable must be initialized

sum=first_number+second_number
print(sum)

# 1 variable name shoud start with lower case char
# 2 digits are allowed but not at the start
# 3 _allowed

# id and type

print(type(first_number),type(second_number))
print(id(first_number),id(second_number)) # it will show memory location

# object intering
# if the value of two variables are same then their memory location will also be same in python
# different memory locations will not be used

a=1
b=1;
print(id(a),id(b))