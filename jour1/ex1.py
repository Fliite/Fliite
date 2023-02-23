from random import randint

def randlist(length, min, max):
    return [randint(min, max) for i in range(length)]