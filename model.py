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
def simulate_bet_data(num_samples=1000):
    # Example structure: [player_id, current_pot, player_bet, max_bet, action (0: fold, 1: check, 2: raise)]
    data = []
    for _ in range(num_samples):
        current_pot = np.random.randint(10, 1000)
        player_bet = np.random.randint(10, 100)
        # max_bet = np.random.randint(0, player_bet // 2)
        

        # Generate player cards and table cards
        player_cards = [encode_carte((np.random.choice(valeurs_vocab),
            np.random.choice(couleurs_vocab)), valeurs_vocab, couleurs_vocab) for _ in range(2)]
        table_cards = [encode_carte((np.random.choice(valeurs_vocab),
            np.random.choice(couleurs_vocab)), valeurs_vocab, couleurs_vocab) for _ in range(5)]
        player_cards_flat = np.concatenate(player_cards)
        table_cards_flat = np.concatenate(table_cards)

        # Combine all features
        features = np.concatenate([[current_pot, player_bet], player_cards_flat, table_cards_flat])


        win_loss = np.random.randint(0, 2)
        data.append(np.concatenate([features, [win_loss]]))

    return np.array(data)

# Generate the simulated bet data
bet_data = simulate_bet_data()

# Split the data into training and testing sets
X = bet_data[:, :-1]
y = bet_data[:, -1]

# # Normalize the numeric data (excluding one-hot encoded cards and win/loss boolean)
# numeric_features = X[:, 0:2]  # current_pot, player_bet, max_bet
# numeric_features = numeric_features / np.max(numeric_features, axis=0)
# X[:, 1:4] = numeric_features

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the RNN model
model = Sequential()
model.add(Embedding(input_dim=NB_JOUEURS, output_dim=10, input_length=X_train.shape[1] - len(valeurs_vocab)*2*2 - len(couleurs_vocab)*2*2))
model.add(SimpleRNN(50, return_sequences=True))
model.add(SimpleRNN(50))
model.add(Dense(3, activation='softmax'))  # Output layer with 3 classes (fold, check, raise)

# model = Sequential()
# model.add(Embedding(input_dim=NB_JOUEURS, output_dim=10, input_length=X_train.shape[1] - len(valeurs_vocab)*2*2 - len(couleurs_vocab)*2*2))
# model.add(Flatten())  # Flatten the embedding output
# model.add(Dense(50, activation='relu'))
# model.add(Dense(50, activation='relu'))
# model.add(Dense(3, activation='softmax')) 

# Compile the model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=20, validation_data=(X_test, y_test), batch_size=32)

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Loss: {loss}")
print(f"Test Accuracy: {accuracy}")
