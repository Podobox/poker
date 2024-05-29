from constante import *
from eval import evaluer_deck, affiche_gagnant
from cards import *
from jetons import *
from data import *


NB_JOUEURS = 3

def afficher_joueur(joueurs, combi_joueurs, cards : list = ""):
    for i in range(len(joueurs)):
        print(f"\nJoueur {i+1}:")
        afficher_cartes(joueurs[i])
        combi_joueurs[i] = evaluer_deck(joueurs[i] , cards)
        print("Main évaluée:", combi_joueurs[i])

def poker_texas_holdem():
    joueurs = distribuer_cartes(NB_JOUEURS)
    combi_joueurs = init_combi(NB_JOUEURS)
    cards = distribuer_cards()
    pot = 0
    winner = []

    afficher_joueur(joueurs, combi_joueurs)
    print("\nVous êtes le joueur 1:")
    pot += mise(joueurs, pot)
    for i in range(3,6):
        afficher_street_card(cards[:i])
        afficher_joueur(joueurs, combi_joueurs, cards[:i])
        pot += mise(joueurs, pot)

        # test si un joueur est tout seul dans la partie
        p = one_player_alive()
        if p >= 0:
            winner = p+1
            break
    
    if not winner:
        winner = affiche_gagnant(joueurs, combi_joueurs, cards)

    print("Le joueur gagnant est: ", winner)
    distrib_jetons(pot, winner)

def save():
    with open("data.txt", "w") as f:
	    f.read()

def last_round():
    joueurs = distribuer_cartes(NB_JOUEURS)
    combi_joueurs = init_combi(NB_JOUEURS)
    cards = distribuer_cards()
    pot = 0
    winner = []

    print("\nVous êtes le joueur 1:")
    afficher_street_card(cards[:5])
    afficher_joueur(joueurs, combi_joueurs, cards[:5])
    pot += mise(joueurs, pot)
    
    if not winner:
        winner = affiche_gagnant(joueurs, combi_joueurs, cards)

    print(f"Le joueur gagnant est: {winner} ({pot} jetons)")
    
    POT = pot
    CARD_PLAYER = joueurs[0][:]
    CARD_TABLE = cards[:]
    write_data()
    # distrib_jetons(pot, winner)

distribuer_jetons(NB_JOUEURS)
if __name__ == '__main__':
    # poker_texas_holdem()
    last_round() # distribution de la dernière main seulement

# pot
# mise joueur
# carte joueur
# carte table
