# Number
De 'Number'-module is een digitale display waarmee je waarden kunt tonen, zoals tijd, countdown, calculaties, ...

![number](/rpi-flotilla/assets/number.png)

# Number aanspreken
1. Verbind de 'Light'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Light'-module: `number = dock.first(flotilla.Number)`

# Een nummer displayen
```python
dock = flotilla.Client()
number = dock.first(flotilla.Number)

number.set_number(99)
```

# Voorbeeld
Het bestand `number.py` illustreert een voorbij waarbij je het `Dock` en de `Number`-module voor nodig hebt.