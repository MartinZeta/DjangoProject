"""
#- git branch: no dice cuantas ramas tenemos creadas.

#- git branch dev(rama nueva desarrollo): crea una rama nueva o, en este caso, un entorno virtual.

#- git checkout dev(rama nueva desarrollo): nos mueve a la rama que creamos.

#- git log --oneline: nos sirve para saber a donde esta apuntando (HEAD-CABEZA), si es a la rama principal, a la de desarrollo y al origin que seria github

#- git merge dev: Une las ramas, de desarrollo con la principal para guardar todos los cambios en la principal, antes que nada hay que moverse a la rama princi.

#- git pull
"""

### Entornos virtuales ###

"""
Un entorno virtual en Python es una herramienta 
que te permite crear un espacio aislado donde puedes instalar 
y manejar las dependencias (bibliotecas y versiones de Python) 
específicas para un proyecto en particular, sin afectar al sistema global de Python.
"""

#Como crear un entorno virtual? (entorno aislado del global)


#- pip list : 
"""
muestra las biblotecas instaladas en el entorno virtual o GLOBAL.
"""

#- python -m venv .venv : 
"""
Crea el entorno virtual. 
Antes de hacer el entorno virtual, se debe crear un modulo llamado dentro de el escribir .venv (.gitignore:
le dice a git que no suba este paquete o archivo a internet que lo ignore.)
"""

#Como activar el entorno virtual?

#.\.venv\Scripts\activate : 
"""
con este comando activamos el entorno virtual.
"""

#--------------------------------------------------------------------------------


#### Instalar Django en entorno virtual? ####

""" 
Esto permite que en este entorno solo quede una version que Django o otros paquetes que instalemos
y si salen actualizaciones que no proboque un error. ¡¡¡¡¡Tambien tiene que estar activo el entorno virtual!!!!, esto para que no lo instale en otro entorno.
"""

## Comandos

#pip install django:
"""instala el paquete django para usar los templates y comandos del mismo."""

"""Creamos la carpeta Proyectodjango"""

#-cd Proyectodjango: 
"""
Luego hay que moverse a la carpeta que creamos, en este caso, Proyectodjango
"""

#django-admin --version:
"""Nos dice la version de django"""

#python -m django startproject Proyectodjango: Ejecutar en terminal
"""Crea la carpeta (Proyectodjango)
Con las configuraciones de django y el modulo manage.py para poder trabajar."""

"""Manage nos ayuda a interactuar con nuestro proyecto con algunos comandos muy simples. Ademas
Lo que genera este comando de primeras es un archivo manage, que es el encargado de casi todo lo que queramos solicitarle al proyecto, 
y una carpeta con los archivos iniciales necesarios para iniciar con configuraciones básicas."""

#python manage.py migrate: 
"""Migra todo a una server de django y nos brinda una url"""

#python manage.py runserver: 
"""Nos crea y corre el servidor en internet"""

#Crtl + C: 
"""para salir del server y usar la terminal"""