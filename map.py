
from event import CavernEvent, FlorestEvents

class Map:
    FLOREST = 'florest'
    CAVERN = 'cavern'
    HOUSE = 'house'

    def __init__(self, caracter):
        self.current_location = self.HOUSE
        self.caracter = caracter

    def choose_destination(self):
        print("Escolha seu destino:")
        print("1. Floresta")
        print("2. Caverna")
        print("3. Casa")
        choice = input("Escolha uma opção (1/2/3): ")

        if choice == "1":
            self.current_location = self.FLOREST
        elif choice == "2":
            self.current_location = self.CAVERN
        elif choice == "3":
            self.current_location = self.HOUSE
        else:
            print("Opção inválida. Escolha novamente.")

    def visit_current_location(self, choose):
        if self.current_location == self.FLOREST:
            florest = FlorestEvents(self.caracter)
            florest.generate_event(choose)
            return self.FLOREST
        elif self.current_location == self.CAVERN:
            CavernEvent(self.caracter)
            return self.CAVERN
        elif self.current_location == self.HOUSE:
            print('nothing...')

