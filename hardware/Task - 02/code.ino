// C++ code
//
void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(A0, INPUT);
}

void loop()
{
  Serial.println(analogRead(A0));
  delay(300);
  if(analogRead(A0)>511){
  	digitalWrite(LED_BUILTIN, HIGH);
  	delay(1000); // Wait for 1000 millisecond(s)
  }
  else{
  	digitalWrite(LED_BUILTIN, LOW);
  	delay(1000); // Wait for 1000 millisecond(s)
  }
}