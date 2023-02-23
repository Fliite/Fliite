L1 = [10,30,15,-22,200,120,85,90,-62,-22,56,-13]
L2 = [10,30,15,-22,2,120,85,90,-62,-22,56,-13]

def fcompare(L1, L2):
    for i in range(len(L1)):
        if L1[i] < L2[i]:
            print(L1[i],"est plus petit que",L2[i],"à l'index",i)
            break
        elif L1[i] > L2[i]:
            print(L1[i],"est plus grand que",L2[i],"à l'index",i)
            break
        else:
            pass
    return

fcompare(L1, L2)