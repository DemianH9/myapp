from flask import Flask
import os

app = Flask(__name__)

# Ruta para verificar persistencia de datos
DATA_FILE = "/app/data/mydata.txt"

@app.route('/')
def home():
    return "¡Aplicación desplegada en Docker con Nginx como proxy inverso!"

@app.route('/data')
def handle_data():
    # Ejemplo de persistencia: lee/escribe en un archivo
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            f.write("Datos iniciales\n")
    
    with open(DATA_FILE, 'a+') as f:
        f.seek(0)
        content = f.read()
        f.write("Nuevo acceso registrado\n")
    
    return f"Datos persistentes:\n{content}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)