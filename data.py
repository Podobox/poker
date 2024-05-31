from ast import literal_eval

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
    with open("data.txt", "a") as f:
         # POT-BET_PLAYER -> ce que le joueur peut espérer gagner
	    f.write(f"{BET_PLAYER}\n{POT-BET_PLAYER}\n{CARD_PLAYER}\n{CARD_TABLE}\n{WINNER}\n\n")

def load_data():
    """ Renvoie un tuple ("pot", "mise du joueur", "carte du joueur", "carte sur la table", "joueur gagnant?")"""
    
    pots = []
    bet_players = []
    card_players = []
    card_tables = []
    win = []

    with open("data.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
    for i in range(0, len(data), 6):
        if data[i].strip():
            bet_players.append(int(data[0]))
            pots.append(int(data[1]))
            card_players.append(literal_eval(data[2]))
            card_tables.append(literal_eval(data[3]))
            win.append(data[4].strip() == "True")
    return pots, bet_players, card_players, card_tables, win
    # print("POTS:", pots)
    # print("BET_PLAYERS:", bet_players)
    # print("CARD_PLAYERS:", card_players)
    # print("CARD_TABLES:", card_tables)
    # print("GAME_STATUSES:", win)



# load_data()