  #! /bin/bash

  # Genera estructura de proyecto 
  
  mkdir -p DEV/dog-api/
  mkdir -p DEV/dog-api/config/
  mkdir -p DEV/dog-api/templates/
  

  cp api-key.txt DEV/dog-api/app.py
  cp api-key.txt DEV/dog-api/config/api-key.txt
  cd index.html DEV/dog-api/templates/index.html
  
  cd DEV/dog-api

  # inicia entorno virtual y descarga las dependencias necesarias

  python3.12 -m venv .venv
  source .venv/bin/activate
  pip install requests Flask
  

  

