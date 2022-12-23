#include <IRremote.h>

int redPin = 10;
int bluePin = 11;
int greenPin = 9;
int recvPin = 13;

IRrecv irrecv(recvPin);

void setup() 
{
  // put your setup code here, to run once:

  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
}

void loop() 
{
  // put your main code here, to run repeatedly:

}
