POT = 0
BET_PLAYER = 0
CARD_PLAYER = []
CARD_TABLE = []

def init_file_variable(pot=0, cardPlayer=[], cardTable=[], bet=0):
    global POT, CARD_PLAYER, CARD_TABLE, BET_PLAYER
    if pot:
        POT = pot
    if cardPlayer:
        CARD_PLAYER = cardPlayer[:]
    if cardTable:
        CARD_TABLE = cardTable[:]
    if bet:
        BET_PLAYER = bet

def write_data():
    with open("data.txt", "a") as f:
	    f.write(f"{POT}\n{BET_PLAYER}\n{CARD_PLAYER}\n{CARD_TABLE}\n\n")
