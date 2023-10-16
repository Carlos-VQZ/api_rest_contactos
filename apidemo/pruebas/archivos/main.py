from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, File, UploadFile, status 
from fastapi.responses import HTMLResponse
import os

app = FastAPI()


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
    return {"message": "Bienvenido imagenes"}

# Directorios para guardar archivos
UPLOADS_DIR = "static"
IMAGES_DIR = os.path.join(UPLOADS_DIR, "images")
PDFS_DIR = os.path.join(UPLOADS_DIR, "pdfs")

# Asegúrate de que los directorios existan
os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(PDFS_DIR, exist_ok=True)

app.mount("/static/images", StaticFiles(directory=IMAGES_DIR), name="static_images")
app.mount("/static/pdfs", StaticFiles(directory=PDFS_DIR), name="static_pdfs")

@app.post("/upload/images/")
async def create_image_files(files: list[UploadFile]):
    for uploaded_file in files:
        with open(os.path.join(IMAGES_DIR, uploaded_file.filename), 'wb') as f:
            f.write(uploaded_file.file.read())
    return {"message": "Imagen recibida", "URL": "https://localhost:8000/static/images/"}

@app.post("/upload/pdfs/")
async def create_pdf_files(files: list[UploadFile]):
    for uploaded_file in files:
        with open(os.path.join(PDFS_DIR, uploaded_file.filename), 'wb') as f:
            f.write(uploaded_file.file.read())
    return {"message": "PDF recibido", "URL": "https://localhost:8000/static/pdfs/"}

@app.get("/")
async def main():
    content = """
<body>
<form action="/upload/images/" enctype="multipart/form-data" method="post">
<input name="files" type="file" accept="image/*" multiple>
<input type="submit" value="Upload Images">
</form>
<form action="/upload/pdfs/" enctype="multipart/form-data" method="post">
<input name="files" type="file" accept=".pdf" multiple>
<input type="submit" value="Upload PDFs">
</form>
</body>
    """
    return HTMLResponse(content=content)
