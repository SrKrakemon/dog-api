
from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

def leer_api_key():
    """Lee la clave API desde un archivo protegido"""
    ruta_archivo = os.path.join('config', 'api_key.txt')
    try:
        with open(ruta_archivo, 'r') as archivo:
            return archivo.read().strip()
    except FileNotFoundError:
        raise Exception("El archivo de configuración no existe")

@app.route('/')
def index():
    api_key = leer_api_key()

    headers = {'x-api-key': api_key}
    respuesta = requests.get('https://api.thedogapi.com/v1/images/search', headers=headers)

    if respuesta.status_code == 200:
        datos_perro = respuesta.json()[0]
        return render_template('index.html', perro=datos_perro)
    else:
        return f'Error al obtener los datos: {respuesta.status_code}', 500

if __name__ == '__main__':
    app.run(debug=True)"
