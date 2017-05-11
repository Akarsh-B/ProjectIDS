#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<Servo.h> //Arduino Nano + Pan & Tilt Assembly

Servo pan,tilt; //Basic Servo object declaration
int pan_position=90,tilt_position=60; // Initialize pan and tilt positions
int pan_value=0,tilt_value=0;
const int lf = 2;
const int lb = 3;
const int rf = 4;
const int rb = 5;

void motors(int inputLF,int inputLB,int inputRF,int inputRB);
void servo(int pan_value, int tilt_value);

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  char *token;
  int count = 0;
  int inputs[4];

  // Here I've got the strings from the arguments
  // On the Arduino, you'll have to read the serial port
  // And generate the String as follows

  // // Max Input Size Expected
	#define INPUT_SIZE 30
  // // Get next command from Serial (add 1 for final 0)
  	char input[INPUT_SIZE + 1];
    byte size = Serial.readBytes(input, INPUT_SIZE);
  // // Add the final 0 to end the C string
    input[size] = 0;


  // Duplicating a string (you can't modify a character array in place in C)
  // You can do the same in C++ and hence this is not required on the Arduino

  token = strtok(input, ",");
  
  while (token != NULL) 
  {
    inputs[count] = atoi(token);
    count++;
    token = strtok(NULL, ",");
  }
  if (count == 4) {
  	motors(inputs[0],inputs[1],inputs[2],inputs[3]);
  	delay(1000);
}
  else if (count == 2) {
    // Call servos with input[0] and input[1]
    servo(inputs[0],inputs[1]);
    delay(1000);
  }
  delay(1000);
}

void motors(int inputLF,int inputLB,int inputRF,int inputRB)
{  
  analogWrite(lf, inputLF);
  analogWrite(lb, inputLB);
  analogWrite(rf, inputRF);
  analogWrite(rb, inputRB);
}

void servo(int pan_value, int tilt_value)
{
  pan.attach(9); // Attach Pan Servo to pin 9
  tilt.attach(10); // Attach Tilt Servo to pin 10 
	pan.write(pan_value);         
  tilt.write(tilt_value); 
  delay(500);
  pan.detach(); // Attach Pan Servo to pin 9
  tilt.detach(); // Attach Tilt Servo to pin 10
  }
