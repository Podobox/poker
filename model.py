import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import SimpleRNN, Dense, Embedding
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential  
from data import load_data

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Define the number of players
NB_JOUEURS = 3
# Define the card values and suits
valeurs_vocab = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] 
couleurs_vocab = ['Coeur', 'Carreau', 'Trèfle', 'Pique']

def encode_carte(carte, valeurs_vocab, couleurs_vocab):
    valeur_one_hot = np.zeros(len(valeurs_vocab))
    couleur_one_hot = np.zeros(len(couleurs_vocab))
    valeur_index = valeurs_vocab.index(carte[0])
    couleur_index = couleurs_vocab.index(carte[1])
    valeur_one_hot[valeur_index] = 1
    couleur_one_hot[couleur_index] = 1
    return np.concatenate((valeur_one_hot, couleur_one_hot))

# Function to simulate data generation for poker bets
pots, bet_players, card_players, card_tables, win = load_data()

# Encode the card data
encoded_card_players = [np.concatenate([encode_carte(card, valeurs_vocab, couleurs_vocab) for card in cards]) for cards in card_players]
encoded_card_tables = [np.concatenate([encode_carte(card, valeurs_vocab, couleurs_vocab) for card in cards]) for cards in card_tables]

# Combine all features
X = np.array([
    np.concatenate([[pot, bet], player_cards, table_cards])
    for pot, bet, player_cards, table_cards in zip(pots, bet_players, encoded_card_players, encoded_card_tables)
])
y = np.array(win)

# Normalize the numeric data (excluding one-hot encoded cards and win/loss boolean)
numeric_features = X[:, :2]  # pot, bet
numeric_features = numeric_features / np.max(numeric_features, axis=0)
X[:, :2] = numeric_features

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the model
model = Sequential()
model.add(Dense(50, activation='relu', input_shape=(X_train.shape[1],)))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification (win/loss)

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), batch_size=8)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")