from matplotlib import pyplot as plt

def graph(X,Y):
    plt.plot(X,Y,markersize=1,markerfacecolor='red',marker='X',linestyle= 'None')
    plt.ylabel('Y')
    plt.xlabel('random numbers')
    plt.savefig('graph.png',dpi = 400)

def graph2(X,Z):
    plt.title('graph 2 : compte')
    plt.bar(X,Z)
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.savefig('graph2.png',dpi = 400)