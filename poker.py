from constante import *
from eval import evaluer_deck, affiche_gagnant
from cards import *

def afficher_joueur(joueurs, combi_joueurs, cards=""):
    for i in range(len(joueurs)):
        print(f"\nJoueur {i+1}:")
        afficher_cartes(joueurs[i])
        combi_joueurs[i] = evaluer_deck(joueurs[i] , cards)
        print("Main évaluée:", combi_joueurs[i])

def poker_texas_holdem(nbJoueurs):
    jetons = distribuer_jetons(nbJoueurs)
    joueurs = distribuer_cartes(nbJoueurs)
    combi_joueurs = init_combi(nbJoueurs)
    cards = distribuer_cards()
    afficher_joueur(joueurs, combi_joueurs)
    afficher_flop(cards)
    afficher_joueur(joueurs, combi_joueurs, cards[:3])
    afficher_turn(cards)
    afficher_joueur(joueurs, combi_joueurs, cards[:4])
    afficher_river(cards)
    afficher_joueur(joueurs, combi_joueurs, cards[:5])

    print("Le joueur gagnant est: ", affiche_gagnant(joueurs, combi_joueurs, cards))

poker_texas_holdem(2)
