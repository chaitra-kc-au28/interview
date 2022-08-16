import requests
from bs4 import BeautifulSoup
url="https://stackoverflow.com/questions/tagged/python "

# get html
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

# parse html
soup = BeautifulSoup(htmlContent, 'html.parser')

# html tree traversal
# title = soup.title
# print(title)

print(soup.find_all('a',class_='s-link'))
