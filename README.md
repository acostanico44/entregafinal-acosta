#  Playground Blog - Proyecto Django

Bienvenido a mi blog personal desarrollado con Django. Aquí comparto ideas, prácticas de desarrollo web y diseño con foco en simplicidad, estética y funcionalidad.

## Tecnologías utilizadas

- **Python 3**
- **Django 4**
- **Bootstrap 5**
- **Bootstrap Icons**
- HTML + CSS (personalizado)
- Sistema de templates extendido
- Autenticación de usuarios
- Manejo seguro de errores (403, 404)
- Manejo de imágenes (media)

## Estructura del proyecto

playground_project/
├── blog/                  # App principal: publicaciones
├── accounts/              # App para usuarios, login y perfil
├── about/                 # App de info personal
├── templates/             # Plantillas HTML base y de error
├── static/                # Archivos CSS e imágenes
├── media/                 # Imágenes de publicaciones y avatares
├── config/    # Configuración Django
├── manage.py              # Comando principal

## Funcionalidades principales

Registro, login, edición de perfil y cambio de contraseña

Crear, editar y eliminar publicaciones

Subida de imágenes en publicaciones

Página de inicio con bloque de bienvenida y últimas entradas

Diseño responsivo y minimalista

Páginas 403 y 404 personalizadas

Sistema de mensajes para acciones exitosas

## Cómo correr el proyecto localmente
1.
Clonar el repositorio:

bash
git clone https://github.com/tuusuario/playground-blog.git
cd playground-blog

2.
Crear entorno virtual y activar:

bash
python -m venv env
source env/bin/activate   # En Linux/Mac
env\Scripts\activate      # En Windows

3.
Instalar dependencias:

bash
pip install -r requirements.txt

4.
Migrar y correr el servidor:

bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

5.
Acceder a: http://localhost:8000


## VIDEO FUNCIONALIDADES DE LA PAGINA.

https://youtu.be/62HHTV0OmtI