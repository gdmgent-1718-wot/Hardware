# Slider
De 'Slider'-module is een potentiometer met 5 LED's in de vorm van een slider. De schaal van deze slider ligt tussen 0 en 1023.

![slider](/rpi-flotilla/assets/slider.png)

# Slider aanspreken
1. Verbind de 'Slider'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Slider'-module: `slider = dock.first(flotilla.Slider)`
4. Bepaal de positie: `slider.position`

# Voorbeeld
Het bestand `slider.py` illustreert een voorbij waarbij je het `Dock` en de `Slider`-module voor nodig hebt.