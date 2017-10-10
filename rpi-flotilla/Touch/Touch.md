# Touch
De 'Touch'-module is een module die 4 touch knoppen bevat. Deze knoppen zijn genummerd van 1 tot 4. Iedere knop kan je appart aanspreken.

# Touch aanspreken
1. Verbind de 'Touch'-module met het Dock.
2. Definieer het dock: `dock = flotilla.Client()`
3. Definieer de 'Touch'-module: `touch = dock.first(flotilla.Touch)`

# Touch knoppen aanspreken

`
if touch.one:
	print("Button 1 pressed!")
`

`
if touch.two:
	print("Button 2 pressed!")
`

`
if touch.three:
	print("Button 3 pressed!")
`

`
if touch.four:
	print("Button 4 pressed!")
`