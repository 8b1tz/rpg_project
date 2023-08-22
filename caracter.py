from abc import ABC, abstractmethod
import random
from arena import ArenaBattle
from map import Map

class CaractherPrincipal(ABC):

    def __init__(self, name):
        self._name = name
        self._class_c = self.__class__.__name__
        self._attributes = {}
        self._max_life = 100
        self._level = 1
        self._points_atributes = 0
        self._ArenaBattle = None
        self._gold = 100.0
        self._xp = 0
        self._map = Map(self)
        self._current_life = 100
    @property
    def xp(self):
        return self._xp

    @property
    def current_life(self):
        return self._current_life
    
    @property
    def name(self):
        return self._name

    @property
    def max_life(self):
        return self._max_life
    
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
    
    @property
    def attributes(self):
        return self._attributes
    
    @property
    def map(self):
        return self._map
    
    @staticmethod
    def upgrade_level(self):
        self._level += 1
        self._points_attributes += 1

    def add_gold(self, value):
        self.gold += value

    def add_points(self):
        self.points_atributes += 1

    def put_point_in_atribute(self, point, attribute):
        self.attributes[attribute] += point
    
    def enter_battle(self):
        self.ArenaBattle = ArenaBattle()

    def verify_equipaments(self, value):
            if value in self.equipaments_use:
                self.accurence_equipament = value

    def lose_gold(self, amount):
        self.gold = max(0, self.gold - amount)

    def gain_xp(self, amount):
        self._xp += amount
        if self._xp >= self.xp_to_next_level():
            self._xp -= self.xp_to_next_level()
            self.upgrade_level()

    def xp_to_next_level(self):
        return 104.2 * self._level  

    def distribute_attribute_points(self):
        while self.points_atributes > 0:
            print(f"Você tem {self.points_atributes} ponto(s) de atributo disponíveis.")
            print("Escolha um atributo para aumentar:")
            print("1. Força")
            print("2. Agilidade")
            print("3. Inteligência")
            print("4. Velocidade")
            
            choice = input("Escolha uma opção (1/2/3/4): ")
            if choice in ["1", "2", "3", "4"]:
                attribute = self.attribute_choices[int(choice) - 1]
                self.attributes[attribute] += 1
                self.points_atributes -= 1
            else:
                print("Escolha inválida. Tente novamente.")

    @abstractmethod
    def add_skill_points(self, point):
        pass

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def skill(self):
        pass
    
    def __str__(self):
        return f'PLAYER: {self.name} CLASSE: {self.__class__.__name__} LEVEL: {self.level}\nVIDA: {self.current_life}/{self.max_life} | XP: {self.xp}/{self.xp_to_next_level()}\n'

class Mage(CaractherPrincipal):
    def __init__(self, name):
        super().__init__(name)
        self._attributes = {
            'force' : '1',
            'agilite' : '1',
            'inteligence' : '3',
            'speed' : '1'
        }
        self._skills = ['METEORO']
        self._equipaments_use = ['CAJADO', 'VARINHA']
        self._accurence_equipament = None
    
    
    def add_skill_points(self, point):
        pass

    def attack(self):
        damage = (int(self.attributes['force']) * 2) + (float(self.attributes['inteligence']) * 1.5) + random.randint(3, 2 * (int(self.attributes['force']) + int(self.attributes['inteligence'])))
        return damage
    
    def skill(self):
        pass
    
    def desc(self):
        print('oi')

class Warrior(CaractherPrincipal):
    def __init__(self, name):
        super().__init__(name)
        self.attributes = {
            'force' : '3',
            'agilite' : '1',
            'inteligence' : '1',
            'speed' : '1'
        }
        self.equipaments_use = ['ESPADA', 'ADAGA']
        self.accurence_equipament = None

    def attack(self):
        damage = (int(self.attributes['force']) * 2) + (float(self.attributes['inteligence']) * 1.5) + random.randint(3, 2 * (int(self.attributes['force']) + int(self.attributes['inteligence'])))
        return damage
    
    def add_skill_points(self, point):
        pass

    def skill(self):
        pass

class Archer(CaractherPrincipal):
    def __init__(self, name):
        super().__init__(name)
        self.attributes = {
            'force' : '1',
            'agilite' : '3',
            'inteligence' : '1',
            'speed' : '1'
        }
        self.equipaments_use = ['ARCO', 'BESTA']
        self.accurence_equipament = None

    def attack(self):
        damage = (int(self.attributes['force']) * 2) + (float(self.attributes['inteligence']) * 1.5) + random.randint(3, 2 * (int(self.attributes['force']) + int(self.attributes['inteligence'])))
        return damage
    
    def skill(self):
        pass
    
    def add_skill_points(self, point):
        pass