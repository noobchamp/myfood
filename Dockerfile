# Usa la imagen base de Python
FROM python:3.9-slim

# Establece la variable de entorno PYTHONUNBUFFERED en 1
# Esto evita que Python haga buffering de la salida, lo que es útil para la salida de registro
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo requirements.txt al contenedor en /app
COPY requirements.txt /app/

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el contenido del directorio actual al directorio de trabajo (/app) en el contenedor
COPY . /app/

# Comando para iniciar Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "nombre_del_proyecto.wsgi:application"]
