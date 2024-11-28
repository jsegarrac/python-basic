from PIL import Image
import requests
from io import BytesIO

# URL de la imagen
url = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

# Descargar la imagen
response = requests.get(url)
if response.status_code == 200:
    # Abrir la imagen directamente desde los bytes descargados
    img = Image.open(BytesIO(response.content))
    
    # Mostrar la imagen
    img.show()

    # Guardar la imagen localmente
    img.save("dog.jpg")
