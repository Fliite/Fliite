#import a function from deflis file
#deflis is in the same folder

import L from deflis.py

def sort_list_up(L):
    for i in L:
        if L[i+1] < L[i]:
            k = L[i]
            L[i] = L[i+1]
            L[i+1] = k
            #pas bon
        else :
            pass
    return L

def sort_list_down(L):
    for i in L:
        if L[i+1] > L[i]:
            k = L[i]
            L[i] = L[i+1]
            L[i+1] = k
            #bon
        else :
            pass
    return L

def main():
    m = int(input("longueur liste: "))
    L = list(m)
    Lup = sort_list_up(L)
    Lown = sort_list_down(L)
    print(L, Lup, Lown)
if __name__ == "__main__":
    main()