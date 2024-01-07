# Clase 9 y Clase 10

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

Creamos la app, en este caso "cliente" con las configuraciones predeterminadas de django, combiene crear varias apps para tener organizado.

-`python manage.py startapp cliente`: antes de ejecutar este codigo, hay que pararce sobre la carpeta project (que es la config), tambien donde esta manage.py. Por si acaso "cliente" es el nombre que toma el paquete, osea, la app.

-`python manage.py makemigrations`: Antes de ejecutar este comando, django tiene que tener la app installada en el modulo settings.py en INSTALLED_APPS del paquete config, se escribe el nombre del paquete, en este caso iria "cliente".
Este comando se utiliza cada vez que realizamos un cambio o creamos un nuevo modelo, sirve para migrar todo lo creado.

-`python manage.py migrate`: Traduce todo en un codigo django o SQL para poder verlo en la base de datos, este paso va luego de makemigrations.
luego de migrar todo los modelos, podemos verlo en la base de datos llamada, db.sqlite3
con el nombre de la app y nombre de la clase del modelo.

-`python manage.py createsuperuser`: usu: Martin o admin contra: 123456 o 123, Crea un super usario que maneja todo, nos permite entrar y usar el "admin" que se encuentra en config dentro del modulo urls.py. El path('admin/') que es la ruta se recomienda que sea otro lo mismo la usuario y contraseña porque eso permite hackear la pagina o lo creado.

- luego para ver los clientes creados mediante un template en HTML, hay que crear la carpeta "templates", dentro otra con el mismo nombre de la app ("cliente") y por ultimo crear el modulo "index.html", dentro escribiremos el codigo en HTML.

- Templates: es lo que se ve.

- views.py: es la informacion que se pasa a los templates

- modelos.py: es la parte de nuestro proyecto que almacena, borra, modifica y manipula el caudal principal de los datos, apoyandose en una base de datos, sql o demas.