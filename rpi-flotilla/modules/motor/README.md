# Motor
De 'Motor'-module is een sensor waarmee je lichtniveau kan waarnemen.

![motor](/rpi-flotilla/assets/motor.png)

# Motor aanspreken
1. Verbind de 'Motor'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Motor'-module: `motor = dock.first(flotilla.Motor)`

# Voorbeeld
Het bestand `motor.py` illustreert een voorbij waarbij je het `Dock` en de `Motor`-module voor nodig hebt.