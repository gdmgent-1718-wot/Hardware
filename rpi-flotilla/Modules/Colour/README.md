# Colour
De 'Colour'-module detecteert RGB-kleur, evenals omgevingslichtniveau. Het heeft ook twee heldere witte LED's om objecten te zien waarvan de kleur wordt gedetecteerd.

![colour](/rpi-flotilla/assets/colour.png)

# Colour aanspreken
1. Verbind de 'Colour'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Colour'-module: `colour = dock.first(flotilla.Colour)`