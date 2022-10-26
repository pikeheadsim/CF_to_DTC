# CombatFlit to Data Transfer Cartridge
Simple program to upload waypoints in DCS from CombatFlite XML exported files

Simplified version of:  ``https://github.com/the-paid-actor/dcs-dtc``

## Installation
The program is using the same interface with DCS as dcs-dtc if you already use that you can skip point one.

1. Copy the DCSDTC.lua file into ...\Saved Games\DCS\Scripts
and add the next line to  ...\Saved Games\DCS\Scripts\Export.lua

local DCSDTClfs=require('lfs'); dofile(DCSDTClfs.writedir()..'Scripts/DCSDTC.lua')

2. Just run **CF_to_DTC.exe**

## Features

*. Allows to open the CombatFlite file, the number of flights and callsigns is shown in the screen.
*. You can generate Json files that can be uploaded in DCS-DTC in case you want to use the extra features there. 
*. You can chose the plane and click upload, if all is good the wayponts will be entering (don't touch any key while this happens) 
*. Is allowed the use of precision coordinates. 

## Limitations

For now only the FA-18, next F-16C and next, I guess A10II

# CombatFlit al cartucho de transferencia de datos
Sencillo programa para cargar waypoints en DCS desde archivos XML exportados con CombatFlite.
Versión simplificada de: [https://github.com/the-paid-actor/dcs-dtc]

## Instalación
El programa usa la misma interfaz que dcs-dtc, si ya lo tienes instalado puede ignorar el punto 1.

1. Copia el archivo DCSDTC.lua en ...\Juegos guardados\DCS\Scripts
y agregua la siguiente línea a ...\Juegos guardados\DCS\Scripts\Export.lua

local DCSDTClfs=require('lfs'); dofile(DCSDTClfs.writedir()..'Scripts/DCSDTC.lua')

2. Simplemente ejecuta el archivo **CF_to_DTC.exe**

## Características

* Permite abrir el archivo CombatFlite, el número de vuelos y los callsigns de los vuelos se muestran en la pantalla.
* Puede generar archivos Json que se pueden cargar en DCS-DTC en caso de que desee utilizar las funciones adicionales allí.
* Puede elegir el avión y hacer clic en cargar, si todo está bien, los wayponts se van metiendo(no le des a ninguna tecla durante el proceso).
* Se pueden introducir las coordenadas de precisión.

## Limitaciones

Por ahora solo el FA-18, el próximo F-16C y el siguiente, supongo que A10II.
