# Aplicación para la planificación de las encuestas FRONTUR-Canarias del ISTAC.


![coverage](https://github.com/borjaguanchesicilia/tfg/blob/master/coverage.svg)


## Información:

* Se ha desarrollado una aplicación con interfaz gráfica (GUI) que permite llevar a cabo la planificación de encuestas FRONTUR-CANARIAS que realiza el Instituto Canario de Estadística (ISTAC). Esta aplicación tiene implementado un modelo matemático de optimización con el que se consigue obtener una planificación óptima de vuelos a encuestar, cumpliendo con los requisitos mínimos impuestos. Para resolver el problema se da la posibilidad de emplear un solucionador gratuito (COIN-OR CBC) y otro de pago (Gurobi).

* Este proyecto forma parte del Trabajo de Fin de Grado (TFG) en Ingeniería Informática por la Universidad de La Laguna.

* **Autor:** Borja Guanche Sicilia

* **Correo electrónico:** bg.sicilia@gmail.com | alu0101205908@ull.edu.es

* **Año:** 2022


## Requisitos:

* La aplicación puede ser utilizada tanto en Windows como en GNU/Linux, por lo que se dispone de dos ejecutables para que pueda ser utiliza por cada uno de los sistemas operativos:

	* **Versión Windows:** [Link](https://github.com/borjaguanchesicilia/tfg_aplicacion/tree/master/Version%20Windows "Versión Windows")
	* **Versión GNU/Linux:** [Link](https://github.com/borjaguanchesicilia/tfg_aplicacion/tree/master/Version%20para%20GNU%20Linux "Versión GNU/Linux")


* Se necesitan las siguientes librerias:
 
	* **[tkinter](https://docs.python.org/es/3/library/tkinter.html "tkinter")**
	* **[tkcalendar](https://pypi.org/project/tkcalendar/ "tkcalendar")**
	* **[os](https://docs.python.org/3/library/os.html "os")**
	* **[numpy](https://numpy.org/ "numpy")**
	* **[pandas](https://pandas.pydata.org/ "pandas")**
	* **[math](https://docs.python.org/3/library/math.html "math")**
	* **[datetime](https://docs.python.org/3/library/datetime.html "datetime")**
	* **[functools](https://docs.python.org/3/library/functools.html "functools")**
	* **[threading](https://docs.python.org/es/3.10/library/threading.html "threading")**
	* **[pulp](https://pypi.org/project/PuLP/ "pulp")**

* **Si se quiere utilizar el solucionador de Gurobi se necesita tener una licencia instalada y verificada.**


## Modo de uso:

* Para poder utilizar la aplicación es un requisito indispensable disponer de un fichero Geslot de AENA (se puede ver un ejemplo en el siguiente [Link](https://github.com/borjaguanchesicilia/tfg/blob/master/ficheros/geslot_marzo_22.csv "Fichero Geslot")) y un fichero con los modelos de aviones comerciales que operan hoy en día (se puede ver un ejemplo en el siguiente [Link](https://github.com/borjaguanchesicilia/tfg/blob/master/ficheros/aviones.csv "Fichero aviones")).

* La aplicación cuenta con tres secciones, donde cada una de las cuales se activará o desactivará en función del paso en que se encuentre el usuario. Estas secciones son las siguientes:

    * **Paso 1:** Ventana desde donde el usuario introduce los parámetros de configuración del problema, que son los siguientes:
        * **Jornada laboral máxima:** 1 - 8 horas
        * **Descanso entre vuelos:** 10 - 60 minutos
        * **Velocidad de encuestas:** 0.10 - 1 minutos
        * **Ocupación:** 10 - 100 %
        * **Éxito:** 10 - 100 %
        * **Aeropuertos de origen:** Lanzarote, Fuerteventura, Gran Canaria, Tenerife Norte, Tenerife Sur y La Palma
        * **Días en los que se realizará la encuesta**

    * **Paso 2:** Ventana desde donde el usuario introduce los ficheros necesarios. Estos ficheros son los siguientes:
        * **Fichero GESLOT de AENA**
        * **Fichero con los modelos de aviones**

    * **Paso 3:** Ventana desde donde el usuario introduce las configuraciones para el solucionador, que son las siguientes:
        * **Función objetivo a emplear:** Neutral, Priorizando el empleo de dos encuestadores, penalizando el empleo de un encuestador.
        * **Solucionador a invocar:** CBC (gratuito) o Gurobi (con licencia)

* Como se mencionó anteriormente, para desbloquear cada uno de los pasos se deben de completar de manera correcta los pasos anteriores. Para ello, se ha desarrollado un sistema de comprobación para que los parámetros que se vayan a introducir al modelo sean los correctos.


## Ejecutar tests

* python3.6 script_pruebas.py