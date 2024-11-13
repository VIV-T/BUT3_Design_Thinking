# Classe Personnage & Torche


class Personnage() :
    def __init__(self, number, name, sprite, position = 0):
        self.name = name
        self.number = number
        self.position = position
        self.sprite = sprite

    def get_name(self):
        return self.name

    def get_number(self):
        return self.number

    def get_position(self):
        return self.position

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
        pass


class Torche() :
    def __init__(self, position = 0):
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position