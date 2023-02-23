from random import randint

def deflis(length, mini, maxi):
    L = []
    for i in range(length):
        L.append(randint(mini, maxi))
    print(L)
    return L