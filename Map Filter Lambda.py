#using map filter same set problems can be solve instead of using list comprehension
#and these are faster than list comprehension

"""
Map()
The basic function of map() is to manipulate iterables. Map executes all the conditions
of a function on the items in the iterable. In the above example, we have
multiplied each element in the range 0–10 with 2 which gives us completely
 new list of elements. Map function takes all elements and allows you to apply
 a function on it and then passes it to the output which can have same as well
 as different values .

 Filter()
As the name suggests, it is used to filter the iterables as per the conditions. Filter filters
the original iterable and passes the items that returns True for the function provided to filter.
Therefore only the items in the iterables can be expected to be seen in the output. In the above
 example the condition is given in the form of lambda function and the elements which satisfy
 the condition are given in the list. The elements which are divisible by 2 are left and others
  are filtered out.
"""

l=[10,205,306,40,50]
l1=[100,200,300,400,500]

def sqr(num1):
    return num1**2

result=map(sqr,l)# map(func,iterable), it will pass each element from l and pass it to sqr and returns map object
print(list(result))
for value in result:
    print(value)

def add(num1,num2):
    return num1+num2

res=list(map(add,l,l1))
print(res)

# filter operation

def check1 (num1):
    if num1%2==0:
        return True
    else:
        return False


result = list(filter(check1, l))#it will return the element for which answer is true
result1 = list(map(check1, l))#it will return all the elemlents True or False
print("res  ",result)
print("res  ",result1)

'''
A function without name (Anoynymous Function)
Not Powerful as Named Function
A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression


Why Use Lambda Functions?
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

def myfunc(n):
  return lambda a : a * n

'''

x=lambda a,b: a*a+2*a*b+b*b
print(x(2,3))
print((lambda a,b: a*a+2*a*b+b*b)(2,6))

result=list(map(lambda num1:num1**2,l))
print(result)
result=list(filter(lambda num1:num1%2==0,l))
print(result)

d={10:50,2:40,3:30,4:20,1:10}
l=dict(sorted(d.items(),key=lambda x:x[1]))#sorted on the basis of values here x[0] is key
print(l)