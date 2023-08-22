from game import Game
from caracter import Mage, Warrior, Archer

class Menu:
    def __init__(self):
        self.game = None
        self.caracter = None

    def create_caracter(self):
        list_class = ['Mage', 'Warrior', 'Archer']
        class_c = input(f'Qual a classe do seu personagem? [{", ".join(list_class)}]').title()
        nome = input('Qual o nome do seu personagem? ')
        self.caracter = globals()[class_c](nome)
        self.game = Game(self.caracter)
        return self.game
    
    def load_game(self):
        pass

    def exit_game(self):
        print('ok')
