from itertools import cycle
from operator import itemgetter
from arena import ArenaBattle
from monster import Monster
from game import Game

import random

class FlorestEvents:
    monsters = [Monster(100, 1, {'force': 1, 'agilite': 1, 'inteligence': 3, 'speed': 1}),
                Monster(100, 2, {'force': 1, 'agilite': 1, 'inteligence': 1, 'speed': 1})]

    def __init__(self, character) -> None:
        self.character = character
        self.events = {
            "andar": [
                ("Saiu da floresta", self.handle_exit_forest),
                ("Encontrou um Viajante", self.handle_encounter_traveler),
                ("Encontrou um monstro", self.handle_monster_encounter),
                ("Continuou andando", self.handle_continue_walking),
            ],
            "explorar": [
                ("Encontrou uma fruta", self.handle_find_fruit),
                ("Encontrou agua potavel", self.handle_find_water),
                ("Encontrou uma pedra preciosa", self.handle_find_gem),
                ("Falha na exploração", self.handle_exploration_failure),
            ],
        }

    def generate_event(self, choice):
        chosen_event = random.choice(self.events[choice])
        chosen_event()  

    def handle_exit_forest(self):
        print("Você saiu da floresta.")

    def handle_encounter_traveler(self):
        print("Você encontrou um Viajante.")

    def handle_monster_encounter(self):
        monster = random.choice(self.monsters)
        arena_battle = ArenaBattle()
        arena_battle.start_battle(self.character, monster)

    def handle_continue_walking(self):
        print("Você continuou andando.")

    def handle_find_fruit(self):
        print("Você encontrou uma fruta.")

    def handle_find_water(self):
        print("Você encontrou água potável.")

    def handle_find_gem(self):
        print("Você encontrou uma pedra preciosa.")

    def handle_exploration_failure(self):
        print("Sua exploração falhou.")

class CavernEvent:
    def __init__(self) -> None:
        self.events = {
            "andar": [
                ("Saida da caverna", 2),
                ("Encontrar um Viajante", 5),
                ("Encontrar um monstro", 15),
                ("Continua andando", 78),
            ],
            "explorar": [
                ("Encontrou uma fruta", 15),
                ("Encontrou agua potavel", 5),
                ("Encontrou uma pedra preciosa", 1),
                ("Falha na exploração", 79),
            ],
        }

