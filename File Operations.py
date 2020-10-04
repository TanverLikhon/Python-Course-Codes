
# r-> read
# r+
# w->write
# w+
# a->append
# a+
'''
r=> fp=> start,file should already exist,read
r+=> fp=> start,file should already exist,read+write

w=> fp => start,create a news file, write
w+=> fp =>start,create a new file, write +read

a=> fp => end, create a new file,write at the end
a+=> fp => end, create a new file, write +read

'''

fp=open("input.txt","r")#open("directory","mode") returns file object
# content=fp.read()# read the file and return string
# print(content)

# print("-----------------")
#
# content=fp.read()
# print(content)#it will not print because the file pointer is last of the file in previous read mode

# content=fp.read(25)#it will read first 25 characters
# print(content)

#readlines readline

# content=fp.readlines()#returns list,slice on the basis of new line character
# print(content)
# print(content[:5])#slicing

# content=fp.readline()#returns string
# print(content,type(content))
# #nextline
# content=fp.readline()#returns string
# print(content,type(content))

# for x in fp:
#     print(x)
fp=open("input2.txt","w") #if the file is opened in write mode then all the previous data will be lost,
# if  file not exist it will create a file,
fp.write("Hello tanver likhon")
fp.write("Hello tanver likhon3434") #text will be append to the end of the last text
fp.close()

#in write mode i can't make read operation

#in w+ mode i can write and read  operation, if  file not exist it will create a file, old data will be removed if file
# exists

fp=open("input2.txt","w+")
print(fp.tell())

#tell=> current fp position
#seek(offset,position)=> to change the fp position : offset specifies how many characters you want to move
#position 0->start of the file  1-> current position 2-> end of the file
#seek(15,0) => change the fp by 15 char from start of the file
#seek(0,2) => change the fp by 0 char from end of the file
#seek(15,1) not allowed
#seek(15,2) not allowed



fp.write("Hello tanver likhon6795")
print(fp.tell())
fp.seek(0,0)
print("--")
content=fp.read()
print(fp.tell())
print("content --",content)
fp.close()

#r+=> mode read+write , previous data will not be removed like w+

fp=open("input2.txt","r+")
content=fp.read()
print(content)

fp.write("\n\nki khobor")
content=fp.read()
fp.close();

#append append+ mode a a+
#in w w+ r r+ mode fp is at the start but in append fp is at last of the file
#a mode is not readable, a+ reading and writing allowed
fp=open("input2.txt","a+")
print(fp.tell())