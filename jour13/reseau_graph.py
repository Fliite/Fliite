from tkinter import *

monReseau = {'A':[('B',4),('C',8)], 'B':[('A',4),('C',2),('D',5)], 'C':[('A',8),('B',2),('D',6),('E',9)], 'D':[('B',5), ('C',6),('E',3)], 'E':[('C',9),('D',3)], 'F':[('G',2)], 'G':[('F',2)]}



#display the network in tkinter

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