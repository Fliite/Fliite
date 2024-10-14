Liste1 = [1, 2, 3, 4, 5]
Liste2 = [1, 2, 3, 4, 5]

def verifie_liste(A, B):
    if len(A) != len(B):
        return False
    else:
        for i in range(len(A)):
            if A[i] != B[i]:
                return False
        return True
    
print(verifie_liste(Liste1, Liste2))