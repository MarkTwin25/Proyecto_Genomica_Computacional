# Buscador de Fagos 

Este es un proyecto para la materia de Genomica Computacional que consiste en una interfaz grafica para el programa phispy.

![Logo](https://github.com/MarkTwin25/Proyecto_Genomica_Computacional/blob/main/Logo.png "Logo")

## Integrantes del equipo:
 
⚡️ Rosas Marín Jesús Martín

💬 Salmerón Gómez Sebastián

👯‍♀️ Integrante

😄 Integrante

🤔 Integrante

## Instalación y manera de ejecutarlo

Primero debemos de tener clonado e instalado en nuestro sistema phispy, que se descarga desde [Phispy](http://https://github.com/linsalrob/PhiSpy "Phispy")

Despues descargamos nuestro repositorio con:
```bash
git clone https://github.com/MarkTwin25/Proyecto_Genomica_Computacional.git
```
Lo que debemos hacer es meter nuestro archivo Interfaz.py dentro de la carpeta generada de phispy, nos movemos hasta ese directorio.
```bash
cd Phispy
```
Y ejecutamos el siguiente comando:
```bash
python3 Interfaz.py
```

## Capturas de la app y comparación con phispy.

Vamos a ejecutar el siguiente comando para realizar una busqueda predeterminada:

```bash
PhiSpy.py -o Streptococcus.phages Streptococcus_pyogenes_M1_GAS.gb
```
donde Streptococcus.phages es la ruta del archivo de salida y Streptococcus_pyogenes_M1_GAS.gb e snuestro archivo genbank de entrada.
Es decir, nuestro input debe ser de la manera:

```bash
PhiSpy.py -o carpeta_salida archivo_genbank
```
De manera similar existen variantes dependiendo que funcionalidad busques en phispy.

![Phispy original](https://github.com/MarkTwin25/Proyecto_Genomica_Computacional/blob/main/Phispy_terminal.png "Phispy original")

Ahora veamos nuestra app:

![App](https://github.com/MarkTwin25/Proyecto_Genomica_Computacional/blob/main/Presentacion_app.png "App")

Debemos elegir un archivo GenBank
![Busqueda de Archivos](https://github.com/MarkTwin25/Proyecto_Genomica_Computacional/blob/main/Busqueda_archivos.png "Busqueda de Archivos")

Podemos ver que tenemos 3 botones que simulan el comportamiento de phispy original pero sin tener aprenderte los distintos comandos de phispy.
Ahora veamos el resultado de la misma instruccion ejecutada en terminal, pero ahora en nuestra app.

![Prueba app](https://github.com/MarkTwin25/Proyecto_Genomica_Computacional/blob/main/Prueba_app.png "Prueba app")

Veamos que el resultado es el mismo. Ahora notemos que cuando hacemos una busqueda predeterminada, el programa nos realiza la busqueda con 5 metricas, mas adelante hablaremos de ellas. Pero en el caso de que solo se desee hacer la busqueda con una metrica especifica, podemos hacerlo desde la app.

![Metricas](https://github.com/MarkTwin25/Proyecto_Genomica_Computacional/blob/main/Metricas.png "Metricas")

### Metricas

## Licencia y aplicacion Phispy original
https://github.com/linsalrob/PhiSpy
