from random import *
from time import *
from math import *

pseudo_choice = input("Quel est votre pseudo ?")
print("Bienvenue dans Shiiyo's world, pour progresser dans ce jeu il existe plusieurs commande")
print("Vous pouvez à tout moment écrire dans la console /? et vous aurez une liste de commande")
print("Dans ce jeu vous pouvez faire deux choses avancer (a) ou reculer (r)")
print("Si ""None" " s'affiche c'est qu'il ne s'est rien passé")

running = True

class Player:
    life = 30
    attack_player = 4
    level = 1
    experience = 0
    pseudo = pseudo_choice


joueur = Player()

class Blob:
    blob_life = 6
    attack_blob = 1


blob = Blob()


class BlobX:
    blobX_life = 10
    attack_blobX = 3


blobX = BlobX()


class Lynel:
    lynel_life = 20
    attack_lynel = 6


lynel = Lynel()


def combat_ending():
    print("le combat est fini")
    if joueur.life < 0:
        print("vous avez perdu : game over")
        sleep(3)
    else:
        print("Bravo, vous avez gagné")
        joueur.experience += int(get_xp)
    running = True


inventaire = ["Baton /"]


def combat_blob():
    while blob.blob_life > 0:
        joueur.life -= blob.attack_blob
        print("vous vous faites attaquer, votre vie est maintenant de : ", joueur.life)
        choice = input(print("que voulez vous faire, attaquer ou fuire ? "))
        if choice == "attaquer":
            blob.blob_life -= joueur.attack_player
            print("la vie du blob est maintenant de : ", blob.blob_life)
        elif choice == "fuire":
            escape_blob_chance = randint(1, 6)
            if escape_blob_chance == 1:
                print("Vous n'arrivez pas a fuire")
            if escape_blob_chance > 1:
                combat_ending()
        if blob.blob_life <= 0:
            combat_ending()


def combat_blobX():
    while blobX.blobX_life > 0:
        joueur.life -= blobX.attack_blobX
        print("vous vous faites attaquer, votre vie est maintenant de : ", joueur.life)
        choice = input(print("que voulez vous faire, attaquer ou fuire ? "))
        if choice == "attaquer":
            blobX.blobX_life -= joueur.attack_player
            print("la vie du blob est maintenant de : ", blobX.blobX_life)
        elif choice == "fuire":
            escape_blobX_chance = randint(1, 6)
            if escape_blobX_chance == 1:
                "Vous n'arrivez pas a fuire"
            if escape_blobX_chance > 1:
                combat_ending()
        if blobX.blobX_life <= 0:
            combat_ending()


def combat_lynel():
    while lynel.lynel_life > 0:
        joueur.life -= lynel.attack_lynel
        print("vous vous faites attaquer, votre vie est maintenant de : ", joueur.life)
        choice = input(print("que voulez vous faire, attaquer ou fuire ? "))
        if choice == "attaquer":
            lynel.lynel_life -= joueur.attack_player
            print("la vie du blob est maintenant de : ", lynel.lynel_life)
        elif choice == "fuire":
            escape_lynel_chance = randint(1, 3)
            if escape_lynel_chance == 1:
                "Vous n'arrivez pas a fuire"
            if escape_lynel_chance > 1:
                combat_ending()
        if lynel.lynel_life <= 0:
            combat_ending()


def game():
    running = True
    while running:
        inputgeneral = input("Que voulez vous faire ?")
        running = False
        if inputgeneral == "/?":
            print("les commandes sont\n /inventory\n/self")
            inputfinal = input(print("Fin de la commande ? (oui)"))
            running = True
            if "oui" == inputfinal :
                running = False
        if inputgeneral == "/inventory":
            print(inventaire)
        running = False
        if inputgeneral == "/self" :
            print("Pseudo : ", joueur.pseudo)
            print("Niveau : ", joueur.level)
            print("Experience : ", joueur.experience)
            print("Vie : ", joueur.life)
            print("points d'attaque : ", joueur.attack_player)
        if inputgeneral == "a":
            print(encounter())
        if inputgeneral == "r":
            print(encounter())
        running = False


class get_xp :
    get_mob = None
    if get_mob == "blob":
        get_xp = 20
    elif get_mob == "blobX":
        get_xp = 30
    elif get_mob == "lynel":
        get_xp = 100


def encounter():
    print("action effectuée")
    chance_blob = randint(1, 25)
    chance_blobX = randint(1, 50)
    chance_lynel = randint(1, 125)
    if chance_blob == 1:
        get_mob = "blob"
        print("Vous rencontrez un blob")
        print(combat_blob())
    elif chance_blob > 1:
        if chance_blobX == 1:
            get_mob = "blobX"
            print("vous rencontrez un blobX")
            print(combat_blobX())
    elif chance_blobX > 1:
        if chance_lynel == 1:
            get_mob = "lynel"
            print("vous rencontrez un lynel")
            print(combat_lynel())
    else:
        print("Rien ne se passe")
        running = False

