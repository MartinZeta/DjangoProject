# Coderhouse-56060-Django

## Proyecto Django

Haremos un proyecto con el framework Django para certificar el curso.

## Entornos virtuales

Un entorno virtual en Python es una herramienta 
que te permite crear un espacio aislado donde puedes instalar 
y manejar las dependencias (bibliotecas y versiones de Python) 
específicas para un proyecto en particular, sin afectar al sistema global de Python.

`pip list` muestra las bibliotecas instaladas en el entorno virtual o global

¿Cómo crear un entorno virtual? (entorno aislado del global)

`python -m venv .venv`

¿Cómo activar el entorno virtual?
`.\.venv\Scripts\activate`  (Windows Powershell)
`source .venv/bin/activate` (Linux o Mac)

## Instalación Django

`pip install django`

## Comandos

- Creo una carpeta `project`
- `cd project`
- `django-admin startproject config .`
- `python manage.py runserver`
- `python manage.py startapp cliente`
- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`


#---------------------------------------------------

# Unificacion del paquete Propio con el del Profe 

#---------------------------------------------------

## Como crear un entorno virtual? (entorno aislado del global)

- `pip list`: muestra las biblotecas instaladas en el entorno virtual o GLOBAL.

- `python -m venv .venv`: Crea el entorno virtual. Antes de hacer el entorno virtual, se debe crear un modulo llamado .gitignore dentro de el escribir .venv (.gitignore: le dice a git que no suba este paquete o archivo a internet que lo ignore.)


## Como activar el entorno virtual?

- `.\.venv\Scripts\activate`: con este comando activamos el entorno virtual.


## Instalar Django en entorno virtual? 

Esto permite que en este entorno solo quede una version que Django o otros paquetes que instalemos
y si salen actualizaciones que no proboque un error. ¡¡¡¡¡Tambien tiene que estar activo el entorno virtual!!!!, esto para que no lo instale en otro entorno.

## Comandos

- `pip install django:` instala el paquete django para usar los templates y comandos del mismo.

- `Creamos la carpeta` project

- `cd project`: Nos mueve a la carpeta que creamos, en este caso, project.

- `django-admin --version`: Nos dice la version de django"

- `python -m django startproject config` o `django-admin startproyect config .`: Crea una carpeta (config) dentro de carpeta config que creamos al principio con las configuraciones de django y el modulo manage.py para poder trabajar.
Luego de "startproyect" es el nombre que va a tomar la carpeta con estas configuraciones, se deberia colocar siempre config.

(Manage nos ayuda a interactuar con nuestro proyecto con algunos comandos muy simples. Ademas
Lo que genera este comando de primeras es un archivo manage, que es el encargado de casi todo lo que queramos solicitarle al proyecto, 
y una carpeta con los archivos iniciales necesarios para iniciar con configuraciones básicas.)

- `python manage.py migrate`: Migra todo a una server de django y nos brinda una url.

- `python manage.py runserver`: Nos crea y corre el servidor en internet

- `Crtl + C`: Para salir del server y usar la terminal

-`django-admin startapp core`: Crea una app. (Core) es el nombre que toma la carpeta que se usa por convencion, pero puede ser cualquiera.
Ademas, creamos una carpeta dentro de core, se va a llamar templates(Plantillas) que lo que guarda son archivos o modulos HTML.
Luego, creamos otra carpeta pero dentro de templates, con el nombre de la app, osea, core nuevamente, donde vamos a hacer un modulo que contenga HTML.

# Clase 10

Creamos la app, en este caso "cliente" con las configuraciones predeterminadas de django

-`python manage.py startapp cliente`: antes de ejecutar este codigo, hay que pararce sobre la carpeta project (que es la config), tambien donde esta manage.py

-`python manage.py makemigrations`: Antes de ejecutar este comando, django tiene que tener la app installada en el modulo settings.py en INSTALLED_APPS se escribe el nombre del paquete. 

-`python manage.py migrate`: Traduce todo lo que esta en migrations

-`python manage.py createsuperuser`: usu: Martin o admin contra: 123456 o 123, Crea un usuario superior, maneja todo