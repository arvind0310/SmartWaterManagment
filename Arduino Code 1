const int trig =10;
const int echo =9;
 const int button = 7;
long duration;
int distance;
char userip;
char ON,OFF;
void setup() {
 pinMode(trig,OUTPUT);
 pinMode(echo,INPUT);
  pinMode(7,INPUT);
   pinMode(3,OUTPUT);
    pinMode(4,OUTPUT);
    pinMode(5,OUTPUT);
 
 Serial.begin(9600);
void loop() {
  if (Serial.available())
  {
    userip=Serial.read();
  switch (userip)
  {
   case '1':
   {
digitalWrite(trig,LOW);
delayMicroseconds(2);
digitalWrite(trig,HIGH);
delayMicroseconds(10);
digitalWrite(trig,LOW);
duration=pulseIn(echo,HIGH);
distance=duration*0.03475/2;
//Serial.print("distance");
Serial.println(distance);
if(distance<=15)//water level 15 cm
  {Serial.println("FULL");
   delay(1000);
