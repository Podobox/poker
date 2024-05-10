from encode import *

valeurs_vocab = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 
couleurs_vocab = ['Coeur', 'Carreau', 'Trèfle', 'Pique']

ACTION_VOCAB = ['miser', 'se_coucher', 'check', 'relancer']
MONTANT_VOCAB = 100 # Montant maximum de mise possible


# données d'exemple
carte_table = [('K, Trèfle')]
carte_joueur = [('8', 'Carreau'), ('A', 'Carreau')]
carte_table = [('5', 'Trèfle'), ('A', 'Coeur'), ('3', 'Coeur'), ('Q', 'Carreau'), ('7', 'Pique')]
actions_joueurs = ['miser', 'miser']  # Actions du joueurs
montant_joueur = 6

# Convertir la carte du joueur en one-hot encoding
carte_joueur_encoded = np.array([encode_carte(carte, valeurs_vocab, couleurs_vocab) for carte in carte_joueur])
# Convertir les cartes sur la table en one-hot encoding
carte_table_encoded = np.array([encode_carte(carte, valeurs_vocab, couleurs_vocab) for carte in carte_table])

actions_joueurs_encoded = np.array([encode_action(action, ACTION_VOCAB) for action in actions_joueurs])
montant_joueur_encoded = encode_montant(montant_joueur, MONTANT_VOCAB)

print("One-hot encoding de la carte du joueur:")
print(carte_joueur_encoded)
print("One-hot encoding des cartes sur la table:")
print(carte_table_encoded)
print("One-hot encoding des actions des joueurs:")
print(actions_joueurs_encoded)
print("One-hot encoding du montant misé par le joueur:")
print(montant_joueur_encoded)



