#compte le nb d'elements de la liste 
def count(L):
    K = [0 for i in range(len(L))]
    for j in L:
        K[j] += 1
    return K