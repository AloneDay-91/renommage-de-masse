import os
from tkinter import *


def callback():
    label2 = Label(fenetre, text="Veuillez choisir le type de fichier")
    label2.pack()
    liste = Listbox(fenetre)
    liste.insert(1, ".jpg")
    liste.insert(2, ".jpeg")
    liste.insert(3, ".png")
    liste.pack()
    bouton = Button(fenetre, text="Suivant", width=10, command=callback2)
    bouton.pack()

def callback2():
    label2 = Label(fenetre, text="Voulez vous continuer ?")
    label2.pack()
    bouton1 = Button(fenetre, text="Suivant", width=10, command=callbackres)
    bouton1.pack()
    bouton2 = Button(fenetre, text="Annuler", width=10)
    bouton2.pack()

def callbackres():
    labelres = Label(fenetre, text=res)
    labelres.pack()

fenetre = Tk()
fenetre.geometry("400x600")

label = Label(fenetre, text="Insérer l'adresse pour le renommage")
label.pack()
entree = Entry(fenetre, textvariable=str, width=30)
entree.pack()
bouton = Button(fenetre, text="Suivant", width=10 , command=callback)
bouton.pack()


fenetre.mainloop()

folder = entree
count = 1

for file_name in os.listdir(folder):
    source = folder + file_name

    destination = folder + "image_" + str(count) + Listbox
    os.renames(source, destination)
    count += 1
print('Nouveaux Noms :')
res = os.listdir(folder)
print(res)