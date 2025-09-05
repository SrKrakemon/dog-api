from flask import Flask, render_template, jsonify
import requests
from config import API_KEY, URL

app = Flask(__name__)

@app.route('/')
def index():
    headers = {
        'x-api-key': API_KEY
    }
    
    try:
        # lista 4 imagenes de perros de manera aleatoria
        params = {'limit': 4}   
        response = requests.get(URL, headers=headers, params=params)
        
        if response.status_code == 200:
            dogs_data = response.json()
            return render_template('index.html', dogs=dogs_data)
        else:
            error_message = f"API Error: {response.status_code}"
            return render_template('error.html', error=error_message)
            
    except Exception as e:
        error_message = f"Error fetching dog data: {str(e)}"
        return render_template('error.html', error=error_message)

if __name__ == '__main__':
    app.run(debug=True) 
