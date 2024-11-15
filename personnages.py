# Classe Personnage & Torche
import pygame

class Personnage() :
    def __init__(self, number, name, position = 0):
        self.name = name
        self.number = number
        self.position = position
        self.selected = 0
        self.sprite = pygame.image.load('C:/Users/loicm/Downloads/'+self.name+'.png')
        self.sprite = pygame.transform.scale(self.sprite, (50,50))
        self.rect = self.sprite.get_rect(center=(60,620))

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