from random import randint

def deflis(length, mini, maxi):
    L = [randint(mini, maxi) for i in range(length)]
    return L

print(deflis(10, 0, 100))