from constante import *
from random import randint
from data import *

def display_jetons():
    print("")
    for i in range(len(JETONS)):
        if JETONS[i] >= 0:
            print(f"Jetons joueur {i+1}: {JETONS[i]}")
        else:
            print(f"Jetons joueur {i+1}: {-JETONS[i]} (couché)")
    print("")

def calcul_jetons(mise : list):
    for i in range(len(JETONS)):
        if JETONS[i] < 0:
            JETONS[i] += mise[i]
        else:
            JETONS[i] -= mise[i]

def init_mise(joueurs):
    mise = [0 for _ in range(len(joueurs))]
    for i in range(len(JETONS)):
        if JETONS[i] < 0:
            mise[i] = -1
    return mise

def end_round(mise : list):
    # boucle infini si 2 joueurs font tapis
    for i in range(len(mise)):
        if JETONS[i] > 0 and mise[i] != max(mise):
            return False
    return True

def mise_player(misePlayer, max):
    mise = 0
    while True:
        try:
            if misePlayer < max: # se couche, mise ou relance
                mise = input("Quelle est votre mise ? (0 pour se coucher)\n")
            else: # check ou mise
                mise = input("Quelle est votre mise ? (0 pour check)\n")
            mise = int(mise) 

            if mise == JETONS[0]:
                print("Vous avez fait tapis !")
                break
            elif mise == 0:
                if misePlayer < max: # se coucher
                    print("Vous vous êtes couché")
                    JETONS[0] = -JETONS[0]
                    break   
                else:
                    print("Voux avez checké")
                    break
            elif mise < 0:
                print("Veuillez entrer un nombre positif pour votre mise")
            elif mise > JETONS[0]:
                print("Vous n'avez pas suffisamment de jetons pour cette mise")
            # elif mise < BASE_STACK + max and mise > max:
            #     print(f"Votre est inférieur à la mise minimum ({BASE_STACK + max} jetons)")
            # elif mise < max:
            #     print(f"Votre mise doit être supérieu à {max} jetons")
            else:
                # Si la mise est valide, sortir de la boucle
                print(f"Vous avez misé {mise}")       
                break

        except ValueError:
            print("Veuillez entrer un nombre entier pour votre mise")
        except TypeError:
            print("La saisie n'est pas valide. Veuillez réessayer.")
    BET_PLAYER = mise
    return mise

def mise(joueurs : list, pot):
    mise = [0 for _ in range(len(joueurs))]
    dealer = DEALER
    ordre = [i for i in range(len(joueurs))]
    ordre[:] = ordre[dealer+1:] + ordre[:dealer+1] # Changer l'orde de demande des mises
    # Affichage des jetons de chaque joueur
    display_jetons()
    print(f"pot: {pot} jetons")
    
    while True:
        for i in ordre:
            if JETONS[i] < 0:
                print(f"Joueur {i+1} est couché")
            elif JETONS[i] == 0:
                print(f"Joueur {i+1} a fait tapis !")
            # si la mise du joueur est égale à la mise max on ne le compte pas
            elif mise[i] == 0 or mise[i] != max(mise):
                # Au tour du joueur
                if i == 0:
                    if mise[0] < JETONS[0]:
                        mise[i] = mise_player(mise[i], max(mise))
                    else:
                        print("Vous ne pouvez pas miser plus")
                else:
                    if mise[i] < JETONS[i]:
                        # Mise minimum de l'ordinateur
                        if randint(0,1) == 0: 
                            if max(mise) == 0:
                                print(f"Joueur {i+1} check")
                                pass # check
                            elif JETONS[i] >= max(mise):
                                if randint(0,1) == 0:
                                    mise[i] = max(mise)
                                    print(f"Joueurs {i+1} a misé {mise[i]}")
                                else:
                                    JETONS[i] = -JETONS[i] # couché
                                    print(f"Joueur {i+1} s'est couché")

                        else:
                            if max(mise) == 0 and JETONS[i] >= 16:
                                mise[i] = randint(BASE_STACK, int(JETONS[i]/4))
                                print(f"Joueurs {i+1} a misé {mise[i]}")
                            elif JETONS[i]*3/4 >= max(mise) and JETONS[i] >= 16:
                                mise[i] = max(mise) + randint(BASE_STACK, int(JETONS[i]/4))
                                if mise[i] == JETONS[i]:
                                    print(f"Joueur {i+1} a fait tapis ! ({mise[i]} jetons)")
                                else:
                                    print(f"Joueurs {i+1} a misé {mise[i]}")
                            else: # tapis
                                mise[i] = JETONS[i]
                                print(f"Joueur {i+1} a fait tapis ! ({mise[i]} jetons)")
                    else:
                        print(f"Joueur {i+1} ne peut pas miser plus")
                
        if i == ordre[-1]: # si on est au dernier joueur 
            break
    calcul_jetons(mise) # calcul les jetons en soustrayant les mises 
    print("Total à gagner: ", pot + sum(mise)) 
    return sum(mise[:])

def distrib_jetons(pot, winner):
    pass