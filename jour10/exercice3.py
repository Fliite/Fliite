chaine = "RbresTaPNpVXgUfIuHJhztMAnDGKyqBSZcdYLvOojFQlWikxCmwE"

def Carac_occurence(string):
    # creer un dico qui associe chaque lettre a son nombre d'occurence dans la chaine
    dico = {}
    for i in string:
        if i not in dico:
            dico[i] = 1
        else:
            dico[i] += 1
    return dico

print(Carac_occurence(chaine))