while running:
    game()
    if encounter():
        break

def Level_up():
    if joueur.level == 1:
        xp_limit = 100
        if joueur.experience >= 100 :
            joueur.level = 2
            joueur.experience = 0
            joueur.life = 31
    if joueur.level == 2 :
        xp_limit = 150
        if joueur.experience >= xp_limit :
            joueur.level = 3
            joueur.experience = 0
    if joueur.level == 3 :
        xp_limit = 200
        if joueur.experience >= xp_limit :
            joueur.level = 4
            joueur.experience = 0
    if joueur.level == 4 :
        xp_limit = 300
        if joueur.experience >= xp_limit :
            joueur.level = 5
            joueur.experience = 0
    if joueur.level == 5 :
        xp_limit = 400
        if joueur.experience >= xp_limit :
            joueur.level = 6
            joueur.experience = 0
    if joueur.level == 6 :
        xp_limit = 500
        if joueur.experience >= xp_limit :
            joueur.level = 7
            joueur.experience = 0
    if joueur.level == 7 :
        xp_limit = 600
        if joueur.experience >= xp_limit :
            joueur.level = 8
            joueur.experience = 0
    if joueur.level == 8 :
        xp_limit = 700
        if joueur.experience >= xp_limit :
            joueur.level = 9
            joueur.experience = 0
    if joueur.level == 9 :
        xp_limit = 800
        if joueur.experience >= xp_limit :
            joueur.level = 10
            joueur.experience = 0
    if joueur.level == 10 :
        xp_limit = 1000
        if joueur.experience >= xp_limit :
            joueur.level = 11
            joueur.experience = 0
    if joueur.level == 11 :
        xp_limit = 1200
        if joueur.experience >= xp_limit :
            joueur.level = 12
            joueur.experience = 0
    if joueur.level == 12 :
        xp_limit = 1400
        if joueur.experience >= xp_limit :
            joueur.level = 13
            joueur.experience = 0
    if joueur.level == 13 :
        xp_limit = 1600
        if joueur.experience >= xp_limit :
            joueur.level = 14
            joueur.experience = 0
    if joueur.level == 14 :
        xp_limit = 1800
        if joueur.experience >= xp_limit :
            joueur.level = 15
            joueur.experience = 0
    if joueur.level == 15 :
        xp_limit = 2000
        if joueur.experience >= xp_limit :
            joueur.level = 16
            joueur.experience = 0
    if joueur.level == 16 :
        xp_limit = 2200
        if joueur.experience >= xp_limit :
            joueur.level = 17
            joueur.experience = 0
    if joueur.level == 17 :
        xp_limit = 2400
        if joueur.experience >= xp_limit :
            joueur.level = 18
            joueur.experience = 0
    if joueur.level == 18 :
        xp_limit = 2600
        if joueur.experience >= xp_limit :
            joueur.level = 19
            joueur.experience = 0
    if joueur.level == 19 :
        xp_limit = 2800
        if joueur.experience >= xp_limit :
            joueur.level = 20
            joueur.experience = 0
    if joueur.level == 20 :
        xp_limit = 3100
        if joueur.experience >= xp_limit :
            joueur.level = 21
            joueur.experience = 0
    if joueur.level == 21 :
        xp_limit = 3400
        if joueur.experience >= xp_limit :
            joueur.level = 22
            joueur.experience = 0
    if joueur.level == 22 :
        xp_limit = 3700
        if joueur.experience >= xp_limit :
            joueur.level = 23
            joueur.experience = 0
    if joueur.level == 23 :
        xp_limit = 4000
        if joueur.experience >= xp_limit :
            joueur.level = 24
            joueur.experience = 0
    if joueur.level == 24 :
        xp_limit = 4300
        if joueur.experience >= xp_limit :
            joueur.level = 25
            joueur.experience = 0
    if joueur.level == 25 :
        xp_limit = 5000
        if joueur.experience >= xp_limit :
            joueur.level = 26
            joueur.experience = 0
    if joueur.level == 26 :
        xp_limit = 5500
        if joueur.experience >= xp_limit :
            joueur.level = 27
            joueur.experience = 0
    if joueur.level == 27 :
        xp_limit = 6000
        if joueur.experience >= xp_limit :
            joueur.level = 28
            joueur.experience = 0
    if joueur.level == 28 :
        xp_limit = 7000
        if joueur.experience >= xp_limit :
            joueur.level = 29
            joueur.experience = 0
    if joueur.level == 29 :
        xp_limit = 10000
        if joueur.experience >= xp_limit :
            joueur.level = 30
            joueur.experience = 0
    if joueur.level == 30 :
        xp_limit = float(inf)

