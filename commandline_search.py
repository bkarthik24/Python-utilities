# Program : Command line wikiedia search 
# Date : 11/14/2020
# Author : Karthik  
import wikipedia 
import wikipediaapi                 # Wrapper used for getting Page URL 
import webbrowser
query = input("Wikipedia Search :")
result = wikipedia.search(query)
wiki = wikipediaapi.Wikipedia('en')
Sno = "{number:d}. "
title_url = []                     # List storing title links 
for i in range(len(result)-1):
    page = wiki.page(result[i])
    print(Sno.format(number=i+1),end= ' ')
    print(page.title)
    title_url.append(page.fullurl)
select = input("Your search results. Enter your choice:")
if 1<=int(select)<=(len(title_url)):
    webbrowser.open(title_url[int(select)-1])
else :
    print("Number out of range")

