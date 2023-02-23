def tribulle(L):
    K = len(L)
    for i in range(K):
        for j in range(i, K):
            if L[i] > L[j]:
                L[i], L[j] = L[j], L[i]
    return L