# Fichier contenant les fonctions de logique du jeu
from personnages import Personnage, Torche

temps_total = 0

# on vérifie ue la selection est possible -> boucler sur la selection tant que cette fonction ne renvoie pas True
def selection_possible(liste_personnages_selected :list[Personnage], torche : Torche):
    try :
        if liste_personnages_selected[1] != None :
            if liste_personnages_selected[0].get_position() == liste_personnages_selected[1].get_position() & liste_personnages_selected[0].get_position()==torche.get_position():
                return True
        return False
    except IndexError :
            if liste_personnages_selected[0].get_position() == torche.get_position() :
                return True
            return False



# 2. les déplacer + ajouter le temps max des personnages au temps_tot
#   -- Apres un click sur un bouton "valider".
#   -- changer la position du/des personnages (coté du pont)    X
#   -- ajouter le temps de traversée au temps_tot   x
#   -- vider la liste liste_selection
#   -- rénitialiser le temps de traversée à 0
def deplacement(temps_tot : int, torche : Torche, liste_selection : list[Personnage]) :

    # modification des positions
    if torche.get_position() == 1:
        torche.set_position(0)
        for personnage in liste_selection:
            personnage.set_position(0)
    else:
        torche.set_position(1)
        for personnage in liste_selection:
            personnage.set_position(1)


    # modification du temps de traversée total
    liste_temps_traverse = []
    for personnage in liste_selection:
        liste_temps_traverse.append(personnage.get_number())

    temps_deplacement = max(liste_temps_traverse)
    temps_tot += temps_deplacement

    return temps_tot



# fonction d'input de l'utilisateur -> renvoi de l'animal selectionné (objet Personnage)
def get_input_user(dico_choix_animaux, numero_selection) :
    good_selection = False
    choix_animal : Personnage|None = None

    if numero_selection == 1 :
        rang_choix = "premier"
    else :
        rang_choix = "deuxieme"

    # Assertion pour eviter les input frauduleuses (faute de frappe, ou erreur)
    while not good_selection:
        try:
            choix_animal = dico_choix_animaux[input(f"Sélectionnez votre {rang_choix} animal : ({dico_choix_animaux.keys()})\n")]
            good_selection = True
        except:
            print("\nMauvaise sélection !")
            good_selection = False

    return choix_animal



# Fonction de vérification : les personnages sont-ils tous du même coté
def check_victoire(dico_choix_animaux : dict[str : Personnage]):
    partie_gagnee = True
    for animal in dico_choix_animaux.values() :
        if animal.get_position == 0 :
            partie_gagnee = False
    return partie_gagnee



