# MOVIE-API-DJANGO

## Description
API para ecommerce de alquiler de peliculas. Está hecho con django-rest-framework y tiene las funciones de sign-in, sign-up y login de usuarios y también creación de películas.

## Author
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)

## Run Locally

Clonar el repositorio

```bash
  https://github.com/Geffrerson7/MOVIE-API-DJANGO.git
```

Ir al directorio al proyecto

```bash
  cd MOVIE-API-DJANGO
```

## Setup
Crear un entorno virtual y lo activamos:

```sh
$ python virtualenv venv
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Primero, dentro de settings.py comentamos la siguiente linea:  
```sh
INSTALLED_APPS = [
   ...
   #'django.contrib.admin',
   ...
]
```
Y en las rutas de nuestra carpeta principal(service_payments), comentamos lo siguiente:
```sh
urlpatterns = [
   ...
   #path('admin/', admin.site.urls) 
   ...
]
```
Luego de hacer esos pasos, realizamos la migración.
```sh
python manage.py makemigrations users

python manage.py migrate
```
Luego de haber realizado la migración, descomentamos todo lo anterior y realizamos las otras migraciones.
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```
