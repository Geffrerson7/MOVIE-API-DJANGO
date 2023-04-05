# MOVIE-API-DJANGO

## Descripción
API para ecommerce de alquiler de peliculas. Está hecho con django-rest-framework y tiene las funciones de sign-in, sign-up y login de usuarios y también creación de películas.

## ERD

![ERD-MOVIE](https://user-images.githubusercontent.com/61089189/230192360-7b052f0e-16ce-4a8c-a1d6-dc54f0cf8302.png)

## Instalación local del proyecto

Clonar el repositorio

```bash
$ git clone https://github.com/Geffrerson7/MOVIE-API-DJANGO.git
```

Ir al directorio al proyecto

```bash
$ cd MOVIE-API-DJANGO
```

Crear un entorno virtual

```sh
$ virtualenv venv
```
Activar el entorno virtual
```sh
# windows
$ source venv/Scripts/activate
# Linux
$ source venv/bin/activate
```

Luego instalar las librerias:

```sh
(env)$ pip install -r requirements.txt
```

Luego, realizamos las migraciones.
```sh
(env) $ python manage.py makemigrations
(env) $ python manage.py migrate
```

Una vez concluido, procedemos a iniciar la app
```sh
(env)$ python manage.py runserver
```
Y navegar a
```sh
http://127.0.0.1:8000/
```

## Tecnologías y lenguajes utilizados

* **Python** (v. 3.10.7) [Source](https://www.python.org/)
* **Django** (v. 4.1.7)  [Source](https://www.djangoproject.com/)
* **Django Rest Framework** (v. 3.14.0) [Source](https://www.django-rest-framework.org/)
* **django-cors-headers** (v. 3.14.0) [Source](https://pypi.org/project/django-cors-headers/)
* **Simple JWT** (v. 5.2.2) [Source](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
* **drf-yasg** (v. 1.21.5) [Source](https://drf-yasg.readthedocs.io/en/stable/)

## Autor
- [Gefferson Max Casasola Huamancusi](https://www.github.com/Geffrerson7)
