import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Reading with xml.etree.ElementTree

# URL del archivo XML
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

# Descargar el archivo XML
response = requests.get(url)
if response.status_code == 200:
    # Guardar el archivo localmente
    with open("Sample-employee-XML-file.xml", "wb") as file:
        file.write(response.content)

    print("Archivo XML descargado y guardado como 'Sample-employee-XML-file.xml'")
else:
    print(f"Error al descargar el archivo: {response.status_code}")

# Parsear el archivo XML descargado
tree = ET.parse("Sample-employee-XML-file.xml")

# Get the root of the XML tree
root = tree.getroot()

# Define the columns for the DataFrame
columns = ["firstname", "lastname", "title", "division", "building", "room"]

# Initialize an empty DataFrame
datatframe = pd.DataFrame(columns=columns)

# Iterate through each node in the XML root
for node in root:
    # Extract text from each element
    firstname = node.find("firstname").text
    lastname = node.find("lastname").text
    title = node.find("title").text
    division = node.find("division").text
    building = node.find("building").text
    room = node.find("room").text
    
    # Create a DataFrame for the current row
    row_df = pd.DataFrame([[firstname, lastname, title, division, building, room]], columns=columns)
    
    # Concatenate with the existing DataFrame
    datatframe = pd.concat([datatframe, row_df], ignore_index=True)
    
print(datatframe)


# Imprimir elementos principales
#print("Raíz del XML:", root.tag)
#for child in root:
#    print("Elemento:", child.tag, "Atributos:", child.attrib)
    
    
