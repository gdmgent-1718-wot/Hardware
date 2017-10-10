# Light
De 'Light'-module is een sensor waarmee je lichtniveau kan waarnemen.

![light](/rpi-flotilla/assets/light.png)

# Light aanspreken
1. Verbind de 'Light'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Light'-module: `light = dock.first(flotilla.Light)`
4. Het lichtniveau aanspreken: `lightlevel = light.light`

# Voorbeeld
Het bestand `light.py` illustreert een voorbij waarbij je het `Dock` en de `Light`-module voor nodig hebt.




