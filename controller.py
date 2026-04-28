from flask import render_template, request, redirect, url_for, flash
from model import ArbolBST

# Instancia global del árbol
diccionario_bst = ArbolBST()

# Datos iniciales
diccionario_bst.insertar("hola", "hello")
diccionario_bst.insertar("casa", "house")
diccionario_bst.insertar("perro", "dog")
diccionario_bst.insertar("gato", "cat")

def init_routes(app):
    """Función para registrar las rutas en la aplicación Flask."""
    
    @app.route('/')
    def index():
        palabras = diccionario_bst.obtener_inorden()
        return render_template('index.html', palabras=palabras)

    @app.route('/agregar', methods=['POST'])
    def agregar():
        espanol = request.form.get('espanol')
        ingles = request.form.get('ingles')
        if espanol and ingles:
            diccionario_bst.insertar(espanol, ingles)
            flash(f"Palabra '{espanol}' agregada correctamente.", "success")
        else:
            flash("Todos los campos son obligatorios.", "danger")
        return redirect(url_for('index'))

    @app.route('/buscar', methods=['POST'])
    def buscar():
        termino = request.form.get('termino_busqueda')
        resultado = diccionario_bst.buscar(termino)
        palabras = diccionario_bst.obtener_inorden()
        if resultado:
            flash(f"Traducción de '{termino}': {resultado}", "info")
        else:
            flash(f"La palabra '{termino}' no se encuentra.", "warning")
        return render_template('index.html', palabras=palabras, busqueda=True)

    @app.route('/eliminar/<espanol>')
    def eliminar(espanol):
        diccionario_bst.raiz = diccionario_bst.eliminar(diccionario_bst.raiz, espanol.lower())
        flash(f"Palabra '{espanol}' eliminada del BST.", "secondary")
        return redirect(url_for('index'))