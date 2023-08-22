import random
class Game:
    def __init__(self, caracter) -> None:
        self._caracter = caracter
    
    @property
    def caracter(self):
        return self._caracter
    
    @staticmethod
    def generate_monsters(list_monster):
        return random.choice(list_monster)

    @staticmethod
    def generate_items(list_itens):
        pass