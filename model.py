import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers import Dense, Input, Concatenate
from tensorflow.keras.models import Model
from sklearn.model_selection import train_test_split
from data import load_data  # Import the load_data function from data.py

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

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

# Load the data from data.txt
pots, bet_players, card_players, card_tables, win, gain = load_data()

# Encode the card data
encoded_card_players = [np.concatenate([encode_carte(card, valeurs_vocab, couleurs_vocab) for card in cards]) for cards in card_players]
encoded_card_tables = [np.concatenate([encode_carte(card, valeurs_vocab, couleurs_vocab) for card in cards]) for cards in card_tables]

# Combine all features
X = np.array([
    np.concatenate([[pot, bet], player_cards, table_cards])
    for pot, bet, player_cards, table_cards in zip(pots, bet_players, encoded_card_players, encoded_card_tables)
])
y_win = np.array(win)
y_gain = np.array(gain)

# Normalize the numeric data (excluding one-hot encoded cards and win/loss boolean)
numeric_features = X[:, :2]  # pot, bet
numeric_features = numeric_features / np.max(numeric_features, axis=0)
X[:, :2] = numeric_features

# Split the data into training and testing sets
X_train, X_test, y_win_train, y_win_test, y_gain_train, y_gain_test = train_test_split(
    X, y_win, y_gain, test_size=0.3, random_state=42
)

# Define the input layer
input_layer = Input(shape=(X_train.shape[1],))

# Define the dense layers
dense1 = Dense(50, activation='relu')(input_layer)
dense2 = Dense(50, activation='relu')(dense1)

# Define the output layers
win_output = Dense(1, activation='sigmoid', name='win_output')(dense2)
gain_output = Dense(1, name='gain_output')(dense2)

# Create the model
model = Model(inputs=input_layer, outputs=[win_output, gain_output])

# Compile the model
model.compile(
    optimizer='adam',
    loss={
        'win_output': 'binary_crossentropy',
        'gain_output': 'mse'
    },
    metrics={
        'win_output': 'accuracy',
        'gain_output': 'mae'
    }
)

# Prepare the target data for training
y_train = {'win_output': y_win_train, 'gain_output': y_gain_train}
y_test = {'win_output': y_win_test, 'gain_output': y_gain_test}

# Train the model
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), batch_size=8)

# Evaluate the model
results = model.evaluate(X_test, y_test)

total_loss = results[0]
win_loss = results[1]
win_accuracy = results[2]

print(f"Total Loss: {total_loss}")
print(f"Win Loss: {win_loss}")
print(f"Win Accuracy: {win_accuracy}")

model.save('bet_predictor_model.h5')