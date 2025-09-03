# Tinkercad Basics
In this task,I learnt Aurdino basics in tinkercad by Simulate a simple LED blink using Arduino and Control the blink with a button.

## Simulate a simple LED blink using Arduino:

### Attempt 1
- I connected the cathode of LED directly to the ground port in aurdino and the anode to digital pin 13.
- In programming terminal I set pin 13 to output mode and inside loop block i configured pin 13 to high,wait 1 sec,pin 13 to low
**result**
  The LED shorted as the current through it was higher(50 mA) than its rated value(20 mA)
**Inference**
  output voltage of digital pin : 5v
  current rating of LED : 20 mA
  voltage rating of LED : 2v
  resistance is required in series with LED
  using kirchoff loop rule
  5 = (0.02 x r) + 2
  r = 150 Ω

### Attempt 2
- I connected the cathode of LED directly to the ground port in aurdino and the anode to digital pin 13 with 150 Ω resistor in series.
- In programming terminal I set pin 13 to output mode and inside loop block i configured pin 13 to high,wait 1 sec,pin 13 to low
**result**
  The LED blincked without shorting
 
## Control the blink with a button:
  


## Outcome: Familiarity with Arduino simulation.
