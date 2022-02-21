# ComerciosEmpleados

Migracion a FastAPI del proyecto realizado en Django. En este proyecto sean realizado las siguientes funciones:

![Listado de funciones](https://github.com/vicogarcia16/ComerciosEmpleados/blob/master/capturas/1.JPG)


## Instalación


Crear un entorno virtual si se desaa y ejecutar archivo requirements.txt


## Ejecución del software

* Ejecutar el comando uvicorn main:app --reload
* Posteriormente acceder a la url por defecto [127.0.0.1:8000], algunas funciones de los cruds no requieren autorización.
* Para tener autorización sobre algunos elementos del crud protegidos, ingresar con usuario y contraseña [mg_619@hotmail.com:admin] o registrar otro usuario. Esto se realiza, 
para recibir el token de acceso (Nota: Dicho token caduca a los 10 minutos)

![Ingresar usuario](https://github.com/vicogarcia16/ComerciosEmpleados/blob/master/capturas/2.JPG)
* Dar clic al botón [Authorize] y pegar el token en el input de tipo texto

![Ingresar token](https://github.com/vicogarcia16/ComerciosEmpleados/blob/master/capturas/3_.JPG)

## Construido con

* [Python] (https://www.python.org/)Lenguaje de programación
* [FastAPI] (https://fastapi.tiangolo.com/)Framework Web
* [SQL Alchemy] (https://www.sqlalchemy.org/)Kit de herramientas SQL para Python
* [JWT] (https://jwt.io/)Verificación de acceso con tokens

## Autor

* Víctor Manuel García Negrete
