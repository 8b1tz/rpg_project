from menu import Menu

class Runner:
    def run(self):
        menu = Menu()
        game = menu.create_caracter()
        game_map = game.caracter.map

        while True:
            choose = game_map.choose_destination()
            action = input(f'você deseja andar ou explorar na {choose}? ')
            game_map.visit_current_location(action)

runner = Runner()
runner.run()