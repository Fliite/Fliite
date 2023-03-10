// rgb : rouge, vert, bleu et c : chroma
void ConvertToWavelength(r, g, b, c)
{
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
    if max == 0 or max-min == 0;
    {
        int sat = 0;
        int hue = 0;
        return;
    }
    else
    {
        //estimer la saturation
        int sat = (max - min) / max;

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
    return [hue, sat, max];
}
