# Comercios-Empleados

Migracion a FastAPI del proyecto [comerciosempleados](https://github.com/alfaro28/comerciosempleados) realizado por [alfaro28](https://github.com/alfaro28) en Django. En este proyecto sean realizado las siguientes funciones:

![Listado de funciones](https://github.com/vicogarcia16/ComerciosEmpleados/blob/master/capturas/1.JPG)

## Instalaci贸n 馃敡

* Crear un entorno virtual para Python si se desea y ejecutar el archivo requirements.txt
* La base de datos se encuentra en SQLite con el nombre [comercios_database.db]

## Ejecuci贸n del software 鈿欙笍

* Ejecutar el comando en cmd o terminal [uvicorn main:app --reload]
* Posteriormente acceder a la url por defecto [127.0.0.1:8000], algunas funciones de los cruds no requieren autorizaci贸n.
* Para tener autorizaci贸n sobre algunos elementos del crud protegidos, ingresar con usuario y contrase帽a [mg_619@hotmail.com:admin] o registrar otro usuario. Esto se realiza, 
para recibir el token de acceso (Nota: Dicho token caduca a los 10 minutos)

![Ingresar usuario](https://github.com/vicogarcia16/ComerciosEmpleados/blob/master/capturas/2.JPG)
* Dar clic al bot贸n [Authorize] y pegar el token en el input de tipo texto

![Ingresar token](https://github.com/vicogarcia16/ComerciosEmpleados/blob/master/capturas/3_.JPG)

## Construido con 馃洜锔?

* [Python](https://www.python.org/) - Lenguaje de programaci贸n
* [SQLite](https://www.sqlite.org/index.html) - Base de datos
* [FastAPI](https://fastapi.tiangolo.com/) - Framework Web
* [SQL Alchemy](https://www.sqlalchemy.org/) - Kit de herramientas SQL para Python
* [JWT](https://jwt.io/) - Verificaci贸n de acceso con tokens

## Autor 鉁掞笍

* **V铆ctor Garc铆a** [vicogarcia16](https://github.com/vicogarcia16) 
