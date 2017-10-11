# Rainbow
De 'Rainbow'-module is een LED-strook met 5 LED's. Je kan ieder LED apart programmeren.

![rainbow](/rpi-flotilla/assets/rainbow.png)

# Motor aanspreken
1. Verbind de 'Rainbow'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Rainbow'-module: `rainbow = dock.first(flotilla.Rainbow)`
4. Een LED instellen (pixel 0 = de eerste pixel): `rainbow.set_pixel(0, 255, 255, 255)`
5. Alle LED's tegelijk instellen (De laatste waarde staat voor de lichtsterkte): `rainbow.set_all(255, 255, 0, 1)`
6. De rainbow updaten na het instellen van een LED: `rainbow.update`

# Voorbeeld
Het bestand `rainbow.py` illustreert een voorbij waarbij je het `Dock` en de `Rainbow`-module voor nodig hebt.