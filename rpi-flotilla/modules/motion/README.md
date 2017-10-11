# Motion
De 'Motion'-module is een sensor die beweging waarneemt in een 3D-assenstelsel.

![motion](/rpi-flotilla/assets/motion.png)

# Motion aanspreken
1. Verbind de 'Motion'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Motion'-module: `motion = dock.first(flotilla.Motion)`
4. x, y en z-waarden oproepen: 
    - x-waarde detecteren: `motion.x`
    - y-waarde detecteren: `motion.y`
    - z-waarde detecteren: `motion.z`
5. Als laatste kan je ook de heading aanspreken: `motion.heading`

# Voorbeeld
Het bestand `motion.py` illustreert een voorbij waarbij je het `Dock` en de `Motion`-module voor nodig hebt.