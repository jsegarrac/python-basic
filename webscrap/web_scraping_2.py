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
    
# Get Request with URL Parameters

# GET

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r=requests.get(url_get,params=payload)
print(r.url)

print("request body:", r.request.body)

print(r.status_code)

print(r.text)

print(r.headers['Content-Type'])

print(r.json())

print(r.json()['args'])

# POST

url_post='http://httpbin.org/post'
r_post=requests.post(url_post,data=payload)

print("POST request URL:",r_post.url )
print("GET request URL:",r.url)

print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)

print(r_post.json()['form'])

# https://requests.readthedocs.io/en/latest/?utm_content=000026UJ&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01&utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_term=10006555#
