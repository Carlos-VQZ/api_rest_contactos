from fastapi import FastAPI, status 
from pydantic import BaseModel
import csv
import json  


app = FastAPI()

#Metodo GET para el endpoint raiz
@app.get(
    "/",
    status_code=status.HTTP_201_CREATED,
    summary="Endpoint GET")
async def root():
    """"
    #Endpoint Raiz
    ##1- Status codes:
    *201- Creado
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
    with open("contactos.csv", "r") as file:
        csv_reader = csv.reader(file)
        contactos = [row for row in csv_reader if row[1] == nombre]
        if not contactos:
            raise HTTPExeption(status_code-404, detail-"No se encontraron contactos con ese nombre")
        return {"contactos": contactos}

# metodo POST para contactos 
class datos(BaseModel):
    id_contacto: int
    nombre: str
    primer_apellido: str
    segundo_apellido: str
    correo: str
    telefono: str


@app.post("/v1/contactos")
async def root(datos: dict):
    id_contacto = datos.get("id_contacto")
    nombre = datos.get("nombre")
    primer_apellido = datos.get("primer_apellido")
    segundo_apellido = datos.get("segundo_apellido")
    email = datos.get("email")
    telefono = datos.get("telefono")

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

