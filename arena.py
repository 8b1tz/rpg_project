import random

class ArenaBattle:
    def start_battle(self, player, enemy):
        player_health = player.current_life
        enemy_health = enemy.current_life
        
        while player_health > 0 and enemy_health > 0:
            print(f"SUA VIDA: {player_health}/{player.max_life}", f"VIDA DO INIMIGO: {enemy_health}/{enemy.max_life}")
            
            self.show_player_actions(player)
            player_action = input("Escolha a opção: ")
            
            if player_action == "1":
                self.attack_enemy(player, enemy, player_health, enemy_health)
            elif player_action == "2" and self.try_to_flee():
                print("Você conseguiu fugir!")
                break
            elif player_action == "3" and player.has_potion():
                self.use_potion(player)
            else:
                print("Opção inválida. Escolha novamente.")
                continue
            
            if enemy_health <= 0:
                self.end_battle(player, enemy, True)
                break
            
            self.enemy_attack(player, enemy, player_health)
            
            if player_health <= 0:
                self.end_battle(player, enemy, False)
                break
    
    def show_player_actions(self, player):
        print("Escolha sua ação:")
        print("1. Atacar")
        print("2. Tentar fugir")
        if player.has_potion():
            print("3. Usar poção")
            
    def attack_enemy(self, player, enemy, player_health, enemy_health):
        player_damage = player.attack()
        print(f"{player.name} atacou {enemy.__class__.__name__} e causou {player_damage} de dano.")
        enemy_health -= player_damage
        
    def try_to_flee(self):
        return random.randint(1, 100) <= 30
    
    def use_potion(self, player):
        potion_heal_amount = 20
        player.use_potion(potion_heal_amount)
        print(f"{player.name} usou uma poção e restaurou {potion_heal_amount} de vida.")
        
    def enemy_attack(self, player, enemy, player_health):
        enemy_damage = enemy.attack()
        print(f"{enemy.__class__.__name__} atacou {player.name} e causou {enemy_damage} de dano.")
        player_health -= enemy_damage
        
    def end_battle(self, player, enemy, player_won):
        if player_won:
            coin_reward = random.randint(3, enemy.level + int(enemy.level * 0.5))
            player.add_gold(coin_reward)
            player.gain_xp(enemy.level * 10)
            print(f"{enemy.__class__.__name__} foi derrotado!")
        else:
            player.lose_gold(enemy.level * 5)
            print(f"{player.name} foi derrotado!")
