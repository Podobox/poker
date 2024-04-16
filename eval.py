from constante import *
from enum import Enum

class Combinaison(Enum):
    CARTE_HAUTE = (0, "Carte Haute")
    PAIRE = (1, "Paire")
    DOUBLE_PAIRE = (2, "Double Paire")
    BRELAN = (3, "Brelan")
    QUINTE = (4, "Quinte")
    FLUSH = (5, "Flush")
    FULL = (6, "Full")
    CARRE = (7, "Carré")
    QUINTE_FLUSH = (8, "Quinte Flush")
    QUINTE_FLUSH_ROYALE = (9, "Quinte Flush Royale")

    def __init__(self, valeur, nom):
        self.valeur = valeur
        self.nom = nom
    
    def __str__(self):
        return self.nom
    
    @classmethod
    def trouver_numero(cls, nom_combinaison):
        for combinaison in cls:
            if combinaison.nom == nom_combinaison:
                return combinaison.valeur
        raise ValueError(f"Combinaison '{nom_combinaison}' non trouvée")
    
# Converti les valeurs d'une liste en entier (ex: '1' en 1)
def convert_values(deck):
    deck = list(deck)
    for n in range(len(deck)):
        for i in range(len(valeurs)):
            if deck[n] == valeurs[i]:
                deck[n] = i+2
    return deck

def is_quinte_color(deck: list, color):
    d = []
    extra_card = False
    # On ajoute les cartes de la même couleur que la color
    [d.append(card) for card in deck if card[1] == color]
    for i in range(len(d)):
        d[i] = d[i][0]
    d.sort()
    d = convert_values(d)
    # On regarde si les cartes de la même couleurs se suivent
    for i in range(len(d)-1):
        if d[i+1] - d[i] != 1:
            if len(d) == 5:
                return 0
            elif not extra_card:
                extra_card = True
            else:
                return 0
    if d[-1] == 14:
        return 2
    return 1

def choose_combinaison(doublon, deck):
    score = 0
    quinte = []
    combinaison = ""
    valeursMain, couleur = zip(*deck)
    valeursMain = convert_values(valeursMain)
    valeursMainSort = sorted(valeursMain)
    # print("Valeurs: ", valeursMain, "\nCouleurs: ", couleur)

    # implement quinte
    for i in range(len(valeursMainSort)-1):
        if valeursMainSort[i+1] == (valeursMainSort[i] + 1):
            quinte.append(valeursMainSort[i])
        elif valeursMainSort[i+1] != (valeursMainSort[i]):
            quinte = []
        if len(quinte) == 4:
            quinte.append(valeursMainSort[i+1])
            score = 4
            combinaison = 'Quinte'
            break
    # implement colors
    for c in couleurs:
        if couleur.count(c) >= 5: 
            if combinaison == 'Quinte':
                if is_quinte_color(deck, c) == 1:
                    score = 8
                    combinaison = 'Quinte Flush'
                if is_quinte_color(deck, c) == 2:
                    score = 9
                    combinaison = 'Quinte Flush Royale'
            else:
                score = 5 
                combinaison = 'Flush'

    if len(doublon) > 0: # Sinon erreur ligne suivante...
        if sum(doublon) == 4:
            for n in valeursMain:
                if valeursMain.count(n) == 4 and score < 8:
                    score = 7
                    combinaison = 'Carré'
                elif score < 3:
                    score = 2
                    combinaison = 'Double Paire'
        elif sum(doublon) == 5 and score < 7:
            score = 6
            combinaison = 'Full'
        elif sum(doublon) == 3 and score < 4:
            score = 3
            combinaison = 'Brelan'
        elif sum(doublon) == 2 and score < 2:
            score = 1
            combinaison = 'Paire'
        # On traite les cas où il y a plusieurs combinaisons dans le même deck
        elif sum(doublon) == 6:
            if sorted(doublon)[0] == 4:
                score = 7
                combinaison = 'Carré'
            elif sorted(doublon)[0] == 3:
                score = 3
                combinaison = 'Brelan'
            else:
                score = 2
                combinaison = 'Double Paire'
                
        elif sum(doublon) == 7:
            if sorted(doublon)[0] == 4:
                score = 7
                combinaison = 'Carré'
            elif sorted(doublon)[0] == 3:
                score = 6
            combinaison = 'Full'
    # Au cas où j'aurai oublié un cas
        elif combinaison == "":
            combinaison = 'To do'
    elif score == 0:
        combinaison = 'Carte Haute'
    return combinaison

