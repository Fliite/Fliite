def factoriel(n):
    if n < 0:
        return "Erreur"
    elif n == 0:
        return 1
    else:
        return n * factoriel(n - 1)


def sort(l):
    #par recursivité
    if len(l) == 1:
        return l
    else:
        return sort([l[0]]) + sort(l[1:])
    

def dichotomie(L, valeur):
    #par dichotomie
    if len(L)==1:
        if L[0] == valeur:
            return True
        return False
    elif valeur > L[len(L//2)]:
        dichotomie(L[L//2:], valeur)
    else:
        dichotomie(L[:L//2],valeur)

def palindrome(str):
    if len(str) == 1:
        return True
    else:
        