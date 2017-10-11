# Joystick
De joystick module is een analoge joystick met een klikknop. Het is ideaal om te gebruiken als spel controller, of om een ​​robot te bedienen. Met een joystick kan je iets laten bewegen in een assenstelsel (x & y).

![joystick](/rpi-flotilla/assets/joystick.png)

## Joystick aanspreken
1. Verbind de 'Joystick'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Joystick'-module: `joystick = dock.first(flotilla.Joystick)`
4. x -en y-waarden oproepen: 
    - x-waarde detecteren: `joystick.x`
    - y-waarde detecteren: `joystick.y`

# Voorbeeld
Het bestand `joystick.py` illustreert een voorbij waarbij je het `Dock` en de `Joystick`-module voor nodig hebt.