import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.strength = random.randint(10, 30)
        self.skip_turn = False

    def choose_ability(self):
        return random.choice(["normal", "special"])

    def attack(self, opponent):
        ability = self.choose_ability()
        if ability == "special":
            self.special_ability(opponent)
        else:
            self.normal_ability(opponent)

    def normal_ability(self, opponent):
        damage = self.strength
        opponent.health -= damage
        logger.log(f"({type(self).__name__}) {self.name} наносит урон {damage} противнику ({type(opponent).__name__}) {opponent.name}")

    def special_ability(self, opponent):
        pass


class Knight(Player):
    def __init__(self, name):
        super().__init__(name)

    def special_ability(self, opponent):
        damage = int(self.strength * 1.3)
        opponent.health -= damage
        logger.log(f"({type(self).__name__}) {self.name} использует (Удар возмездия) и наносит урон {damage} противнику ({type(opponent).__name__}) {opponent.name}")


class Mage(Player):
    def __init__(self, name):
        super().__init__(name)

    def special_ability(self, opponent):
        logger.log(f"({type(self).__name__}) {self.name} использует (Заворожение) на противнике ({type(opponent).__name__}) {opponent.name}")
        opponent.skip_turn = True


class Archer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.fire_arrows_used = False
        self.fire_damage = 2
        self.fire_effect = False

    def special_ability(self, opponent):
        if not self.fire_arrows_used:
            logger.log(f"({type(self).__name__}) {self.name} использует (Огненные стрелы) и противник ({type(opponent).__name__}) {opponent.name} загорается")
            self.fire_arrows_used = True
            self.fire_effect = True
        else:
            self.normal_ability(opponent)

    def apply_fire_damage(self, opponent):
        if self.fire_effect:
            logger.log(f"({type(opponent).__name__}) {opponent.name} горит и получает {self.fire_damage} урона от огня")
            opponent.health -= self.fire_damage

    def attack(self, opponent):
        ability = self.choose_ability()
        if ability == "special":
            self.special_ability(opponent)
        else:
            self.normal_ability(opponent)
        self.apply_fire_damage(opponent)


class Logger:
    def log(self, message):
        with open("game_log.txt", "a", encoding="utf-8") as file:
            file.write(message + '\n')

logger = Logger()


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

while True:
    try:
        num_players = int(input("Введите количество игроков (от 2 до 4): "))
        if 2 <= num_players <= 4:
            break
        else:
            print("Пожалуйста, введите число от 2 до 4.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

game = RPGSaga(num_players)
game.start_game()