def ajouter(notes,Etudiants):
    nouveau = input('ajoutez un Etudiant, suel est son nom ?')
    note_n = int(input('quelle est sa note ?'))
    while note_n < 0 or note_n > 20:
        note_n = int(input('quelle est sa note ?'))
    Etudiants.append(nouveau)
    notes.append(note_n)


def moyenne(notes):
    som = 0
    for i in range(len(notes)):
        som += notes[i]    
    moy = som/len(notes)
    print('la moyenne est', moy)

    
def tri(Etudiants,notes):
    recales = []
    admis = []
    i=0
    lenliste = len(Etudiants)
    while i < lenliste:
        if notes[i] < 10 and notes[i] > 0:
            print(Etudiants[i],'a eu ', notes[i],': il est recalé')
            recales.append(Etudiants[i])
        elif notes[i] == 0 :
            Etudiants.pop(i)
            lenliste = lenliste-1
            print("on jette l'etudaiant", Etudiants[i],"il a eu zero")
        else: 
            print(Etudiants[i],'a eu ', notes[i],': il est admis')
            admis.append(Etudiants[i])
        i += 1

def main():
    Etudiants = ['pierre', 'paul', 'jacques', 'marie', 'jean', 'marc', 'lucie', 'luc', 'louis', 'louise']
    notes = [10, 12, 8, 15, 9, 11, 13, 14, 16, 17]
    print('bienvenue dans le programme de gestion des notes')
    print('1- ajouter un etudiant')
    print('2- afficher la moyenne')
    print('3- afficher les etudiants admis et recales')
    print('4- quitter')
    choix = int(input('quel est votre choix ?'))
    while choix != 4:
        if choix == 1:
            ajouter(notes,Etudiants)
        elif choix == 2:
            moyenne(notes)
        elif choix == 3:
            tri(Etudiants,notes)
        else:
            print('choix incorrect')
        print('1- ajouter un etudiant')
        print('2- afficher la moyenne')
        print('3- afficher les etudiants admis et recales')
        print('4- quitter')
        choix = int(input('quel est votre choix ?'))



if __name__ == '__main__':
    main()