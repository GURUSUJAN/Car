#include<Servo.h>
int led_red=13;
int pos=90;
int led_yellow=12;
int led_white=11;
int buzzer=8;
int motor=5;
int trig_front=2;
int echo_front=4;
int trig_port=1;
int echo_port=0;
int trig_starboard=6;
int echo_starboard=7;
int distance_front=0,sure_front=0;
int distance_port=0,sure_port=0;
int distance_starboard=0,sure_starboard=0;
Servo rear;
void setup()
{
  pinMode(led_red,OUTPUT);
  pinMode(led_yellow,OUTPUT);
  pinMode(buzzer,OUTPUT);
  pinMode(motor,OUTPUT);
  pinMode(trig_starboard,OUTPUT);
  pinMode(trig_port,OUTPUT);
  pinMode(trig_front,OUTPUT);
  pinMode(echo_starboard,INPUT);
  pinMode(echo_port,INPUT);
  pinMode(echo_front,INPUT);
  rear.attach(3);
}
void loop()
{
  
 //For Front view
 digitalWrite(trig_front,LOW);
 delayMicroseconds(2);
 digitalWrite(trig_front,HIGH);
 delayMicroseconds(10);
 digitalWrite(trig_front,LOW);
 sure_front = pulseIn(echo_front,HIGH);
 distance_front = (sure_front/2)/29.0;
 
 //For Port
 digitalWrite(trig_port,LOW);
 delayMicroseconds(2);
 digitalWrite(trig_port,HIGH);
 delayMicroseconds(10);
 digitalWrite(trig_port,LOW);
 sure_port = pulseIn(echo_port,HIGH);
 distance_port = (sure_port/2)/29.0;
  
 //For Starboard
 digitalWrite(trig_starboard,LOW);
 delayMicroseconds(2);
 digitalWrite(trig_starboard,HIGH);
 delayMicroseconds(10);
 digitalWrite(trig_starboard,LOW);
 sure_starboard = pulseIn(echo_starboard,HIGH);
 distance_starboard = (sure_starboard/2)/29.0;
 
 //Main algo for Front
 if(distance_front<=150)
 {
  digitalWrite(led_red,1);
 // digitalWrite(led_yellow,0);
  digitalWrite(buzzer,0);
  delay(2000);
  if(distance_front<=150)
  {
    digitalWrite(buzzer,1);
    delay(20);
    digitalWrite(buzzer,0);
    delay(20);
  }
 }
 else if(distance_front>150)
 {
  digitalWrite(led_red,0);
  //digitalWrite(led_yellow,1);
  digitalWrite(buzzer,0);
  digitalWrite(motor,1);
 }
 //Main algo for Starboard
 if(distance_starboard<=150)
 {
   digitalWrite(12,1);
   delay(100);
  for(pos=0;pos<45;pos++)
  {
    rear.write(pos);
    delay(10);
  }
  delay(1000);
  for(pos=45;pos>0;pos--)
  {
    rear.write(pos);
    delay(10);
  }
   digitalWrite(12,0);
 }
 //Main algo for Port
 if(distance_port<=150)
 {
   digitalWrite(11,1);
   delay(100);
  for(pos=0;pos>315;pos--)
  {
    rear.write(pos);
    delay(10);
  }
  delay(1000);
  for(int pos=315;pos<0;pos++)
  {
    rear.write(pos);
    delay(10);
  }
   digitalWrite(11,0);
 }
}
