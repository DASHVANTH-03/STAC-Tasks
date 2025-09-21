# Sensor Inputs in Tinkercad 
In this task,I learnt about photoresistor(LDR) and how analog input works in Arduino basics using Tinkercad by Simulateing a LED on/off depending on brightness of LDR sensor.

### Procedure
- The [circuit](circuit.png) connection was made.
- In programming terminal [code](code.ino) was implemented.

### Theory:
Photoresistor(LDR): resistance offered is inversely proportional to the amount of light shined in it<br>
input pinmode : reads the voltage applied to the device,by default it doesn't has any stationary value therefore it must by initialised manually in the hardware<br>
pull down resistance : comes handy in initialising the stationary value of input pin.<br>
Analog input : no HIGH or LOW,can take any value in the range 0-1023

###  Result:
The LED glowed according to the intensity of light falling on the LDR.

## Things learnt
- LDR basics
- how Analog input works in arduino
