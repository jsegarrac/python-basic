# Downloading And Scraping The Contents Of A Web Page

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page


url = "http://www.ibm.com"

data  = requests.get(url).text 

soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'

print(soup.prettify())

for link in soup.find_all('a',href=True): # in html anchor/link is represented by the tag <a>
    print(link.get('href'))
    
for link in soup.find_all('img'): # in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))
