L = [3,5,1,6,2,4,7]

#L est la liste, i et j sont les indices de debut et de fin de la liste
#le pivot est le premier element de la liste
def partition(L,i,j):
    for k in L:
        if k < L[0]:
            

print(partition(L,0,6))