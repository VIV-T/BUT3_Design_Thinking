import time

import pygame
import logique
from personnages import Personnage, Torche
import os
# utilse pour les regex
from re import sub,search

# creation du project_path & du sprite_path
project_path = os.getcwd()
sprite_directory_path = project_path + "\\sprite"
pygame.font.init()

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("escape the jungle")
#main_theme = sprite_directory_path+'\\main_theme.mp3'
#pygame.mixer.music.load(main_theme)
#pygame.mixer.music.play()

# Chargement des images
icon = pygame.image.load(sprite_directory_path+'\\icon.png')
button_play = pygame.image.load(sprite_directory_path+'\\PlayBtn.png')
bg_jeu = pygame.image.load(sprite_directory_path+'\\background_game.png')
bg_menu = pygame.image.load(sprite_directory_path+'\\bg_menu.png')
fg_jeu = pygame.image.load(sprite_directory_path+'\\front_game.png')
hub_animal_select = pygame.image.load(sprite_directory_path+'\\hud_animals.png')
button_valid = pygame.image.load(sprite_directory_path+'\\hud_valid.png')
prof_chen = pygame.image.load(sprite_directory_path+'\\prof_chen_1.png')
bubble_text = pygame.image.load(sprite_directory_path+'\\bubble_text.png')

font = pygame.font.Font(None, 15)


# Creation des personnages/animaux
pikachu = Personnage(1,"pikachu", sprite_directory_path, 0, x=360, y=630, taille=35)
poussifeu = Personnage(2,"poussifeu", sprite_directory_path, 0, x=300, y=610, taille=85)
lokhlass = Personnage(5,"lokhlass", sprite_directory_path, 0, x=220, y=620, taille=120)
ronflex = Personnage(7,"ronflex", sprite_directory_path, 0, x=110, y=595, taille=150)


# changement icon app
pygame.display.set_icon(icon)

# Redim des images
bg_jeu = pygame.transform.scale(bg_jeu, screen.get_size())
bg_menu = pygame.transform.scale(bg_menu, screen.get_size())
button_play = pygame.transform.scale(button_play, (200, 100))
button_valid = pygame.transform.scale(button_valid, (75,75))
hub_animal_select = pygame.transform.scale(hub_animal_select, (250,100))
fg_jeu = pygame.transform.scale(fg_jeu, (1280, 720))

# Position
hub_animal_rect = hub_animal_select.get_rect(center=(130,60))
play_rect = button_play.get_rect(center=(640, 640))
valid_rect = button_valid.get_rect(center=(1200, 50))
fg_jeu_rect = fg_jeu.get_rect(center=(640, 360))
prof_chen_rect = prof_chen.get_rect(center=(1260,600))
bubble_text_rect = bubble_text.get_rect(center=(1150,520))

running = True
menu = True

# initialisation perso
dico_choix_animaux : dict[str : Personnage] = {"pikachu" : pikachu, "poussifeu" : poussifeu, "lokhlass" : lokhlass, "ronflex" : ronflex}

torche = Torche(sprite_directory_path, x=390, y = 615)
temps_tot = 0
liste_personnages_selected: list[Personnage] = []



