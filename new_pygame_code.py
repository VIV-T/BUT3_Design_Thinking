import pygame
import logique
import personnages

# Initialisation de Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("escape the jungle")
main_theme = 'C:/Users/loicm/Downloads/main_theme.mp3'
pygame.mixer.music.load(main_theme)
pygame.mixer.music.play()

# Chargement des images
"""icon = pygame.image.load('C:/Users/loicm/Downloads/icon.png')
button_play = pygame.image.load('C:/Users/loicm/Downloads/PlayBtn.png')
bg_jeu = pygame.image.load('C:/Users/loicm/Downloads/background_0.png')
bg_menu = pygame.image.load('C:/Users/loicm/Downloads/bg_menu.png')
fg_jeu = pygame.image.load('C:/Users/loicm/Downloads/front_game.png')
button_valid = pygame.image.load('C:/Users/loicm/Downloads/hud_valid.png')
rabbit = pygame.image.load('C:/Users/loicm/Downloads/rabbit.png')
boar = pygame.image.load('C:/Users/loicm/Downloads/boar.png')
hub_animal_select = pygame.image.load('C:/Users/loicm/Downloads/hud_animals.png')"""

# changement icon app
pygame.display.set_icon(icon)

# Redim des images
bg_jeu = pygame.transform.scale(bg_jeu, screen.get_size())
bg_menu = pygame.transform.scale(bg_menu, screen.get_size())
button_play = pygame.transform.scale(button_play, (200, 100))
button_valid = pygame.transform.scale(button_valid, (75,75))
hub_animal_select = pygame.transform.scale(hub_animal_select, (250,100))
fg_jeu = pygame.transform.scale(fg_jeu, (1280, 720))
rabbit = pygame.transform.scale(rabbit, (50,50))
boar = pygame.transform.scale(boar, (50,100))

# Position
hub_animal_rect = hub_animal_select.get_rect(center=(130,60))
play_rect = button_play.get_rect(center=(640, 640))
valid_rect = button_valid.get_rect(center=(1200, 640))
fg_jeu_rect = fg_jeu.get_rect(center=(640, 360))
rabbit_rect = rabbit.get_rect(center=(60,620))
boar_rect = boar.get_rect(center=(150,620))

running = True
menu = True

# initialisation perso
guepard = Personnage(1,"guepard", 0)
lapin = Personnage(2,"lapin", 0)
chevre = Personnage(5,"chevre", 0)
escargot = Personnage(7,"escargot", 0)
dico_choix_animaux : dict[str : Personnage] = {"guepard" : guepard, "lapin" : lapin, "chevre" : chevre, "escargot" : escargot}

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
                if rabbit_rect.collidepoint(event.pos):
                    print("lapin")

        # Affichage des éléments de jeu
        screen.blit(bg_jeu, (0, 0))  # Fond de jeu
        screen.blit(fg_jeu, fg_jeu_rect.topleft)  # Avant-plan positionné
        screen.blit(button_valid, valid_rect.topleft)  # Affiche le boutton valider
        screen.blit(hub_animal_select, hub_animal_rect)
        screen.blit(rabbit, rabbit_rect)
        screen.blit(boar, boar_rect)

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
