# CombatFlite to Data Transfer Cartridge
Simple program to upload waypoints in DCS from CombatFlite XML exported files. 
CombatFlite is a widelly used tool to plan missions in DCS and this code is intended to provide direct data transfer cartridge capabilities from CombatFlite exported files.

It's using the lua files from (dcs-dtc):  [https://github.com/the-paid-actor/dcs-dtc] based en [https://github.com/aronCiucu/DCSTheWay/tree/main/src]

If you have dcs-dtc installed this should work out of the box, just run CF_to_DTC.exe. The prgram can also export the .json files 
compatible with dct-dtc in case you want to use the extra features available there.  

## Installation
If you already use DCS-DTC skip point one.

1 Copy the DCSDTC.lua file into ``...\Saved Games\DCS\Scripts``
and add the next line to  ``...\Saved Games\DCS\Scripts\Export.lua``

``local DCSDTClfs=require('lfs'); dofile(DCSDTClfs.writedir()..'Scripts/DCSDTC.lua')``

2 Just run **CF_to_DTC.exe**

## Features

* Allows to open CombatFlite xml exported file, the number of flights and callsigns can be shown in the screen.
* You select the flight and airplane and click upload, the wayponts should start entering (don't touch any key while this happens) 
* Precision coordinates can be used.  
* You can generate Json files that can be uploaded in DCS-DTC in case you want to use the extra features there. 

## Limitations

 * For now only the FA-18 is implemented, next probably the F-16C and next, I guess A10II?

# De CombatFlit al Cartucho

Programa sencillo para cargar waypoints en DCS desde archivos XML exportados de CombatFlite.
CombatFlite es una herramienta ampliamente utilizada para planificar misiones en DCS y este código está destinado a proporcionar la funcionalidad de DTC de forma directa para los vuelos.  

El codigo usa los archivos .lua de (dcs-dtc): [https://github.com/the-paid-actor/dcs-dtc] basado en [https://github.com/aronCiucu/DCSTheWay/tree/main/src]
Si tienes instalado dcs-dtc, debería funcionar simplemente ejecutando CF_to_DTC.exe, el código también puede exportar los archivos .json
compatible con dct-dtc en caso de que desee utilizar las opciones adicionales disponibles allí pero importando las rutas de CombatFlite.

## Instalación
El programa usa la misma interfaz que dcs-dtc, si ya lo tienes instalado puedes ignorar el punto 1.

1 Copia el archivo DCSDTC.lua en ``...\Juegos guardados\DCS\Scripts``
y agregua la siguiente línea a ``...\Juegos guardados\DCS\Scripts\Export.lua``

``local DCSDTClfs=require('lfs'); dofile(DCSDTClfs.writedir()..'Scripts/DCSDTC.lua')``

2 Simplemente ejecuta el archivo **CF_to_DTC.exe** donde quieras. 

## Características

* Permite abrir el archivo CombatFlite, el número de vuelos y los callsigns de los vuelos se muestran en la pantalla.
* Puedes escoger el avión y el numero de vuelo y dar click en "Load", si todo funciona los wayponts se van metiendo(no le des a ninguna tecla durante el proceso).
* Puedes generar archivos Json que se pueden cargar en DCS-DTC en caso de que quieras utilizar las funciones adicionales allí.
* Se pueden introducir las coordenadas de precisión.

## Limitaciones

* Por ahora solo el FA-18 esta implementado, el próximo seguramente F-16C y el siguiente, igual A10II?
