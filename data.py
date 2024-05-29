POT = 0
BET_PLAYER = 0
CARD_PLAYER = []
CARD_TABLE = []

def init_variable(pot, cardPlayer, cardTable):
    POT = pot
    CARD_PLAYER = cardPlayer[:]
    CARD_TABLE = cardTable[:]

def write_data():
    with open("data.txt", "w") as f:
	    f.write(f"{POT}\n{BET_PLAYER}\n{CARD_PLAYER}\n{CARD_TABLE}\n\n")
