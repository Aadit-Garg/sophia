int input = 4;

void setup() {
  Serial.begin(9600);
  pinMode(input,INPUT);
}

void loop() {
  int sensorReading = digitalRead(input);
  Serial.println(sensorReading);
  delay(2000);
}
