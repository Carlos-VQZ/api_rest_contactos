from fastapi import FastAPI, status, File, UploadFile
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from PIL import Image
import requests
import random
import csv
import json  
import os


app = FastAPI()

#Metodo GET para el endpoint raiz
@app.get(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Endpoint GET")
async def root():
    """
    # Endpoint Raiz
    ## 1- Status codes:
    * 201- Creado
    """
    return {"message": "Bienvenido Api Contactos"}

# metodo GET para contactos
@app.get(
    "/v1/contactos",
    status_code=250,
    summary="Endpoint GET"    
)
async def root():
    """
    # Endpoint del método GET contactos
    ## 1- Status codes:
    * 201- CREADO  
    """
    with open("contactos.csv", "r") as file:
        contactos = list(csv.DictReader(file))

        json_data = json.dumps(contactos)

    with open("contactos.json", "w") as json_file:
        json_file.write(json_data)
 
    response = json_data
    return response

# Metodo Get para buscar contactos por nombre    
@app.get("/v1/contactos/{nombre}")
async def buscar_contacto(nombre: str):
    """
    # Endpoint del método GET contactos
    # Endpoint del método GET para buscar contactos por nombre
    ## 1- Status codes:
    * 201- CREADO  
    Proporcione el nombre del contacto que desea buscar y haga clic en 'Buscar'.
    """
    with open("contactos.csv", "r") as file:
        csv_reader = csv.reader(file)
        contactos = [row for row in csv_reader if row[1] == nombre]
        if not contactos:
            raise HTTPExeption(status_code-404, detail-"No se encontraron contactos con ese nombre")
        return {"contactos": contactos}

# metodo POST para contactos 
class Datos(BaseModel):
    id_contacto: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    correo: str
    telefono: str


@app.post("/v1/contactos")
async def create_contact(datos: Datos):
    id_contacto = datos.id_contacto
    nombre = datos.nombre
    primer_apellido = datos.primer_apellido
    segundo_apellido = datos.segundo_apellido
    email = datos.correo
    telefono = datos.telefono

    if contact_exists(id_contacto):
        return {"error": "El contacto con el mismo ID ya existe."}

    with open("contactos.csv", "a", newline='') as file:
        escribir_csv = csv.writer(file)
        escribir_csv.writerow([id_contacto, nombre, primer_apellido, segundo_apellido, email, telefono])

    with open("contactos.csv", "r") as file:
        contactos = list(csv.DictReader(file))

    json_data = json.dumps(contactos)

    with open("contactos.json", "w") as json_file:
        json_file.write(json_data)

    return {"message": "Datos agregados correctamente"}

def contact_exists(id_contacto):
    with open("contactos.csv", "r") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row and row[0] == str(id_contacto):
                return True
    return False

@app.get("/v1/contactos/{nombre}")
async def buscar_contacto(nombre: str):
    """
    # Endpoint del método DELETE para contactos
    Proporcione el ID del contacto que desea eliminar y haga clic en 'Borrar'.
    ## 1- Status codes:
    * 200 - OK
    * 404 - Not Found
    """
    with open("contactos.csv", "r") as file:
        csv_reader = csv.reader(file)
        contactos = [row for row in csv_reader if row[1] == nombre]
        if not contactos:
            raise HTTPException(status_code=404, detail="No se encontraron contactos con este nombre")
        return {"contactos": contactos}

@app.delete("/v1/contactos/{id_contacto}")
async def borrar_contacto(id_contacto: int):
    """
    # Endpoint del método DELETE para contactos
    Proporcione el ID del contacto que desea eliminar y haga clic en 'Borrar'.
    ## 1- Status codes:
    * 200 - OK
    * 404 - Not Found
    """
    found = False
    with open("contactos.csv", "r") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
    with open("contactos.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row and row[0] != str(id_contacto):
                csv_writer.writerow(row)
            else:
                found = True
        if not found:
            raise HTTPException(status_code=404, detail="No se encontró un contacto con este ID")
        return {"message": f"Contacto con ID {id_contacto} borrado exitosamente"}

@app.put("/v1/contactos/{id_contacto}")
async def actualizar_contacto(id_contacto: int, datos: Datos):
    """
    # Endpoint del método PUT para contactos
    Proporcione el ID del contacto que desea actualizar y haga clic en 'Actualizar'.
    ## 1- Status codes:
    * 200 - OK
    * 404 - Not Found
    """
    with open("contactos.csv", "r") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)
    updated = False
    with open("contactos.csv", "w", newline='') as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row and row[0] == str(id_contacto):
                updated = True
                csv_writer.writerow([
                    id_contacto,
                    datos.get("nombre", row[1]),
                    datos.get("primer_apellido", row[2]),
                    datos.get("segundo_apellido", row[3]),
                    datos.get("email", row[4]),
                    datos.get("telefono", row[5])
                ])
            else:
                csv_writer.writerow(row)
        if not updated:
            raise HTTPException(status_code=404, detail="No se encontró un contacto con este ID")
        return {"message": f"Contacto con ID {id_contacto} actualizado exitosamente"}


# Directorios para guardar archivos
UPLOADS_DIR = "static"
IMAGES_DIR = os.path.join(UPLOADS_DIR, "images")
MODIFIED_IMAGES_DIR = os.path.join(UPLOADS_DIR, "modified_images")

# Asegúrate de que los directorios existan
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(MODIFIED_IMAGES_DIR, exist_ok=True)

app.mount("/static", StaticFiles(directory=UPLOADS_DIR), name="static")

@app.post("/v1/contactos/upload/images/")
async def create_image_files(files: list[UploadFile] = File(...)):
    """
    # Endpoint del método POST para cargar imágenes
    Seleccione las imágenes que desea cargar y haga clic en 'Cargar imágenes'.
    ## 1- Status codes:
    * 200 - OK
    """
    for uploaded_file in files:
        with open(os.path.join(IMAGES_DIR, uploaded_file.filename), 'wb') as f:
            f.write(uploaded_file.file.read())
        process_image(uploaded_file.filename)
    return {"message": "Imagen recibida", "URL": f"https://localhost:8000/static/images/{uploaded_file.filename}"}

def process_image(filename):
    source_folder_path = IMAGES_DIR
    destination_folder_path = MODIFIED_IMAGES_DIR

    # Cargar la imagen
    image_path = os.path.join(source_folder_path, filename)
    im = Image.open(image_path)

    # Realizar operaciones de imagen
    box = (0, 0, 150, 200)
    region = im.crop(box)
    region.save(os.path.join(destination_folder_path, f"recorte_{filename}"))

    r, g, b = region.split()
    region = Image.merge("RGB", (b, g, r))
    region.save(os.path.join(destination_folder_path, f"cambio_{filename}"))

    out = region.rotate(45)
    out.save(os.path.join(destination_folder_path, f"giro_{filename}"))

@app.get("/v1/contactos/upload/images/")
async def main():
    """
    # Formulario para cargar imágenes
    Seleccione las imágenes que desea cargar y haga clic en 'Cargar imágenes'.
    ## 1- Status codes:
    * 200 - OK
    """
    content = """
<body>
<form action="/upload/images/" enctype="multipart/form-data" method="post">
<input name="files" type="file" accept="image/*" multiple>
<input type="submit" value="Upload Images">
</form>
</body>
    """
    return HTMLResponse(content=content)


class GameSearcher:
    def search_game_by_title(self, juego_a_buscar):
        url = f"https://www.cheapshark.com/api/1.0/games?title={juego_a_buscar}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data:
                return data
            else:
                raise HTTPException(status_code=404, detail="No se encontraron juegos con ese nombre.")
        else:
            raise HTTPException(status_code=response.status_code, detail=f"Error al llamar a la API. Código de estado: {response.status_code}")

game_searcher = GameSearcher()

@app.get("v1/contactos/form_search_game/")
async def form_search_game():
    """
    # Formulario de búsqueda de juegos
    Ingrese el nombre del juego a buscar y haga clic en 'Buscar'.
    ## 1- Status codes:
    * 200 - OK
    """
    content = """
    <body>
    <form action="/search_game/" enctype="multipart/form-data" method="get">
    <label for="juego_a_buscar">Nombre del juego:</label><br>
    <input type="text" id="juego_a_buscar" name="juego_a_buscar" value=""><br><br>
    <input type="submit" value="Buscar">
    </form>
    </body>
    """
    return HTMLResponse(content=content)

@app.get("v1/contactos/search_game/")
async def get_game_by_title(juego_a_buscar: str):
    """
    # Búsqueda de juegos por título
    Proporcione el nombre del juego que desea buscar y haga clic en 'Buscar'.
    ## 1- Status codes:
    * 200 - OK
    * 404 - Not Found
    """
    return game_searcher.search_game_by_title(juego_a_buscar)