def game_loop():
    # boucle de la partie
    playing = True
    current_crossing_time = 0

    # Initialisation chaine de caractère affichées à l'écran
    # Affichage des poké_selected & time
    poke_text = ""
    poke_lines = poke_text.splitlines()
    poke_selection_change = True
    crossing_bridge = False
    max_move_time = 0
    # Répliques du prof Chen
    bool_prof_chen_text = True
    time_start_affichage_text = 0
    prof_chen_text = "Commençons le jeu..."
    prof_chen_lines = prof_chen_text.splitlines()

    while playing:
        screen.blit(bg_jeu, (0, 0))  # Fond de jeu
        screen.blit(fg_jeu, fg_jeu_rect.topleft)  # Avant-plan positionné
        screen.blit(button_valid, valid_rect.topleft)  # Affiche le boutton valider
        screen.blit(hub_animal_select, hub_animal_rect)
        screen.blit(torche.get_sprite(), torche.get_rect())
        screen.blit(prof_chen, prof_chen_rect)

        # Affichage texte : poke_selected & temps de parcours
        # definition de la coord y de la premiere ligne
        y = 60
        if poke_selection_change :
            if max_move_time !=0 :
                poke_text += f"Current crossing time : {current_crossing_time} (+{max_move_time})"
            else :
                poke_text += f"Current crossing time : {current_crossing_time}"
            poke_selection_change = False
        elif crossing_bridge :
            poke_text = f"Current crossing time : {current_crossing_time}"
            crossing_bridge = False

        poke_lines = poke_text.splitlines()
        for poke_line in poke_lines:
            printed_line = font.render(poke_line, 1, (0, 0, 0))
            printed_line_rect = printed_line.get_rect(center=(150, y))
            screen.blit(printed_line, printed_line_rect)
            y += 10

        # Affichage texte professeur Chen
        if bool_prof_chen_text == True and pygame.time.get_ticks() < time_start_affichage_text +4000:
            # Affichage de la bulle
            screen.blit(bubble_text, bubble_text_rect)
            # Affichage du texte de la bulle
            # set le y de la première ligne
            y = 510
            prof_chen_lines = prof_chen_text.splitlines()
            for prof_chen_line in prof_chen_lines :
                printed_line = font.render(prof_chen_line, 1, (0, 0, 0))
                printed_line_rect = printed_line.get_rect(center=(1150, y))
                screen.blit(printed_line, printed_line_rect)
                y += 10
        else:
            bool_prof_chen_text = False


        for poke in dico_choix_animaux.values():
            screen.blit(poke.get_sprite(), poke.get_rect())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if valid_rect.collidepoint(event.pos):  # Vérifie si le bouton "valider" est cliqué
                    if len(liste_personnages_selected) > 0:
                        list_moving_poke = []
                        # impossible de faire une deepcopy avec des instance de classe et une copie simple ne suffit pas
                        for poke_selected in liste_personnages_selected :
                            list_moving_poke.append(poke_selected)

                        list_move_time =[]
                        for poke_selected in list_moving_poke:
                            list_move_time.append(poke_selected.get_number())
                        max_move_time = max(list_move_time)

                        # deplacement des pokemon, rajouter la notion de temporalité !!!! (en fonction de la var max_move_time)
                        # j'ai essayé des trucs dans la methode move de la classe Personnage,
                        # mais il faut faire en sorte de faire un poke.move() par frame dans la boucle while
                        move_finished = False
                        while not move_finished :
                            for moving_poke in list_moving_poke:
                                # le code est fait pour que les deux pokemon arrivent dans la même itération de boucle while
                                move_finished = moving_poke.move(max_move_time=max_move_time)
                            move_finished = torche.move(max_move_time=max_move_time)

                        for moving_poke in list_moving_poke :
                            moving_poke.unselect(liste_personnages_selected)
                            moving_poke.change_position()

                        # déplacement de la torche
                        if torche.get_position() == 0:
                            torche.set_position(1)
                        else:
                            torche.set_position(0)

                        # Maj du current_crossing_time
                        current_crossing_time += max_move_time
                        crossing_bridge = True


                for poke in dico_choix_animaux.values() :
                    if poke.get_rect().collidepoint(event.pos) :
                        if poke.get_selected() == 0:
                            if len(liste_personnages_selected) < 2:
                                if torche.get_position() == poke.get_position():
                                    poke.select(liste_personnages_selected)
                                    poke.set_sprite()

                                    # obtention de la valeur max de crossing time
                                    list_move_time = []
                                    for poke_selected in liste_personnages_selected:
                                        list_move_time.append(poke_selected.get_number())
                                    if len(list_move_time) == 0:
                                        max_move_time = 0
                                    else:
                                        max_move_time = max(list_move_time)

                                    # gestion du crossing_time
                                    if search(f"Current crossing time : {current_crossing_time} \(\+[1-9]+\)",
                                              poke_text):
                                        pattern = f"Current crossing time : {current_crossing_time} \(\+[1-9]+\)"
                                    elif search(f"Current crossing time : {current_crossing_time}", poke_text):
                                        pattern = f"Current crossing time : {current_crossing_time}"
                                    poke_text = sub(pattern, '', poke_text)
                                    # rajouter le nom de ce poke + son number au texte affiché
                                    poke_text += f"{poke.get_name()}         {poke.get_number()}\n"
                                    poke_selection_change = True

                                else:
                                    bool_prof_chen_text = True
                                    time_start_affichage_text = pygame.time.get_ticks()
                                    prof_chen_text = "Sélection impossible !\nLa torche n'est pas de ce coté !"

                            else:
                                bool_prof_chen_text = True
                                time_start_affichage_text = pygame.time.get_ticks()
                                prof_chen_text = "Sélection impossible !\nIl a déjà 2 pokémons sélectionnés !"

                        else:
                            poke.unselect(liste_personnages_selected)
                            poke.set_sprite()

                            # obtention de la valeur max de crossing time
                            list_move_time = []
                            for poke_selected in liste_personnages_selected:
                                list_move_time.append(poke_selected.get_number())
                            if len(list_move_time) == 0 :
                                max_move_time = 0
                            else :
                                max_move_time = max(list_move_time)

                            # gestion de l'affichage du crossing time
                            if search(f"Current crossing time : {current_crossing_time} \(\+[1-9]+\)", poke_text):
                                pattern = f"Current crossing time : {current_crossing_time} \(\+[1-9]+\)"
                            elif search(f"Current crossing time : {current_crossing_time}", poke_text) :
                                pattern = f"Current crossing time : {current_crossing_time}"
                            poke_text = sub(pattern, '', poke_text)
                            poke_selection_change = True
                            ## enlever le nom de ce poke + son number au texte affiché
                            poke_regex_search = f"{poke.get_name()}         {poke.get_number()}\n"
                            poke_text = sub(poke_regex_search, '', poke_text)




                        # Affichage des poké selected
                        for poke_selected in liste_personnages_selected :
                            print(poke_selected.get_name())


        # Affichage des éléments de jeu



        pygame.display.flip()
        clock.tick(60)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):  # Vérifie si play est cliqué
                menu = False
                game_loop()  # Lancer la boucle de jeu principale

    # Affichage du menu
    if menu:
        screen.blit(bg_menu, (0, 0))
        screen.blit(button_play, play_rect.topleft)  # Affiche l'image du bouton play
        pygame.display.flip()

pygame.quit()
