flotte = {
12 : {"type" : "E", "etat" : 1, "station" : "Prefecture"},
80 : {"type" : "C", "etat" : 0, "station" : "Saint-Leu"},
45 : {"type" : "C", "etat" : 1, "station" : "Baraban"},
41 : {"type" : "C", "etat" : 1,"station" : "Citadelle"},
26 : {"type" : "C", "etat" : 1, "station" : "Coliseum"},
28 : {"type" : "E", "etat" : 0, "station" : "Coliseum"},
74 : {"type" : "E", "etat" : 1, "station" : "Jacobins"},
13 : {"type" : "C", "etat" : -1, "station" : "Citadelle"},
83 : {"type" : "C", "etat" : 1,"station" : "Saint-Leu"},
22 : {"type" : "E", "etat" : 1,"station" : "Joffre"},
12 : {"type" : "E", "etat" : 1, "station" : "Prefecture"},
98 : {"type" : "C", "etat" : 1, "station" : "Saint-Leu"},
23 : {"type" : "C", "etat" : -1, "station" : "Baraban"},
61 : {"type" : "E", "etat" : 1,"station" : "Citadelle"},
34 : {"type" : "C", "etat" : 1, "station" : "Coliseum"},
}

def disponibles(flotte):
    L = []
    #renvoie la liste des vélos disponibles (état = 1)
    for i in flotte:
        if flotte[i]["etat"] == 1:
            L.append(i)
    return L

def station(nom_station, flotte):
    #renvoie la liste des vélos disponibles à la station nom_station (modifier le main)
    L = []
    for i in flotte:
        if flotte[i]["station"] == nom_station:
            L.append(i)
    return L

def PasEnPanne(flotte):
    #renvoie l'identifiant et la station du vélo qui n'est pas en panne
    for i in flotte:
        if flotte[i]["etat"] != -1 and flotte[i]["type"] == "E":
            print(i, flotte[i]["station"])
    return ""
        
def disponible_par_station(flotte):
    #renvoie le dictionnaire qui associe le nombre de vélos disponibles pour chaque station
    #station : cle et nombre de velos : valeur
    D = {}
    for i in flotte:
        if flotte[i]["etat"] == 1:
            if flotte[i]["station"] in D:
                D[flotte[i]["station"]] += 1
            else:
                D[flotte[i]["station"]] = 1
    return D


#appel des fonctions 
def main(flotte):
    print('les velos disponibles sont', disponibles(flotte),'\n')
    print('les velos disponibles en station sont', station("Saint-Leu", flotte),'\n')
    print("les velos éléctriques qui ne sont pas en panne sont : ")
    print(PasEnPanne(flotte))
    print("les velos disponibles par station sont : ")
    print(disponible_par_station(flotte))


#appel du main
if __name__ == '__main__':
    main(flotte)