import numpy as np

def encode_carte(carte, valeurs_vocab, couleurs_vocab):
    valeur_one_hot = np.zeros(len(valeurs_vocab))
    couleur_one_hot = np.zeros(len(couleurs_vocab))
    valeur_index = valeurs_vocab.index(carte[0])
    couleur_index = couleurs_vocab.index(carte[1])
    valeur_one_hot[valeur_index] = 1
    couleur_one_hot[couleur_index] = 1
    return np.concatenate((valeur_one_hot, couleur_one_hot))

def encode_action(action, actions_vocab):
    action_one_hot = np.zeros(len(actions_vocab))
    action_index = actions_vocab.index(action)
    action_one_hot[action_index] = 1
    return action_one_hot
def encode_montant(montant, montants_vocab):
    return montant / montants_vocab