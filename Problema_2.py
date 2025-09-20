# Problema_2.py

# Diccionario de extensiones y sus tipos MIME
mime_extensiones = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Solicitar nombre de archivo al usuario
filename = input("Nombre Archivo: ").strip()

# Obtener la extensión en minúsculas
dot_index = filename.rfind(".")
if dot_index != -1:
    extension = filename[dot_index:]
    extension = extension.lower()
else:
    extension = ""

# Buscar el tipo MIME correspondiente
mime = mime_extensiones.get(extension, "application/octet-stream")

print(mime)