import numpy as np
from poker import *

valeurs_vocab = valeurs 
couleurs_vocab = couleurs

carte_joueur = [('8', 'Carreau'), ('A', 'Carreau')]
carte_table = [('5', 'Trèfle'), ('A', 'Coeur'), ('3', 'Coeur'), ('Q', 'Carreau'), ('7', 'Pique')]

def encode_carte(carte, valeurs_vocab, couleurs_vocab):
    valeur_one_hot = np.zeros(len(valeurs_vocab))
    couleur_one_hot = np.zeros(len(couleurs_vocab))
    valeur_index = valeurs_vocab.index(carte[0])
    couleur_index = couleurs_vocab.index(carte[1])
    valeur_one_hot[valeur_index] = 1
    couleur_one_hot[couleur_index] = 1
    return np.concatenate((valeur_one_hot, couleur_one_hot))

# Convertir la carte du joueur en one-hot encoding
carte_joueur_encoded = np.array([encode_carte(carte, valeurs_vocab, couleurs_vocab) for carte in carte_joueur])

# Convertir les cartes sur la table en one-hot encoding
carte_table_encoded = np.array([encode_carte(carte, valeurs_vocab, couleurs_vocab) for carte in carte_table])

print("One-hot encoding de la carte du joueur:")
print(carte_joueur_encoded)
print("One-hot encoding des cartes sur la table:")
print(carte_table_encoded)


