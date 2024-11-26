# Classe Personnage & Torche
import pygame

class Personnage() :
    def __init__(self, number, name, sprite_directory_path, position = 0, x = 0, y = 0, taille= 50):
        self.name = name
        self.number = number
        self.position = position
        self.selected = 0
        self.taille = taille
        self.sprite_directory_path = sprite_directory_path
        self.sprite = pygame.image.load(self.sprite_directory_path+'\\'+self.name+'_0.png')
        self.sprite = pygame.transform.scale(self.sprite, (self.taille,self.taille))
        self.rect = self.sprite.get_rect(center=(x,y))

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_position(self):
        return self.position

    def get_selected(self):
        return self.selected

    def get_sprite(self):
        return self.sprite
    def get_rect(self):
        return self.rect

    def set_nom(self, new_name):
        self.name = new_name

    def set_number(self, new_number):
        self.number = new_number

    def set_position(self, new_position):
        self.position = new_position

    def set_sprite(self, selected : bool):
        if selected == False :
            if self.position == 0:
                sprite_extension = '_0.png'
            else :
                sprite_extension = '_1.png'
        else :
            if self.position == 0:
                sprite_extension = '_0_selected.png'
            else :
                sprite_extension = '_1_selected.png'
        self.sprite = pygame.image.load(self.sprite_directory_path + '\\' + self.name + sprite_extension)
        self.sprite = pygame.transform.scale(self.sprite, (self.taille, self.taille))

    def __str__(self):
        return  self.get_name()

    def select(self, liste_personnages_selected):
        # ajouter le code quand le personnage est selectionné
        liste_personnages_selected.append(self)
        self.selected = 1

    def unselect(self, liste_personnages_selected):
        # ajouter le code quand le personnage est selectionné
        liste_personnages_selected.remove(self)
        self.selected = 0


class Torche() :
    def __init__(self, position = 0):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position