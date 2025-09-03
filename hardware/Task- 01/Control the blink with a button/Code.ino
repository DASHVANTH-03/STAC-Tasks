// C++ code
//
void setup()
{
  pinMode(5,INPUT);
  pinMode(13,OUTPUT);
}

void loop()
{
  int state = digitalRead(5);
    if (state == HIGH)
    {
      digitalWrite(13, HIGH);
      delay(1000); // Wait for 1000 millisecond(s)
      digitalWrite(13, LOW);
      delay(1000); // Wait for 1000 millisecond(s)
    }
  delay(10); // Delay a little bit to improve simulation performance
}