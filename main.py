# fichier principal d'execution, là où le jeu sera lancé.
import logique
# import des classes et modules annexes
from personnages import Personnage, Torche
from logique import selection_possible, deplacement, get_input_user, check_victoire

if __name__ == "__main__" :
    # creation des personnages & torche + initialisation des positions à gauche (0)
    guepard = Personnage(1,"guepard", 0)
    lapin = Personnage(2,"lapin", 0)
    chevre = Personnage(5,"chevre", 0)
    escargot = Personnage(7,"escargot", 0)
    dico_choix_animaux : dict[str : Personnage] = {"guepard" : guepard, "lapin" : lapin, "chevre" : chevre, "escargot" : escargot}

    torche = Torche(0)
    temps_tot = 0

    while True :
        # 1. selectionner le/les personnages à deplacer
        #   -- verifier que les personnages sont à la même position (coté du pont) +
        #       position de la torche -> selection possible que si les personnages et
        #       la torche sont du même coté
        #   -- ajouter les personnages à une liste si la len(liste_selection) <= 2
        #   -- calculer le temps de traversée des personnages sélectionnés (en prenant le temps max)

        liste_personnages_selected: list[Personnage] = []
        # Cette variable depend de si la selection est possible ou non (si aucun animal est selectionné, Faux)
        # cf fonction : selection_possible
        bool_selection_possible = False

        while not bool_selection_possible :
            # réinitialisation des choix de l'utilisateur
            liste_personnages_to_select: list[Personnage] = []

            # input de l'utilisateur
            choix_animal_1 = get_input_user(dico_choix_animaux, 1)
            # ajout de l'animal choisi à la liste : liste_personnages_selected
            liste_personnages_to_select.append(choix_animal_1)

            # Autre animal sélectionné ?
            input_bool_valide = False
            autre_choix = None
            while not input_bool_valide :
                autre_choix = input("Voulez-vous choisir un autre animal ? (True/False)\n")
                if autre_choix == "True" or autre_choix == "False":
                    input_bool_valide = True
                else :
                    print("Mauvaise valeur !")

            # Selection du deuxième animal
            if autre_choix == "True":
                choix_valide = False
                while not choix_valide :
                    # input de l'utilisateur
                    choix_animal_2 = get_input_user(dico_choix_animaux, 2)
                    if choix_animal_2 == choix_animal_1 :
                        print("Vous devez choisir un animal différent !")
                    else :
                        choix_valide = True
                        # ajout de l'animal choisi à la liste : liste_personnages_selected
                        liste_personnages_to_select.append(choix_animal_2)

            ### On ne permet au joueur de choisir que 2 animaux avant de les selectionner et d'appliquer les fonctions de déplacement.


            # vérification que la selection est bien possible
            bool_selection_possible = selection_possible(liste_personnages_to_select, torche)

            if not bool_selection_possible :
                print("Vous ne pouvez pas choisir un animal qui n'est pas du coté de la torche")
            else :
                # on selectionne le/les animaux que le joueur a choisi
                for animal in liste_personnages_to_select:
                    animal.select(liste_personnages_selected)




        # 2. les déplacer + ajouter le temps max des personnages au temps_tot
        #   -- Apres un click sur un bouton "valider".
        #   -- changer la position du/des personnages (coté du pont)
        #   -- ajouter le temps de traversée au temps_tot
        #   -- vider la liste liste_selection
        #   -- rénitialiser le temps de traversée à 0

        # if bouton validé clicked :
        temps_tot = deplacement(temps_tot, torche, liste_personnages_selected)

        # Résultats du tour
        print("\n----------------------------------------------------------------------------------\n")


        print("Vous avez déplacé les animaux suivant avec la torche :")
        for animal in liste_personnages_selected :
            print(f"    -{animal.get_name()}")
        print("\nIls sont maintenant de l'autre coté du pont.")
        print(f"Votre temps de traversée est de {temps_tot} minutes.\n")

        # Etat des lieux = quel animal de quel coté ?
        liste_animaux_start =[]
        liste_animaux_arrive =[]
        for animal in dico_choix_animaux.values() :
            if animal.get_position() == 0 :
                liste_animaux_start.append(animal.get_name())
            else :
                liste_animaux_arrive.append(animal.get_name())
        print("Les animaux aux départ sont :")
        for animal in liste_animaux_start:
            print(animal)
        print("Les animaux à l'arrivée sont :")
        for animal in liste_animaux_arrive:
            print(animal)


        # positio de la torche
        if torche.get_position() ==0 :
            print("La torche est au départ")
        else :
            print("La torche est à l'arrivée")


        print("\n----------------------------------------------------------------------------------\n")



        # 3. si le temps tot == 14 & tous les personnages du bon coté du pont => gagné,
        #   sinon => perdu + option pour recommencer/reset
        #   le temps_tot et les positions de tous les personnages.
        if temps_tot >= 14 :
            break

    # 3. si le temps tot == 14 & tous les personnages du bon coté du pont => gagné,
    #   sinon => perdu + option pour recommencer/reset
    #   le temps_tot et les positions de tous les personnages.
    victoire_valide = check_victoire(dico_choix_animaux)
    if temps_tot==14 and victoire_valide==True :
        print("Bravo, vous avez remporter la partie !")
    else :
        print("Dommage, cette partie est perdue !")
