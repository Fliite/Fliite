 #include "MeAuriga.h"
 #include "Wire.h"
 #include <RVB_convert.c>


 MeColorSensor colorsensor(PORT_6);

uint8_t colorresult;
uint16_t r=0,g=0,b=0,c=0;
uint8_t grayscale = 0;
long systime = 0,colorcode=0; //ce sont des variables longues 
void setup()
{
  Serial.begin(115200); //ouvre le port série sur la bande 115200
  colorsensor.SensorInit(); //démarre le capteur de couleur
  systime = millis(); //initialise le temps en millisecondes
}

void loop() 
{
  // doit rentrer le code ici obligatoirement
  if(millis()-systime>200)// marque une pause de 200ms
  {
    systime = millis();
    colorresult = colorsensor.Returnresult();
    r = colorsensor.ReturnRedData();
    g = colorsensor.ReturnGreenData();
    b = colorsensor.ReturnBlueData();
    c = colorsensor.ReturnColorData();
    colorcode = colorsensor.ReturnColorCode();//RGB24code
    grayscale  = colorsensor.ReturnGrayscale();

    //implémente la fonction de conversion de couleur
    liste = ConvertToWavelength(r, g, b, c);

    //affiche les valeurs de couleur dans le moniteur série
    Serial.print("R:");
    Serial.print(r);
    Serial.print("\t");
    Serial.print("G:");
    Serial.print(g);
    Serial.print("\t");
    Serial.print("B:");
    Serial.print(b);
    Serial.print("\t");
    Serial.print("C:");
    Serial.print(c);
    Serial.print("\t");
    Serial.print("color:");
    
    switch(colorresult)
    {
      case BLACK:
      Serial.print("BLACK");
      break;
      case BLUE:
      Serial.print("BLUE");
      break;
      case YELLOW:
      Serial.print("YELLOW");
      break;
      case GREEN:
      Serial.print("GREEN");
      break;
      case RED:
      Serial.print("RED");
      break;
      case WHITE:
      Serial.print("WHITE");
      break;
      default:
      break;    
     }
    Serial.print("\t");
    Serial.print("code:");
    Serial.print(colorcode,HEX);
    Serial.print("\t");
    Serial.print("grayscale:");
    Serial.println(grayscale);
  }
}