# 🌐 Aplicación Web Flask - Proyecto Universitario

**Autor:** Mayeli Miranda Rocha
**Registro:** 223043362
**Materia:** Ingeniería de Sistemas - UAGRM

Este proyecto es una aplicación web desarrollada utilizando el micro-framework **Flask**, implementando una arquitectura de software basada en el patrón **MVC** (Modelo-Vista-Controlador).

## 🚀 Tecnologías y Requerimientos
* **Backend:** Python 3.10+ con el framework **Flask**.
* **Frontend:** HTML5 y CSS3 administrados mediante el motor de plantillas **Jinja2**.
* **Arquitectura:** Organización por capas para separar la lógica de datos, el control de rutas y la interfaz de usuario[cite: 2].
* **Contenedores:** Incluye configuración para entornos de desarrollo remoto (`.devcontainer`).

## 📁 Estructura del Proyecto
Basado en la organización del código fuente[cite: 2]:
* `app.py`: Archivo principal que inicia el servidor y configura la aplicación[cite: 2].
* `model.py`: Definición de la lógica de datos[cite: 2].
* `controller.py`: Manejo de las peticiones HTTP y lógica de control.
* `templates/`: Contiene los archivos de vista (`index.html`).
* `static/`: Recursos estáticos como estilos (`main.css`) e imágenes.

## 🛠️ Instalación y Ejecución
Para poner en marcha el servidor localmente, siga estos pasos:

1. **Instalar las dependencias:**
   Asegúrese de tener el archivo `requirements.txt` actualizado y ejecute:
   ```bash
   pip install -r requirements.txt
2. **Ejecutar el servidor flask**
   python app.py
3. **Ver la aplicación:**
    Abra su navegador y acceda a la dirección local:
    http://127.0.0.1:5000