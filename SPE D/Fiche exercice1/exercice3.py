def DistanceHamming(seq1, seq2):
    l = []
    listePos = []
    if len(seq1) != len(seq2):
        raise ValueError("Les deux séquences doivent avoir la même longueur")
    else:
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                l.append(seq1[i])
                listePos.append(i)
        return len(l), listePos

print(DistanceHamming("ATG4TG", "ATGCTA"))