# Flotilla
Onderdeel van het werkcollege WoT

## Info
- Contributors: **Niels Capelle & Ismail Kutlu**
- Opleidingsonderdeel: **Web Of Things**
- Academiejaar: **2017-2018**
- Opleiding: **Bachelor in de Grafische en Digitale Media**
- Afstudeerrichting: **New Media Development**
- Opleidingsinstelling: **Arteveldehogeschool**

## Setup Raspberry Pi
> More information: https://www.raspberrypi.org/documentation/setup/

## Connect Flotilla with Raspberry Pi and docks
![dock-setup](/rpi-flotilla/assets/dock-setup.png)

## Installatie
1. Ga naar de map /home/pi: 
```
cd ../home/pi
```
2. Maak in `/home/pi` de map `Libaries` aan: 
```
mkdir Libaries
```
3. Ga naar de map `Libaries`:
```
cd Libaries
```
4. Kloon volgende github repo via de terminal: 
```
git clone https://github.com/pimoroni/flotilla-python
```
5. Ga naar de map `flotilla-python`: 
```
cd flotilla-python
```
6. Als je de bestanden in deze map oplijst merk je op dat er een bestand `setup.py` aanwezig is. Deze moeten we uitvoeren aan de hand van volgend commando: 
```
sudo python3 setup.py
```

De installatie is nu afgerond.

## Errors?
### Update software in Raspbian
```
sudo apt-get dist-upgrade
```
### Stop service flotilla
Soms krijg je foutmeldingen bij het uitvoeren van python scripts, dan kan je volgende scripts uitvoeren:
```
sudo service flotillad stop
```

## Imports
Om aan de slag te kunnen gaan met Flotilla met je bovenaan je code de Flotilla Libary importeren: `import flotilla`

## Modules
Flotilla bevat verschillende modules: 
`Rainbow`, `Touch`, `Motion`, `Number`, `Colour`, `Light`, `Matrix`, `Barometer`, `Joystick`, `Dial`, `Slider`, `Motor` en `Bits`

Al deze modules kun je aansluiten op het `Dock`. Om in je code aan de slag te gaan met de bovenstaande modules moet je eerst het `Dock` aanspreken: 

`dock = flotilla.Client()`

Daarna kan je module aanspreken. We nemen de `Weather`module als voorbeeld: 

`weather = dock.first(flotilla.Weather)`

Verdere documentatie kan u per module vinden via `https://github.com/pimoroni/flotilla-python/tree/master/documentation`.
