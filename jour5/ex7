L = [10,30,15,-22,200,120,85,90,-62,-22,56,-13]

def sort_list_up(L):
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i] < L[j]:
                k = L[i]
                L[i] = L[j]
                L[j] = k
            else :
                pass
    return L

L2 = sort_list_up(L)

def add_x(L, x):
    L.append(x)
    L2 = sort_list_up(L)
    return L2

L3 = add_x(L2, -89)

print(L3)