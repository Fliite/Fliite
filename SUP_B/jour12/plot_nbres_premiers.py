#on plote une grande partie des nombres premiers
#on utilise la fonction est_Premier() seuleent 

from matplotlib import pyplot as plt

def est_Premier(n):
    #Renvoie True si n est premier, False sinon
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def premiers(n):
    #Renvoie la liste des nombres premiers inférieurs ou égaux à n
    liste = []
    for i in range(2, n + 1):
        if est_Premier(i):
            liste.append(i)
    return liste

def plot():
    #plot les nombres premiers
    liste = premiers(10000)
    plt.plot(liste, linewidth=0.1, color = "red")
    plt.savefig("plot_nbres_premiers.png", dpi = 1000)
    plt.show()

plot()