import pygame
import logique
from personnages import Personnage, Torche
import os

# creation du project_path & du sprite_path
project_path = os.getcwd()
sprites_path = project_path + "\\sprite"

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("escape the jungle")
main_theme = sprites_path+'\\main_theme.mp3'
pygame.mixer.music.load(main_theme)
pygame.mixer.music.play()

# Chargement des images
icon = pygame.image.load(sprites_path+'\\icon.png')
button_play = pygame.image.load(sprites_path+'\\PlayBtn.png')
bg_jeu = pygame.image.load(sprites_path+'\\background_0.png')
bg_menu = pygame.image.load(sprites_path+'\\bg_menu.png')
fg_jeu = pygame.image.load(sprites_path+'\\front_game.png')
hub_animal_select = pygame.image.load(sprites_path+'\\hud_animals.png')
button_valid = pygame.image.load(sprites_path+'\\hud_valid.png')

# Creation des personnages/animaux
pikachu = Personnage(1,"pikachu")
poussifeu = Personnage(2,"poussifeu")
lokhlass = Personnage(5,"lokhlass")
ronflex = Personnage(7,"ronflex")



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
valid_rect = button_valid.get_rect(center=(1200, 640))
fg_jeu_rect = fg_jeu.get_rect(center=(640, 360))

running = True
menu = True

# initialisation perso
dico_choix_animaux : dict[str : Personnage] = {"pikachu" : pikachu, "poussifeu" : poussifeu, "lokhlass" : lokhlass, "ronflex" : ronflex}

torche = Torche(0)
temps_tot = 0
liste_personnages_selected: list[Personnage] = []

def game_loop():
    # boucle de la partie
    playing = True
    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if valid_rect.collidepoint(event.pos):  # Vérifie si valider est cliqué
                    print("test")
                for poke in dico_choix_animaux.values() :
                    if poke.get_rect().collidepoint(event.pos) :
                        print(poke.get_name())


        # Affichage des éléments de jeu
        screen.blit(bg_jeu, (0, 0))  # Fond de jeu
        screen.blit(fg_jeu, fg_jeu_rect.topleft)  # Avant-plan positionné
        screen.blit(button_valid, valid_rect.topleft)  # Affiche le boutton valider
        screen.blit(hub_animal_select, hub_animal_rect)
        for poke in dico_choix_animaux.values():
            screen.blit(poke.get_sprite(), poke.get_rect())
 

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