def evaluer_deck(joueur, flop=""):
    deck = joueur[:]
    doublon = []
    if(flop):
        deck += flop
    valeursMain = [carte[0] for carte in deck]

    for valeur in valeurs:
        if valeursMain.count(valeur) > 1:
            doublon.append(valeursMain.count(valeur))
    return choose_combinaison(doublon, deck)    

# fonctions pour déterminer le gagnant entre les différents paquets
# Pour les carte haute/paire/double paire/brelan/full/carré
def meilleure_carte(deck : list):
    doublon = []
    cards = [value for value, color in deck]
    cards = convert_values(cards)
    print("Function meilleure_carte, cards: ", cards)
    for c in cards:
        count = cards.count(c)
        if count > 1:
            doublon.append(count)

    if not doublon:
        if not cards:
            print("Function meilleure_carte, meilleure carte haute: ", max(cards))
            return max(cards)
        else: # Les 2 joueurs ont les mêmes cartes


    else:
        doublon = max(doublon)
        combi = []
        for c in cards:
            if cards.count(c) == doublon:
                combi.append(c)
        print("Function meilleure_carte, meilleure carte: ", max(combi))
        return max(combi)

def troncate(deck : list):
    doublon = []
    cards = deck[:]
    value = [v for v, c in deck]
    value = convert_values(value)
    cardRemove = []
    for v in value:
        count = value.count(v)
        if count > 1:
            doublon.append(count)
    if not doublon: # Carte haute
        for c in cards:
            if convert_values([c[0]])[0] == max(value):
                cards.remove(c)
                return cards
    else:
        doublon = max(doublon)
        for i in range(len(cards)):
            if value.count(convert_values([cards[i][0]])[0]) == doublon:
                cardRemove.append(cards[i])

        value = [v for v,c in cardRemove]
        value = convert_values(value)
        print("troncate, cardRemove: ", cardRemove)
        for c in cardRemove:
            # Pour ne pas retirer plusieurs paire d'un coup
            if convert_values([c[0]])[0] == max(value): # Plus de problème 
                cards.remove(c)

        return cards



def affiche_gagnant(joueurs, combi_joueurs, cards):
    winner = []
    number_combi = []
    deck = [] 
    for i in range(len(combi_joueurs)):
        number_combi.append(Combinaison.trouver_numero(combi_joueurs[i])) # Fonction qui converti en nombre les combinaisons
    for i in range(len(combi_joueurs)):
        if max(number_combi) == number_combi[i]:
            winner.append(i)
            deck.append(sorted(joueurs[i][:] + cards[:])) # Ajoute le deck entier trié dans une variable
    if len(winner) == 1:
        return winner[0]+1
    else: # Si les joueurs ont la même combinaison
        best_card = [] # Même longueur que winner

        # On s'assure que les meilleurs joueurs n'aient pas les mêmes cartes
        while not best_card or max(best_card) != 0  or best_card.count(max(best_card)) != 1:
            best_card = []
            for i in range(len(winner)):
                # On traite le cas carte haute/paire/double paire/brelan/full/carré
                if Combinaison.trouver_numero(combi_joueurs[winner[i]]) in [0, 1, 2, 3, 7]:
                    best_card.append(meilleure_carte(deck[i]))
                else:
                    return "To do"

            # On modifie les deck puisque les deux joueurs ont les mêmes meilleurs cartes
            for i in range(len(deck)):
                deck[i] = troncate(deck[i])

        for i in range(len(best_card)):
            if best_card[i] == max(best_card):
                return winner[i]+1

