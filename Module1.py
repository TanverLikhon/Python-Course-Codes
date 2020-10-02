""""
Docstring: it is the description of particular module

This module contains binary search Implementation
Modified : 03-10-20

"""



def binary_serach(l,key):

    """
         BinarySearch
    """
    if len(l)==0:
        return False
    mid=len(l)//2 #floor

    if l[mid]==key:
        return True
    elif key<l[mid]:
        return binary_serach(l[:mid],key)
    else:
        return binary_serach(l[mid+1:],key)

# print(__name__) #if this module is called from Module2 than it is __main__

if __name__=='__main__':
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    key = 7
    result = binary_serach(l, key)
    print(result)