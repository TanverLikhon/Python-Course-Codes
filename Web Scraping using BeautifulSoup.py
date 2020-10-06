import requests
from bs4 import BeautifulSoup

response=requests.get("http://codeforces.com/profile/tanverlikhon6795")
print(response) #if it returns 200 that means i have succesfully received response from the server else there is some
# error : if 404 than it means i can not go ahead with the scrapping part of it
print(response.status_code)#returns entire html code of the page
print(response.content)#returns entire html code of the page

soup=BeautifulSoup(response.content,"html.parser")
print(soup.prettify())#it will show the entire html code

# find("a")#finds first anchor tag
# find_all("div")#finds all div tag
# find_parent("a")
# find_next_siblings("a")

card=soup.find("div",attrs={"class":"main-info"})
#if I call find_all ithen card will be iterable
# print(card)
name=card.find("div",attrs={"class":"user-rank"})#div under div
print(name.text)#fetch the text part

card1=soup.find("h1")
print(card1.text.strip("\n"))#for newline

print("Printing Data")

data="{} {}".format(name.text,card1.text.strip("\n"))
print("data->",data)

