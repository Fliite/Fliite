L = [10,30,15,-22,200,120,85,90,-62,-22,56,-13]

def derivative(L):
    K = []
    for i in range(len(L)-1):
        if L[i] < L[i+1]:
            K.append(1)
        elif L[i] > L[i+1]:
            K.append(-1)
        else:
            K.append(0)
    return K

def main():
    print(derivative(L))

if __name__ == "__main__":
    main()