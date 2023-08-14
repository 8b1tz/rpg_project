from abc import ABC, abstractmethod
import random

class Menu:
    def __init__(self):
        self.game = Game()
        self.caracter = None

    def create_caracter(self):
        list_class = ['MAGE', 'SUPORT', 'WARRIOR', 'ARCHER']
        class_c = input(f'Qual a classe do seu personagem? [{", ".join(list_class)}]')
        nome = input('Qual o nome do seu personagem? ')
        self.caracter = CaractherPrincipal(nome, class_c)
    
    def load_game(self):
        pass

    def exit_game(self):
        print('ok')


class Game:
    def __init__(self, caracter) -> None:
        self.caracter = caracter
    
    def generate_monsters(self):
        pass

    def generate_items(self):
        pass

class Monster:
    def __init__(self, max_life, level, attributes):
        self.max_life = max_life
        self.level = level
        self.attributes = attributes

    def attack(self):
        pass
    
    def up_hearth(self):
        pass

class Boss(Monster):
    pass

class CaractherPrincipal(ABC):

    def __init__(self, name, class_c):
        self.name = name
        self.health = 100
        self.level = 1
        self.attributes = class_c['attributes']
        self.skill = class_c['skills']
        self.points_atributes = 0
        self.ArenaBattle = None
        self.gold = 100.0

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def level(self):
        return self._level

    @property
    def attributes(self):
        return self._attributes

    @property
    def skills(self):
        return self._skills

    @property
    def points_atributes(self):
        return self._points_atributes

    @property
    def ArenaBattle(self):
        return self._ArenaBattle

    @property
    def gold(self):
        return self._gold
    
    def add_gold(self, value):
        self.gold += value

    def upgrade_level(self):
        self.level += 1

    def add_points(self):
        self.points_atributes += 1

    def put_point_in_atribute(self, point, attribute):
        self.attributes[attribute] += point
    
    def enter_battle(self):
        self.ArenaBattle = ArenaBattle()

    def verify_equipaments(self, value):
            if value in self.equipaments_use:
                self.accurence_equipament = value
    
    @abstractmethod
    def add_skill_points(self, point):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def skill(self):
        pass


class Mage(CaractherPrincipal):
    def __init__(self, name, class_c):
        super().__init__(name, class_c)
        self.attributes = {
            'force' : '1',
            'agilite' : '1',
            'inteligence' : '3',
            'speed' : '1'
        }
        self.skills = ['METEORO']
        self.equipaments_use = ['CAJADO', 'VARINHA']
        self.accurence_equipament = None
    
    def add_skill_points(self, point):
        pass

    def attack(self):
        damage = (self.attributes['force'] * 2) + (self.attributes['inteligence'] * 1.5) + random.randint(3, 2 * (self.attributes['force'] + self.attributes['inteligence']))
        return damage
    
    def skill(self):
        pass

class Warrior(CaractherPrincipal):
    def __init__(self, name, class_c):
        super().__init__(name, class_c)
        self.attributes = {
            'force' : '3',
            'agilite' : '1',
            'inteligence' : '1',
            'speed' : '1'
        }
        self.equipaments_use = ['ESPADA', 'ADAGA']
        self.accurence_equipament = None

    def attack(self):
        damage = (self.attributes['force'] * 2) + (self.attributes['agilite'] * 0.5) + random.randint(3, 2 * (self.attributes['force'] + self.attributes['agilite']))
        return damage
    
    def add_skill_points(self, point):
        pass

    def skill(self):
        pass

class Archer(CaractherPrincipal):
    def __init__(self, name, class_c):
        super().__init__(name, class_c)
        self.attributes = {
            'force' : '1',
            'agilite' : '3',
            'inteligence' : '1',
            'speed' : '1'
        }
        self.equipaments_use = ['ARCO', 'BESTA']
        self.accurence_equipament = None

    def attack(self):
        damage = (self.attributes['force'] * 2) + (self.attributes['speed'] * 0.5) + random.randint(3, 2 * (self.attributes['force'] + self.attributes['speed']))
        return damage
    
    def skill(self):
        pass
    
    def add_skill_points(self, point):
        pass

class ArenaBattle:
    def start_battle(self, player, enemy):
        player_health = player.health
        enemy_health = enemy.max_life
        
        while player_health > 0 and enemy_health > 0:
            player_damage = player.attack()
            enemy_damage = enemy.attack()
            
            print(f"{player.name} atacou {enemy.__class__.__name__} e causou {player_damage} de dano.")
            enemy_health -= player_damage
            
            if enemy_health <= 0:
                print(f"{enemy.__class__.__name__} foi derrotado!")
                player.add_gold(random.randint(3, enemy.level + enemy.level * 0.5))
                break
            
            print(f"{enemy.__class__.__name__} atacou {player.name} e causou {enemy_damage} de dano.")
            player_health -= enemy_damage
            
            if player_health <= 0:
                print(f"{player.name} foi derrotado!")
                break
            
class Map:
    FLOREST = 'florest'
    CAVERN = 'cavern'
    HOUSE = 'house'
    
class Runner:
    def run(self):
        menu = Menu()
        menu.create_caracter()

runner = Runner()
runner.run()