# Tinkercad Basics
In this task,I learnt Arduino basics in tinkercad by Simulate a simple LED blink using Arduino and Control the blink with a button.


## Simulate a simple LED blink using Arduino:

### Procedure
- The [circuit](Simulate%20a%20simple%20LED%20blink%20using%20Arduino/circuit.png) connection was made.
- In programming terminal [code](Simulate%20a%20simple%20LED%20blink%20using%20Arduino/code.ino) was implemented.

### Theory:
**output voltage of digital pin** : 5v<br>
**current rating of LED** : 20 mA<br>
**voltage rating of LED** : 2v<br>
**resistance is required in series with LED(r)**<br>
using kirchoff loop rule<br>
5 = (0.02 x r) + 2<br>
r = 150 Ω<br>

###   result:
The LED blinked
 
## Control the blink with a button:
  - The [circuit](Control%20the%20blink%20with%20a%20button/Circuit.png) connection was made.
  - In programming terminal [code](Control%20the%20blink%20with%20a%20button/Code.ino) was implemented.

### Theory:
In input mode the pin has no specific voltage,therefore the pin should be connected to GND for LOW and 5v for High.<br>
Pull down Resistor : resistor connected between a digital pin and GND to ensure that the pin reads LOW,it in the order of kΩ to block the flow of current through GND

###   result:
The LED started blinking when button was ON.

## Things Learnt:
#### Pin In Output Mode,
- HIGH of digital pin : 5v<br>
- LOW of digital pin : 0v<br>
- Maximum current : 40 mA<br>
#### Pin In Input mode,
- Pin has No specific voltage<br>
- Pull Down Resistor
