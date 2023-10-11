L = [10,30,15,-22,200,120,85,90,-62,-22,56,-13]

def pluspetit(L):
    pluspetit = L[0]
    for i in range(len(L)):
        if L[i] < pluspetit:
            pluspetit = L[i]
            index = i
        else:
            pass
        
    return pluspetit, index

print(pluspetit(L))