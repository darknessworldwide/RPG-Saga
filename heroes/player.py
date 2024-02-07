import random
from structures.logger import logger

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