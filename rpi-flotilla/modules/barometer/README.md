# Barometer
De 'Barometer'-module of 'Weather'-module is een sensor die de temperatuur (in °C) en de luchtdruk (in hPa) kan meten.

![barometer](/rpi-flotilla/assets/barometer.png)

# Barometer aanspreken
1. Verbind de 'Barometer'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Barometer'-module: `barometer = dock.first(flotilla.Barometer)`
4. Bepaal de temperatuur: `temperature = barometer.temperature`
4. Bepaal de luchtdruk: `pressure = barometer.pressure`


# Voorbeeld
Het bestand `barometer.py` illustreert een voorbij waarbij je het `Dock` en de `Barometer`-module voor nodig hebt.