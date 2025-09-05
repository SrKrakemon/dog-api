  #! /bin/bash


  # Genera la estructura de directorios del proyecto
  mkdir -p DEV/dog-api/
  mkdir -p DEV/dog-api/templates/
  
  #Genera el arvivo de configuracion con las variables del proyecto
  API_KEY = "AGREGA AQUI TU API KEY" >> DEV/dog-api/config.py
  URL = "https://api.thedogapi.com/v1/images/search" >> DEV/dog-api/config.py

  # Copia los archivos estaticos del proyecto
  cp api-key.txt DEV/dog-api/app.py
  cp error.html DEV/dog-api/templates/error.html
  cd index.html DEV/dog-api/templates/index.html

  #Se mueve al directorio DEV/dog-api
  cd DEV/dog-api

  # Inicia el entorno virtual y descarga las dependencias necesarias

  python3.12 -m venv .venv
  source .venv/bin/activate
  pip install requests Flask
  

  

