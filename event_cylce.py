from itertools import cycle
from operator import itemgetter
import random
import time


florest_events = {
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


class BaseEventLoop:
    def __init__(self, list_events) -> None:
        self.events = cycle(list_events)

    def next_event(self):
        return next(self.events)


class FlorestEvents(BaseEventLoop):
    def __init__(self) -> None:
        self.florest_events = florest_events
        list_events = self.florest_events.keys()
        super().__init__(list_events)

    def random_next_action(self):
        next_action = self.next_event()
        weight_sum = sum(map(itemgetter(1), self.florest_events[next_action]))
        chosen_weight = random.randint(1, weight_sum)
        iteration_sum = 0
        for item in self.florest_events[next_action]:
            iteration_sum += item[1]
            if chosen_weight <= iteration_sum:
                return item[0]


if __name__ == "__main__":
    event = FlorestEvents()
    while True:
        print(event.random_next_action())
        time.sleep(0.3)
