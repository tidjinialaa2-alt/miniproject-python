#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

def calculer():
    try:
        val1 = float(entry1.get())
        val2 = float(entry2.get())
        resultat = (val1 - val2) / val1  # exemple simple de calcul
        lbl_result.config(text=f"Résultat : {resultat:.3f}")
    except ValueError:
        lbl_result.config(text="Erreur : entrez des chiffres valides")

# Création fenêtre principale
fenetre = Tk()
fenetre.title("Calcul de Recherche Doctorale")

# Widgets interface utilisateur
Label(fenetre, text="Valeur initiale:").pack()
entry1 = Entry(fenetre)
entry1.pack()

Label(fenetre, text="Valeur finale:").pack()
entry2 = Entry(fenetre)
entry2.pack()

btn_calcul = Button(fenetre, text="Calculer", command=calculer)
btn_calcul.pack()

lbl_result = Label(fenetre, text="Résultat : ")
lbl_result.pack()

btn_quit = Button(fenetre, text="Quitter", command=fenetre.destroy)
btn_quit.pack()

# Lancement de l'interface
fenetre.mainloop()
