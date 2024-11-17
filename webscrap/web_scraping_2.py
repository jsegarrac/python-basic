import requests
import os
from PIL import Image
from IPython.display import IFrame

url='https://www.ibm.com/'
r=requests.get(url)

# stus code
print(r.status_code)

# headers
print(r.request.headers)

# body
print("request body:", r.request.body)

# You can view the HTTP response header using the attribute headers
header=r.headers
print(r.headers)

# date
print(header['date'])

# Content-Type indicates the type of data:
print(header['Content-Type'])

# encoding
print( r.encoding)

# As the Content-Type is text/html we can use the attribute text to display the HTML in the body. We can review the first 100 characters:
print(r.text[0:100])

# You can load other types of data for non-text requests, like images. Consider the URL of the following image:
# Use single quotation marks for defining string
url='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r=requests.get(url)
print(r.headers)
print(r.headers['Content-Type'])

path=os.path.join(os.getcwd(),'image.png')
with open(path,'wb') as f:
    f.write(r.content)
Image.open(path)

# Question: Download a file
URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt'
r1=requests.get(URL)
print(r1.headers)
print(r1.headers['Content-Type'])

path1=os.path.join(os.getcwd(),'Example1.txt')
with open(path1,'wb') as f:
    f.write(r1.content)
