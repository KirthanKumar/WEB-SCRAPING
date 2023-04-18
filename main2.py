# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
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
# .contents (stored in memory) - A tag's children are availabe as a list.
# .children (not stored in memory) - A tag's childeren are available as a generator, this generator can be iterated. The chilren can also be iterated using nextt function.
# these difference are effective for large website but for smaller ones both work the same. 

imgpreview2 = soup.find(id='imgpreview2') # returns the container having the spwcifird id
# print(imgpreview2)
print(imgpreview2.contents) # returns the children of container having the spwcifird id

# for elem in imgpreview2.children: #(or)  # for elem in imgpreview2.contents:
    # print(elem)
    
# for item in imgpreview2.strings:
#     print(item)
    
# for item in imgpreview2.stripped_strings:
#     print(item)
    
# print(imgpreview2.parent)

# for item in imgpreview2.parents:
#     print(item.name)

# print(imgpreview2.next_sibling)
# print(imgpreview2.next_sibling.next_sibling)
# print(imgpreview2.previous_sibling)
# print(imgpreview2.previous_sibling.previous_sibling)
# even a space in between elements is also counted as sibling

# css selector
elem = soup.select('#loginModal')
print(elem)
elem = soup.select('.loginModal')
print(elem)