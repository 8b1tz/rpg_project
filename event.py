from itertools import cycle
from operator import itemgetter
import random

class BaseEventLoop:

    def __init__(self, list_events) -> None:
        self.events_cycle = cycle(list_events)
        
    def next_event(self):
        return next(self.events_cycle)

    def random_next_action(self):
        next_action = self.next_event()
        weight_sum = sum(map(itemgetter(1), self.events[next_action]))
        chosen_weight = random.randint(1, weight_sum)
        iteration_sum = 0
        for item in self.events[next_action]:
            iteration_sum += item[1]
            if chosen_weight <= iteration_sum:
                return item[0]
        
class FlorestEvents(BaseEventLoop):
    def __init__(self) -> None:
        self.events =  {
            "andar": [
                ("Saiu da floresta", 2),
                ("Encontrou um Viajante", 5),
                ("Encontrou um monstro", 15),
                ("Continuou andando", 78),
            ],
            "explorar": [
                ("Encontrou uma fruta", 15),
                ("Encontrou agua potavel", 5),
                ("Encontrou uma pedra preciosa", 1),
                ("Falha na exploração", 79),
            ],
        }
        super().__init__(self.events.keys())

class CavernEvent(BaseEventLoop):
    def __init__(self) -> None:
        self.events =  {
            "andar": [
                ("Saida da floresta", 2),
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
        super().__init__(self.events.keys())
