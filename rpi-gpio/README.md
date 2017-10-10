# Raspberry Pi **GPIO**
## Ilona Zancaner & Sander Van Damme

#### Handige links
- [GPIO pins schema](https://i.stack.imgur.com/sVvsB.jpg)
- [BMP280 Sensor Tutorial](http://faradaysclub.com/?p=1325)
- [Breadboard?](https://cdn.shopify.com/s/files/1/0176/3274/files/Breadboard_Remarked_grande.png?15033584625641436291)

---

## LED lichtje linken aan de GPIO van de Raspberry Pi

#### Benodigheden
- Breadboard
- 2 F/M Jumper Wires
- Weerstand van ongeveer 400 Ohm
- LED lichtje

#### Samenstellen
Bekijk het schema van de GPIO pins eerst ([GPIO pins schema](https://i.stack.imgur.com/sVvsB.jpg))
Het circuit bestaat uit een stroomtoevoer (de Pi), een LED die brandt wanneer de stroom wordt aangelegd en een weerstand om de stroom te beperken die door het circuit stroomt.

We gebruiken één van de **ground (GND)** pinnen als 0 volt-eind van een batterij. Het **positieve** einde van de batterij wordt geleverd door een **GPIO-pin**.
Je kan vrij kiezen welke pin je gebruikt. Voor dit voorbeeld gebruiken we pin 18 (zie schema).

**LET OP** We gebruiken Pin 18, dit wil zeggen **GPIO018 (PCM_CLK)**, NIET physical nummer 18 (deze is dan GPIO24)!

Connecteer nu de draden zoals in de afbeelding hieronder.
Één van de F/M Jumper Cables gaat naar de ground en verbind je met de kleine poot van het LED lichtje (negatieve kant).
De andere F/M Jumper Cable gaat naar **GPIO pin 18** en verbind je met de weerstand.
De weerstand verbind je dan van de Jumper Cable naar de lange poot van de LED (positieve kant).

Belangrijk om te weten: de hoeveelheid Volt die een GPIO pin meegeeft is 3V3 (3.3V)

![alt text](https://github.com/AngryMoustache/RaspberryPi/blob/master/images/gpioledlampje.jpg "GPIO LED Lampje")

#### Python code
Tijd om code te schrijven.
Maak een nieuw .py bestand aan, wij gebruikten de naam **LED.py**.

We beginnen met de imports. In dit voorbeeld hebben we **time** en **RPi.GPIO** nodig. **time** zal ons vanzelfsprekend enkele functies aanbieden die te maken hebben met tijd. In dit voorbeeld zal dat de time.sleep() functie zijn. **RPi.GPIO** levert ons de functies om onder andere de input en output van ons GPIO panel te kunnen aanspreken.

```python
import time
import RPi.GPIO as GPIO
```

Hierna configureren we de GPIO:
```python
led_output = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_output, GPIO.OUT)
```
Voor **GPIO.setmode(GPIO.BCM)** kan je ook **GPIO.setmode(GPIO.BOARD)** gebruiken, dan gebruik je de physical pinnummers ipv de **GPIOXX** nummering. Tot zover hebben we nog geen verschil gemerkt dus je kan het eventueel beide eens uittesten. Houdt wel rekening met de nummering!

Als laatste schrijven we nog een kleine loop waarin de LED aan en uit gaat:
```python
led = False

while True:
	# toggle LED
	led = not led

	# Zet de LED aan of uit
    	GPIO.output(led_output, led)
    
	# Sleep a bit
    	time.sleep(0.5)
```

Hier nog eens de volledige code:
```python
import time
import RPi.GPIO as GPIO

led_output = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_output, GPIO.OUT)

led = False

while True:
	# toggle LED
	led = not led

	# Zet de LED aan of uit
   	GPIO.output(led_output, led)
    
	# Sleep a bit
    	time.sleep(0.5)
```

Probeer nu eens een politie sirene te maken met een rood en een blauw LED lichtje ;)

## Externe button input linken aan de GPIO van de Raspberry Pi

#### Benodigdheden
- Breadboard
- 2 F/M Jumper Wires
- Button

#### Samenstellen
Zo goed als hetzelfde als bij een LED lichtje, maar ipv een LED gebruiken we een button.
Voor dit voorbeeld gebruiken we pin **GPIO04** voor de button.

![alt text](http://razzpisampler.oreilly.com/images/rpck_1102.png "Button")

#### Python
De code hier is ook grotendeels hetzelfde, maar ipv een **output (GPIO.OUT)** doen we nu een **input (GPIO.IN)**.
De setup van een input verloopt iets anders dan een output.
```python
button = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN, pull_up_down = GPIO.PUD_UP)
```
Elke GPIO pin heeft software configureerbare pull-up en pull-down weerstanden. Als je een GPIO-pin gebruikt als invoer, kan je de weerstanden configureren, zodat één ofwel geen van de weerstanden is ingeschakeld, met behulp van de **pull_up_down** parameter in de GPIO.setup. Als die parameter wordt weggelaten, dan zal geen weerstand worden ingeschakeld. Als het op **GPIO.PUD_UP** is ingesteld, is de pull-up resistor ingeschakeld. Als het is ingesteld op **GPIO.PUD_DOWN**, is de pull-down resistor ingeschakeld.

Om te kijken of de knop wel of niet is ingedrukt doen we het zo:
```python
input_state = GPIO.input(button)
```

**LET OP** Omdat we **GPIO.PUD_UP** gebruiken, zal input_state **False** returnen als de button ingedrukt is, en **True** als hij niet ingedrukt word.
