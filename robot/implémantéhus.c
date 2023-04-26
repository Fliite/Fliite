MeColorSensor colorsensor(PORT_6);

uint8_t colorresult;
uint16_t redvalue=0,greenvalue=0,bluevalue=0,colorvalue=0;
uint16_t r=0,g=0,b=0,c=0, sat = 0, hue = 0;
uint8_t grayscale = 0;
long systime = 0,colorcode=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  colorsensor.SensorInit();//
  systime = millis();
}

void loop() 
{
  // put your main code here, to run repeatedly:
  if(millis()-systime>200) //attendre 1 seconde
  {
    systime = millis();
    colorresult = colorsensor.Returnresult();
    redvalue   = colorsensor.ReturnRedData();
    greenvalue = colorsensor.ReturnGreenData();
    bluevalue  = colorsensor.ReturnBlueData();
    colorvalue = colorsensor.ReturnColorData();
    colorcode = colorsensor.ReturnColorCode();//RGB24code
    grayscale  = colorsensor.ReturnGrayscale();

    redvalue = r;
    greenvalue = g;
    bluevalue = b;
    colorvalue = c;

    //vérifier si les valeurs sont entre 0 et 255, || = ou
    if (r < 0 || r > 255 || g < 0 || g > 255 || b < 0 || b > 255)
    {
        return;
    }

    //calculer la valeur maximale de r,g,b
    int max = r;
    if (g > max)
    {
        max = g;
    }
    if (b > max)
    {
        max = b;
    }

    //calculer la valeur minimale de r,g,b
    int min = r;
    if (g < min)
    {
        min = g;
    }
    if (b < min)
    {
        min = b;
    }
    
    //cas limite exclus
    if (max == 0 | max-min == 0)
    {
        return;
    }
    else
    {
        //estimer la saturation
        int sat = (max - min) / (max);

        //estimer la chroma
        int chroma = max - min;

        //compare la couleur estimée avec sa valeur de référence
        int Dchoma = chroma - c;
        //pour reference

        //déduire la position de la couleur dans le cercle chromatique
        int hue = 0;
        if (chroma == 0)
        {
            hue = 0;
        }
        else if (max == r)
        {
            hue = 60 * ((g - b) / chroma);
        }
        else if (max == g)
        {
            hue = 60 * ((b - r) / chroma) + 120;
        }
        else if (max == b)
        {
            hue = 60 * ((r - g) / chroma) + 240;
        }
    }
    if (hue < 0)
    {
        hue = hue + 360;
    }
    hue = hue / 2;
    sat = sat * 255;
    max = max * 255;
    
    Serial.print("R:"); // affichage
    Serial.print(redvalue);
    Serial.print("\t");
    Serial.print("G:");
    Serial.print(greenvalue);
    Serial.print("\t");
    Serial.print("B:");
    Serial.print(bluevalue);
    Serial.print("\t");
    Serial.print("C:");
    Serial.print("\t");
    Serial.print("color:");
    

  }
}