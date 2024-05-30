POT = 0
BET_PLAYER = 0
CARD_PLAYER = []
CARD_TABLE = []
WINNER = False

def init_file_variable(pot=0, cardPlayer=[], cardTable=[], winner = {}, bet=0):
    global POT, CARD_PLAYER, CARD_TABLE, BET_PLAYER, WINNER
    if pot:
        POT = pot
    if cardPlayer:
        CARD_PLAYER = cardPlayer[:]
    if cardTable:
        CARD_TABLE = cardTable[:]
    if bet:
        BET_PLAYER = bet
    if type(winner) is list and winner[0] == 0:
        WINNER = True
    else:
        WINNER = winner == 0

def write_data():
    with open("data.txt", "w") as f:
         # POT-BET_PLAYER -> ce que le joueur peut espérer gagner
	    f.write(f"{BET_PLAYER}\n{POT-BET_PLAYER}\n{CARD_PLAYER}\n{CARD_TABLE}\n{WINNER}\n\n")
