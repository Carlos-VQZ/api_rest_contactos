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

# metodo POST para contactos 
class datos(BaseModel):
    nombre: str
    correo: str

@app.post("/v1/contactos")
async def root(datos: dict):
    # Suponemos que 'datos' es un diccionario con 'nombre' y 'correo' como claves
    nombre = datos.get("nombre")
    correo = datos.get("correo")

    if nombre and correo:
        with open("contactos.csv", "a", newline='') as file:
            escribir_csv = csv.writer(file)
            escribir_csv.writerow([nombre, correo])

        # Opcionalmente, si deseas convertir los datos a JSON y guardarlos en un archivo .json
        with open("contactos.csv", "r") as file:
            contactos = list(csv.DictReader(file))

        json_data = json.dumps(contactos)

        with open("contactos.json", "w") as json_file:
            json_file.write(json_data)

        return {"message": "Datos agregados correctamente"}
    else:
        return {"error": "Falta el nombre y/o correo en los datos enviados"}
