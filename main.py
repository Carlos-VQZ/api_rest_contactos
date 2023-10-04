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
async def root(datos: datos):
    datos = []
    with open("contactos.csv", "a",newline = '') as file:
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        datos.append([nombre, correo])
        escribir_csv = csv.writer(file)
            
        for fila in datos:
            escribir_csv.writerow(fila)

        with open("contactos.csv", "r") as file:
            contactos = list(csv.DictReader(file))

            json_data = json.dumps(contactos)
        with open("contactos.json", "w") as json_file:
            json_file.write(json_data)
    
        response = json_data
        return response

