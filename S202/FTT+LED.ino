#include "arduinoFFT.h"
 
#define SAMPLES 128             //SAMPLES-pt FFT. Must be a base 2 number. Max 128 for Arduino Uno.
#define SAMPLING_FREQUENCY 2048 //Ts = Based on Nyquist, must be 2 times the highest expected frequency.
 
arduinoFFT FFT = arduinoFFT();
 
unsigned int samplingPeriod;
unsigned long microSeconds;
 
double vReal[SAMPLES]; //create vector of size SAMPLES to hold real values
double vImag[SAMPLES]; //create vector of size SAMPLES to hold imaginary values

bool sequenceDetected = false;
bool do3;
bool re3;
bool mi3;
 
void setup() 
{
    Serial.begin(115200); //Baud rate for the Serial Monitor
    samplingPeriod = round(1000000*(1.0/SAMPLING_FREQUENCY)); //Period in microseconds
    pinMode(LED_BUILTIN, OUTPUT);
    pinMode(2, OUTPUT);
    pinMode(3, OUTPUT);
    pinMode(4, OUTPUT);
    pinMode(5, OUTPUT);
    pinMode(6, OUTPUT);
    pinMode(7, OUTPUT);
    pinMode(8, OUTPUT);
    pinMode(9, OUTPUT);
    pinMode(10, OUTPUT);
}
 
void loop() 
{  
    /*Sample SAMPLES times*/
    for(int i=0; i<SAMPLES; i++)
    {
        microSeconds = micros();    //Returns the number of microseconds since the Arduino board began running the current script. 
     
        vReal[i] = analogRead(0); //Reads the value from analog pin 0 (A0), quantize it and save it as a real term.
        vImag[i] = 0; //Makes imaginary term 0 always

        /*remaining wait time between samples if necessary*/
        while(micros() < (microSeconds + samplingPeriod))
        {
          //do nothing
        }
    }
 
    /*Perform FFT on samples*/
    FFT.Windowing(vReal, SAMPLES, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
    FFT.Compute(vReal, vImag, SAMPLES, FFT_FORWARD);
    FFT.ComplexToMagnitude(vReal, vImag, SAMPLES);

    /*Find peak frequency and print peak*/
    double peak = FFT.MajorPeak(vReal, SAMPLES, SAMPLING_FREQUENCY);
    Serial.println(peak);     //Print out the most dominant frequency.

    if (peak >= 147 && peak <= 149){
      digitalWrite(2,HIGH);
    }else{
      digitalWrite(2,LOW);
    }
    if (peak >= 166 && peak <= 168){
      digitalWrite(3,HIGH);
    }else{
      digitalWrite(3,LOW);
    }
    if (peak >= 176 && peak <= 179){
      digitalWrite(4,HIGH);
    }else{
      digitalWrite(4,LOW);
    }
    if (peak >= 197 && peak <= 199){
      digitalWrite(5,HIGH);
    }else{
      digitalWrite(5,LOW);
    }
    if (peak >= 223 && peak <= 225){
      digitalWrite(6,HIGH);
    }else{
      digitalWrite(6,LOW);
    }
    if (peak >= 251 && peak <= 253){
      digitalWrite(7,HIGH);
    }else{
      digitalWrite(7,LOW);
    }
    if (peak >= 266 && peak <= 268){
      digitalWrite(8,HIGH);
    }else{
      digitalWrite(8,LOW);
    }
    if (peak >= 299 && peak <= 331){
      digitalWrite(9,HIGH);
    }else{
      digitalWrite(9,LOW);
    }
    if (peak >= 335 && peak <= 338){
      digitalWrite(10,HIGH);
    }else{
      digitalWrite(10,LOW);
    }
    /*detection de la combinaison de note*/
   if (!sequenceDetected)
  {
    if (peak >= 266 && peak <= 268)
    {
      do3 = true;
    }
    else if (peak >= 335 && peak <= 338 && do3)
    {
      mi3 = true;
    }
    else if (peak >= 299 && peak <= 331 && do3 && mi3)
    {
      re3 = true;
    }
    else
    {
      do3 = false;
      mi3 = false;
      re3 = false;
    }

    if (do3 && mi3 && re3)
    {
      sequenceDetected = true;
      digitalWrite(LED_BUILTIN, HIGH); // Allumer la LED intégrée
    }
  }
  else
  {
    if (!(peak >= 266 && peak <= 268 && do3 && mi3 && re3))
    {
      sequenceDetected = false;
      digitalWrite(LED_BUILTIN, LOW); // Éteindre la LED intégrée
    }
  }
}
