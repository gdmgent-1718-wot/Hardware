# Matrix
De 'Matrix'-module is een LED display waarmee iedere LED apart kan instellen

![matrix](/rpi-flotilla/assets/matrix.png)

# Matrix aanspreken
1. Verbind de 'Matrix'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Matrix'-module: `matrix = dock.first(flotilla.Matrix)`
4. Definieer een pixel: `matrix.set_pixel(x, y, state)`
5. Update de ingestelde pixel: `matrix.update()`

# Voorbeeld
Het bestand `matrix.py` illustreert een voorbij waarbij je het `Dock` en de `Matrix`-module voor nodig hebt.