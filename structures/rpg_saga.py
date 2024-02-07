import random
from heroes.knight import Knight
from heroes.mage import Mage
from heroes.archer import Archer
from structures.logger import logger

class RPGSaga:
    def __init__(self, num_players):
        self.players_names = ["Эльдар", "Артур", "Гэндальф", "Вильямс"]
        self.players = []
        for _ in range(num_players):
            player_class = random.choice([Knight, Mage, Archer])
            name = random.choice(self.players_names)
            self.players_names.remove(name)
            player = player_class(name)
            self.players.append(player)
            logger.log(f"Игрок ({type(player).__name__}) {player.name} создан (Здоровье: {player.health}, Сила: {player.strength})")

    def start_game(self):
        round_num = 1
        while len(self.players) > 1:
            logger.log(f"\nКон {round_num}.")
            self.battle()
            round_num += 1
        logger.log(f"Победитель: ({type(self.players[0]).__name__}) {self.players[0].name}")

    def battle(self):
        random.shuffle(self.players)
        players_to_remove = []
        for i in range(0, len(self.players), 2):
            if i + 1 < len(self.players):
                player1 = self.players[i]
                player2 = self.players[i + 1]
                logger.log(f"({type(player1).__name__}) {player1.name} vs ({type(player2).__name__}) {player2.name}")
                self.perform_combat(player1, player2, players_to_remove)

        for player in players_to_remove:
            self.players.remove(player)

    def perform_combat(self, player1, player2, players_to_remove):
        while player1.health > 0 and player2.health > 0:
            self.execute_turn(player1, player2)
            if player2.health <= 0:
                logger.log(f"({type(player2).__name__}) {player2.name} погибает\n")
                players_to_remove.append(player2)
                break

            self.execute_turn(player2, player1)
            if player1.health <= 0:
                logger.log(f"({type(player1).__name__}) {player1.name} погибает\n")
                players_to_remove.append(player1)
                break

    def execute_turn(self, attacker, defender):
        if not attacker.skip_turn:
            attacker.attack(defender)
        else:
            attacker.skip_turn = False
            logger.log(f"({type(attacker).__name__}) {attacker.name} заворожён и пропускает ход")