'''
generator function will execute from the yeild statement to the next yeild statement
saves memory
'''

def fibo():
    first_num=0;
    second_num=1;
    while(True):
        next_value=first_num+second_num
        yield next_value#if yeild statement is use in a function then it is called generator fucntion
        first_num,second_num=second_num,next_value

g=fibo() #return generator class object it is iterable oblject
# print(g)
# print(next(g))#will generate first number
# print(next(g))#will generate second number
# print(next(g))#will generate third number
# print(next(g))

for value in range(10):
    print(next(g))

l=[1,2,3,4,5,6,7,8,9]
l2=(value*value for value in l)#it's an generator expression
print(next(l2))
print(next(l2))