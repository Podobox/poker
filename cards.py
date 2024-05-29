from constante import *
from random import shuffle

def melanger_paquet():
    shuffle(cartes)

def init_combi(nbJoueurs):
    return [ [] for _ in range(nbJoueurs)]

def distribuer_jetons(nbJoueurs):
    for i in range(nbJoueurs):
        JETONS.append(100)

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


def afficher_street_card(street_card : list):
    match len(street_card):
        case 3:
            print("\nFlop:\n(press enter to continue)")
        case 4:
            print("\nTurn:\n(press enter to continue)")
        case 5:
            print("\nRiver:\n(press enter to continue)")
        case _:
            print("Erreur de longueur de street_card")
    
    for i in range(len(street_card)):
        print(f"{street_card[i][0]} de {street_card[i][1]}")

def one_player_alive():
    player_alive = []
    for i in range(len(JETONS)):
        if JETONS[i] > 0:
            player_alive.append(i)
    if len(player_alive) != 1:
        return -1
    else:
        return player_alive[0]