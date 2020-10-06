#decorators are function which take function as arguments and returns another function

def deco(func):
    def new_func(val1,val2):
        if type(val1)==type(val2):
            return func(val1,val2)
        else:
            return func(str(val1),str(val2))

    return new_func


@deco
def concate(val1,val2):
    return val1+val2

result=concate(10,10)
print(result)


result=concate("Python","String")
print(result)

result=concate(101,"String")
print(result)