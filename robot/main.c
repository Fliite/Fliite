 #include "MeAuriga.h"  //bibliotheque 
 #include "Wire.h" //bi

MeColorSensor colorsensor(PORT_6); 

void setup()
{
  Serial.begin(9600);
  colorsensor.begin();
}

void loop():
{
  int r = colorsensor.readRed(); // variable = lecture de la couleur rouge
  int g = colorsensor.readGreen();
  int b = colorsensor.readBlue();
  int c = colorsensor.readClear(); // variable = lecture de la luminosité totale
  Serial.print("R = ");
  Serial.print(r);
  Serial.print(" G = ");
  Serial.print(g);
  Serial.print(" B = ");
  Serial.print(b);
  Serial.print(" C = ");
  Serial.print(c); 
  delay(1000); // revie les valeurs toutes les 1 seconde
}

// cree un ficher texte avec le nom de la couleur et la valeur de la couleur

void file_color()
{
  // create my file
  


  if (r > 100 && g < 100 && b < 100)
  {
    Serial.println("Red");
    File myFile = SD.open("Red.txt", FILE_WRITE);
    myFile.println(r);
    myFile.close();
  }
  if (r < 100 && g > 100 && b < 100)
  {
    Serial.println("Green");
    File myFile = SD.open("Green.txt", FILE_WRITE);
    myFile.println(g);
    myFile.close();
  }
  if (r < 100 && g < 100 && b > 100)
  {
    Serial.println("Blue");
    File myFile = SD.open("Blue.txt", FILE_WRITE);
    myFile.println(b);
    myFile.close();
  }
  if (r < 100 && g < 100 && b < 100)
  {
    Serial.println("Black");
    File myFile = SD.open("Black.txt", FILE_WRITE);
    myFile.println(c);
    myFile.close();
  }
  if (r > 100 && g > 100 && b > 100)
  {
    Serial.println("White");
    File myFile = SD.open("White.txt", FILE_WRITE);
    myFile.println(c);
    myFile.close();
  }
}