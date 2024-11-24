# Data Engineering Process
'''
There are several steps in Data Engineering process.

Extract - Data extraction is getting data from multiple sources. Ex. Data extraction from a website using Web scraping or 
          gathering information from the data that are stored in different formats(JSON, CSV, XLSX etc.).

Transform - Transforming the data means removing the data that we don't need for further analysis and converting the data in 
            the format that all the data from the multiple sources is in the same format.

Load - Loading the data inside a data warehouse. Data warehouse essentially contains large volumes of data that are accessed 
       to gather insights.
'''

import urllib.request
urllib.request.urlretrieve("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")

import pandas as pd


filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")

df = pd.read_csv("addresses.csv", header=None)