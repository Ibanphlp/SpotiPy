import pygame 
# si ce n'est pas fait, installez Pygame : 

# Terminal: 'pip3 install pygame' ou 'sudo apt install python3-pygame' 
    
# Spyder: 
# (installation dans spyder-runtime car environnement py spécial)
# D'abord:
    # import ensurepip
    # ensurepip.bootstrap()
              
# Puis ensuite:
    # import sys
    # !{sys.executable} -m pip install pygame
              
from bdd import * # importation du module base de données contenant les fonctions pour lire la base de donnée
import sqlite3 

def jouer(son):
    '''Jouer un son mp3 avec pygame (non fonctionnel sur la VM)'''
    pygame.init()
    pygame.mixer.music.load('archive/' + son[0][0]) # jouer le mp3 se trouvant dans le dossier archive et dont le nom est dans la base de donnée
    pygame.mixer.music.play()

def stop(son):
    '''stopper la musique'''
    pygame.mixer.music.stop()


# interfaces  
def menu_principal():
    '''CLI du programme qui affiche soit la liste des albums soit la liste des titres dans les albums et gérant les touches d'interaction'''
    
    # Menu principal
    print(couleurs['vert'] + "Bienvenue sur Spotipy !" +couleurs['reset']+"\nPour accéder à un album, tapez son id.")
    print()
    make_dico()

    print("\nTouches disponibles : [id de l'album] [c pour les crédits] [q pour quitter]\n")

    dans_album = False # état du menu: soit affichage des albums soit affichage des titres

    while True:
        touche = input("Tapez une touche : ").lower() # input pour la touche préssée (toujours en miniscule)

        if touche == 'q': # q pour quitter la boucle
            print("Merci d'avoir utilisé Spotipy et au revoir !!")
            break
        elif touche.isdigit() and dans_album: # si la touche est un chiffre et si l'interface est dans l'affichage des titres, jouer le titre choisi
            jouer(get_lien_par_id_titre(touche))
            print("Lecture en cours de "+ couleurs['vert'] +style['gras']+get_nom_par_id_titre(touche)[0][0]+couleurs['reset']+ couleurs['reset'])
        elif touche == 's': # si la touche est s alors stopper la musique 
            pygame.mixer.music.stop()
            print("La musique a été stopée")
        elif touche == 'c': # si la touche est c alors afficher les crédits
            print(couleurs['jaune']+"Spotipy a été developpé par Iban PHILIPPE, Lalie PLAGELET ainsi que Vigil VUILLIOMENET sur Thonny et testé sur Spyder et Thony.\nPython a ete utilisé pour le developpement du logiciel et SQLite pour la base de données.\nSi vous avez appréciés ce logiciel, n'hésitez pas a faire un don merci 💚."+couleurs['reset'])
        elif touche == 'r': # si la touche est r alors re-afficher le menu principal
            dans_album = False # sortir de l'état affichant les titres
            print(couleurs['vert'] + "Bienvenue sur Spotipy !" + couleurs['reset'] + "\nPour accéder à un album, tapez son id.")
            print()
            make_dico()
            print("\nTouches disponibles : [id de l'album] [c pour les crédits] [q pour quitter]\n")
        elif touche.isdigit() and not dans_album: # si la touche est un chiffre et si l'état n'affiche pas les titres, alors afficher la liste des titres
            if make_dico_titres(int(touche)):
                dans_album = True # entrer dans l'état affichant les titres
                print("\nTouches disponibles : \n[(id du titre) pour ▶ un titre] \n[s pour ⏹ la lecture] \n[r pour revenir aux albums] \n[q pour quitter]\n")
        else:
            print("La touche" + touche + "n'est pas assignée.\n")
 
menu_principal() # lancer le programme