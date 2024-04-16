from constante import *
from random import shuffle

def melanger_paquet():
    shuffle(cartes)

def init_combi(nbJoueurs):
    return [ [] for _ in range(nbJoueurs)]

def distribuer_jetons(nb_joueurs):
    jetons = []
    for i in range(nb_joueurs):
        jetons.append(100)
    return jetons

def distribuer_cartes(nb_joueurs):
    melanger_paquet()
    joueurs = [[] for _ in range(nb_joueurs)]
    for i in range(2):
        for j in range(nb_joueurs):
            joueurs[j].append(cartes.pop())
    return joueurs

def afficher_cartes(joueur):
    [print(f"{carte[0]} de {carte[1]}") for carte in joueur]

def distribuer_cards():
    return [cartes.pop() for _ in range(5)] 


def afficher_flop(flop):
    print("\nFlop:\n(press enter to continue)")
    input()
    for i in range(3):
        print(f"{flop[i][0]} de {flop[i][1]}")
def afficher_turn(flop):
    print("\nTurn:\n(press enter to continue)")
    input()
    for i in range(4):
        print(f"{flop[i][0]} de {flop[i][1]}")

def afficher_river(flop):
    print("\nRiver:\n(press enter to continue)")
    input()
    for i in range(5):
        print(f"{flop[i][0]} de {flop[i][1]}")

        