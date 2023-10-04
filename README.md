# Design Document: API REST CONTACTOS
## 1. Descripción
Ejemplo de una API REST para gestionar contactos en una DB utilizando FastAPI.

## 2. Objetivo 
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com/).

## 3. Diseño de la BD 
Para este ejemplo se utilizará el gestor de base de datos [SQLite3](https://www.sqlite.org) con las siguientes tablas:

### 3.1 Tabla: contactos 
|No.|Campo|Tipo|Restricciones|Descripción|
|--|--|--|--|--|
|1|id_contacto|int|PRYMARY KEY|Llave primaria de la tabla|
|2|nombre|varchar(100)|Not Null|Nombre del contacto|
|3|primer_apellido|varchar(50)|Not Null|Primer Apellido del contacto|
|4|segundo_apellido|varchar(50)|Not Null|Segundo Apellido del contacto|
|5|email|varchar(100)|Not Null|Email del contacto|
|6|telefono|varchar(13)|Not Null|Telefono del contacto|

### 3.2 Script
```
CREATE TABLE IF NOT EXISTS contactos (
    id_contacto INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    segundo_apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(13) NOT NULL
);
```

## 4. Diseño de ENDPOINTS

### 4.1 GET
#### http://localhost-8000/contactos
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para recibir datos de la API|
|2|Summary|Endpoint GET|
|3|Method|GET|
|4|Endpoint|http://localhost-8000/contactos|
|5|Query Param|limit = 20|
|6|Path Param|NA|
|7|Data|NA|
|8|Version|v1|
|9|Status code|200 OK|
|10|Content-type|application/json|
|11|Response|response.json|
|12|Curl|curl -X GET 'hhtp://localhost-8000/contactos/' -H 'accept:application/json'|
|13|Status code (error)|400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Server Error|
|14|Response type (error)|application/json|
|15|Response (error)|404: solicitud no valida, 401: no tienes permiso para solicitar este recurso, 404: el recurso no existe, 500: hubo un problema en el servidor.|

### 4.2 POST
#### http://localhost-8000/contactos
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para enviar datos a la API|
|2|Summary|Endpoint POST|
|3|Method|POST|
|4|Endpoint|http://localhost-8000/contactos|
|5|Query Param|NA|
|6|Path Param|NA|
|7|Data|id_contacto, nombre, apellidos, telefono, correo|
|8|Version|v1|
|9|Status code|201 CREATED, 202 ACCEPTED|
|10|Content-type|application/json|
|11|Response|response.json|
|12|Curl|curl -X POST 'hhtp://localhost-8000/contactos/' -H 'accept:application/json'|
|13|Status code (error)|400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Server Error|
|14|Response type (error)|application/json|
|15|Response (error)|404: solicitud no valida, 401: no tienes permiso para solicitar este recurso, 404: el recurso no existe, 500: hubo un problema en el servidor.|


### 4.2 PUT
#### http://localhost-8000/contactos?id_contacto=
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para actualizar datos de la API|
|2|Summary|Endpoint PUT|
|3|Method||PUT|
|4|Endpoint|http://localhost-8000/contactos?id_contacto=|
|5|Query Param|NA|
|6|Path Param|id_contacto|
|7|Data|Datos actualizados|
|8|Version|v1|
|9|Status code|201 CREATED, 202 ACCEPTED, 200 OK|
|10|Content-type|application/json|
|11|Response|response.json|
|12|Curl|curl -X PUT 'hhtp://localhost-8000/contactos/' -H 'accept:application/json'|
|13|Status code (error)|400 Bad Request, 401 Unauthorized, 404 Not Found, 500 Internal Server Error, 412 Precondition Failed, 422 Unprocessable Entity|
|14|Response type (error)|application/json|
|15|Response (error)|404: solicitud no valida, 401: no tienes permiso para actualizar este recurso, 404: el recurso no existe, 500: hubo un problema en el servidor, 412: las condiciones de datos no son correctas, 422: los datos enviados no son validos|

### 4.2 DELETE
#### http://localhost-8000/contactos?id_contacto=
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|Endpoint para eliminar datos de la API|
|2|Summary|Endpoint DELETE|
|3|Method||DELETE|
|4|Endpoint|http://localhost-8000/contactos?id_contacto=|
|5|Query Param|NA|
|6|Path Param|id_contacto|
|7|Data|NA|
|8|Version|v1|
|9|Status code|202 ACCEPTED, 200 OK|
|10|Content-type|application/json|
|11|Response|response.json|
|12|Curl|curl -X DELETE 'hhtp://localhost-8000/contactos/' -H 'accept:application/json'|
|13|Status code (error)|401 Unauthorized, 404 Not Found, 500 Internal Server Error|
|14|Response type (error)|application/json|
|15|Response (error)|401: no tienes permiso para eliminar este recurso, 404: el recurso no existe, 500: hubo un problema en el servidor|

