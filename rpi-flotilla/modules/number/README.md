# Number
De 'Number'-module is een digitale display waarmee je waarden kunt tonen, zoals tijd, countdown, calculaties, ...

![number](/rpi-flotilla/assets/number.png)

# Number aanspreken
1. Verbind de 'Number'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Number'-module: `number = dock.first(flotilla.Number)`
4. Definieer een nummer: `number.set_number(1234)`

# Voorbeeld
Het bestand `number.py` illustreert een voorbij waarbij je het `Dock` en de `Number`-module voor nodig hebt.