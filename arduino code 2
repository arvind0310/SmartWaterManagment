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
  pinMode(7,OUTPUT);
   pinMode(3,OUTPUT);
    pinMode(4,OUTPUT);
    pinMode(5,OUTPUT);
 
 Serial.begin(9600);


 

 
}

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
//Serial.println(distance);
if(distance<=15)//water level 15 cm
  {Serial.println("FULL");
  digitalWrite(7,LOW);
   delay(1000);
}
else if(distance<=25)
{Serial.println("MEDIUM");
digitalWrite(7,LOW);
}
else if(distance>=25)
{Serial.println("VERY LOW");
 digitalWrite(7,HIGH);
}
  break; }
Serial.print("Enter command");
  case'3':
 {
  digitalWrite(3,HIGH);//motor on off 
 break;}
 case'4':
 {
  digitalWrite(3,LOW);//motor on off 
 break;}
