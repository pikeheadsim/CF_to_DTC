# CombatFlit to Data Transfer Cartridge
Simple program to upload waypoints in DCS from CombatFlite XML exported files
similar to:  https://github.com/the-paid-actor/dcs-dtc
With only waypoints, allows to import every flight from the .xml


## Installation
The program is using the same interface as dcs-dtc if you already use that you can skype point one.

1. Copy the DCSDTC.lua file into ...\Saved Games\DCS\Scripts
and add the next line to  ...\Saved Games\DCS\Scripts\Export.lua

local DCSDTClfs=require('lfs'); dofile(DCSDTClfs.writedir()..'Scripts/DCSDTC.lua')

2. Just run the .exe file
