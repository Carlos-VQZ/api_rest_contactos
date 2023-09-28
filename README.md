# Desing Document: API REST CONTACTOS

## 1. Descripcion
Ejemplo de una API REST para gestionar contactos en una DB utilizando FastAPI.

## 2. Objetivo
Realizar un ejemplo de diseño de una API REST de tipo CRUD y su posterior codificación utilizando el framework [FastAPI](https://fastapi.tiangolo.com/).

## 3. Diseño de la BD
Para este ejemplo se utilizará el gestor de base de datos [SQLite3](https://www.sqlite.org/) con las siguientes tablas:

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

CREATE TABLE IF NOT EXISTS contactos (
    id_contacto INTEGER PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    primer_apellido VARCHAR(50) NOT NULL,
    segundo_apellido VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL,
    telefono VARCHAR(13) NOT NULL
);

## 4. Diseño del Endpoint
Diseño del end para el recurso contatos

### 4.1 Listar todos los contactos
Endpoint para obtener todos los contactos

## 4.2 Get incial
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|--|
|2|Summary|--|
|3|Method|--|
|4|Endpoint|--|
|5|Query Param|--|
|6|Path Param|--|
|7|Data|--|
|8|Version|--|
|9|Status Code|--|
|10|Response type|--|
|11|Response|--|
|12|Curl|--|
|13|Status Code (error)|--|
|14|Response Type (error)|--|
|15|Response (error)|--|

## 4.3 GET
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|--|
|2|Summary|--|
|3|Method|--|
|4|Endpoint|--|
|5|Query Param|--|
|6|Path Param|--|
|7|Data|--|
|8|Version|--|
|9|Status Code|--|
|10|Response type|--|
|11|Response|--|
|12|Curl|--|
|13|Status Code (error)|--|
|14|Response Type (error)|--|
|15|Response (error)|--|

## 4.4 POST
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|--|
|2|Summary|--|
|3|Method|--|
|4|Endpoint|--|
|5|Query Param|--|
|6|Path Param|--|
|7|Data|--|
|8|Version|--|
|9|Status Code|--|
|10|Response type|--|
|11|Response|--|
|12|Curl|--|
|13|Status Code (error)|--|
|14|Response Type (error)|--|
|15|Response (error)|--|

## 4.5 PUT
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|--|
|2|Summary|--|
|3|Method|--|
|4|Endpoint|--|
|5|Query Param|--|
|6|Path Param|--|
|7|Data|--|
|8|Version|--|
|9|Status Code|--|
|10|Response type|--|
|11|Response|--|
|12|Curl|--|
|13|Status Code (error)|--|
|14|Response Type (error)|--|
|15|Response (error)|--|

## 4.5 Delete
|No.|Propiedad|Detalle|
|--|--|--|
|1|Description|--|
|2|Summary|--|
|3|Method|--|
|4|Endpoint|--|
|5|Query Param|--|
|6|Path Param|--|
|7|Data|--|
|8|Version|--|
|9|Status Code|--|
|10|Response type|--|
|11|Response|--|
|12|Curl|--|
|13|Status Code (error)|--|
|14|Response Type (error)|--|
|15|Response (error)|--|
