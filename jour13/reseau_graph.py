from tkinter import *

monReseau = {'A' : [('A', 1), ('B', 2), ('C', 3)], 'B' : [('A', 1), ('B', 2), ('C', 3)], 'C' : [('A', 1), ('B', 2), ('C', 3)]}


#display the network in tkinter

def coordinates(monReseau):
    for i in monReseau:
        for j in monReseau[i]:
            print(50*ord(i), 50*ord(j[0])

def afficherReseau(monReseau):
    fenetre = Tk()
    fenetre.title("Reseau")
    canvas = Canvas(fenetre, width=1000, height=1000, bg='white')
    canvas.pack(side=LEFT, padx=5, pady=5)


    for i in monReseau:
        for j in monReseau[i]:
            
            #red dot for each node
            canvas.create_oval(50*ord(i)-10, 50*ord(j[0])-10, 50*ord(i)+10, 50*ord(j[0])+10, fill='red')
            #line between the nodes
            canvas.create_line(50*ord(i), 50*ord(j[0]), 50*ord(i), 50*ord(j[0]), fill='black', width=2)
            #weight of the edge
    fenetre.mainloop()

afficherReseau(monReseau)