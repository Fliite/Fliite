from random import randint

L = [randint(-110, 100) for i in range(10)]
k = 12

def tri_insertion(L):
    for i in range(1, len(L)):
        j = i
        while j > 0 and L[j] < L[j-1]:
            L[j],L[j-1] = L[j-1],L[j]
            j = j - 1
    return L


def insert(L1,k):
    for i in range(len(L1)):
        if k < L1[i]:
            L1.insert(i,k)
            break
    return L1