L = [42,15,19,64,-7,54,-16,23,0,6,5,-3,4,5,89,7,8,9,10,-11,12,13,14]

#faire un tri par insertion

def tri_insertion(L):
    for i in range(1,len(L)):
        x = L[i]
        j = i
        while j>0 and L[j-1]>x:
            L[j] = L[j-1]
            j = j-1
        L[j] = x
    return L

#faire un tri par sélection

def tri_selection(L):
    for i in range(len(L)):
        min = i
        for j in range(i+1,len(L)):
            if L[j]<L[min]:
                min = j
        L[i],L[min] = L[min],L[i]
    return L

print(tri_insertion(L))
print(tri_selection(L))