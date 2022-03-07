tutorial_wagtail_final
Descripción
Web de datos realizada con Wagtail. En ella podemos ver el listado de las 250 mejores películas según IMDb,viajes, hoteles y noticias en general.



¿Cómo lo instalo y hago funcionar?
Windows
(ATENCIÓN) Deberemos tener en nuestro ordenador la aplicación "GitBash" u otra del estilo para que el cmd reconozca los comandos de Git, y Python.

Nos posicionamos donde queramos tener la capeta en el cmd (con cd)
Copiamos el enlace del repositorio git donde está el trabajo.
Nos posicionamos dentro del proyecto en el cmd (con cd)
Creamos el entorno virtual (py -m venv env)
Activamos el entorno virtual (env\Scripts\activate)
Instalamos los requisitos (pip install -r requirements.txt)
Dentro del entorno: py manage.py runserver
En google buscamos: http://localhost:8000/ (número indicado al ejecutar el runserver (Starting development server at http://127.0.0.1:8000/) ese es el 8000)
Cuando queramos pararlo: Ctrl + c (en el cmd)
Linux/Mac
(ATENCIÓN) Deberemos tener en nuestro ordenador la aplicación "GitBash" u otra del estilo para que el cmd reconozca los comandos de Git, y Python.

Nos posicionamos donde queramos tener la capeta en el cmd (con cd)
Copiamos el enlace del repositorio git donde está el trabajo
En el cmd escribimos: git clone https://github.com/johannague/tutorial_wagtail_final.git
Nos posicionamos dentro del proyecto en el cmd (con cd)
Creamos el entorno virtual (python3 -m venv env)
Activamos el entorno virtual (source tutorial-env/bin/activate)
Instalamos los requisitos (pip install -r requirements.txt)
Dentro del entorno: py manage.py runserver
En google buscamos: http://localhost:8000/ (número indicado al ejecutar el runserver (Starting development server at http://127.0.0.1:8000/) ese es el 8000)
Cuando queramos pararlo: Ctrl + c (en el cmd)
