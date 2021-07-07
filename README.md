##API EN FLASK

###Configuración Inicial
IMPORTANTE: _Tener instalado el gestor de paquetes de Python llamado pip_

Ejecutar el siguiente comando en la consola:
* pip install flask flask_restful flask_sqlalchemy flask_migrate flask_marshmallow marshmallow-sqlalchemy

###Iniciar proyecto
Podes iniciar el proyecto de dos formas:
* Sobre el directorio ejecutar en una consola el comando -> flask run
* O sino, con Pycharm ejecutar el archivo entrypoint.py

Después de ejecutar la API se te creará en sqlite la base de datos.

###¿Cómo se que la API está funcionando?

Es importante tener instalado un programa que realice requests http,
como por ejemplo POSTMAN.

Después de iniciar POSTMAN, dentro de su UI, vas a tener que configurar
el request y ejecutarlo.

_La api va a estar de forma local en la URL **localhost:5000/api**_