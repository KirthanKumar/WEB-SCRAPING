# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
# When a call is made to server, to get a perticular web page, server returns the html, css and js file. Instead of browser getting this filr we get this file through python and extract some information from it, this is called scraping. 
# step 0: setting up the environment. * in order to use the power of python to scrap websites, we dont have to reinvent the wheel. *We can use existing liberies to get the job done. *we will install the following liberaries using python. * pip install requests * pip install html5lib(parser) * pip inatall bs4

# step 1: fetching the html content: Inorder to work with the html, we will have to get the html as a string. *we will leverage the power of python request module to get this done. *the next step then will be to parse the html content and give it a tree like structre so that it can be traversed. 

# step 2: * once the html is fetched using requests as an string we need to parse it. * for parsing we will use pythons BeautifulSoup module which will create a tree like structure for our DOM. 

# step 3: * once the html is fetched and parsed the next step is to manipulate the tree using BeautifulSoup's functions to geet our job done. * This tutorial will teach you hoe to get started and traverse the tree; * after watching this video u will be able to scrap any website  and its contents into ur desired format. 

# if we get stuck we will google and see stackoverflow and beautifulSoup docs. 
# step 0 
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# step 1
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# step 2
soup = BeautifulSoup(htmlContent, "html.parser")
# print(soup.prettify())

# step 3

# get the title of the page
title = soup.title

# commenly used types of objets: tag, NavigableString, BeautifulSoup, Comment
markup = "<p><!--this is a comment--></p>" #comment
soup2 = BeautifulSoup(markup)
print(soup2.p.string)
print(type(soup2.p.string))
exit()


# print(title, type(title)) # tag
# print(title.string, type(title.string)) # NavigableString
# pritn(type(soup)) # BeautifulSoup

# get all the paragraphs
paras = soup.findAll('p')
# print(paras)

# get first element in the html page
print(soup.find('p'))

# get classes of any element in th ehtml page
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# get the text from the tags/soup
print(soup.find('p').get_text())
print(soup.get_text())

# get all the anchor tags
anchors =soup.findAll('a')
all_links = set()
# print(anchors)
for link in anchors:
    if(link.get("href") != "#"):
        linkText = url + link.get('href')
        all_links.add(linkText)
        print(linkText)