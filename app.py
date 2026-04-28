from flask import Flask
from controller import init_routes

app = Flask(__name__)
app.secret_key = "clave_secreta_uagrm"

# Inicializar las rutas desde el controlador
init_routes(app)

if __name__ == "__main__":
    # Ejecución en el puerto 8000 como estaba configurado
    app.run(debug=True, port=8000)