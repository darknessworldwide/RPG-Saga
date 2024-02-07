from heroes.player import Player
from structures.logger import logger

class Knight(Player):
    def __init__(self, name):
        super().__init__(name)

    def special_ability(self, opponent):
        damage = int(self.strength * 1.3)
        opponent.health -= damage
        logger.log(f"({type(self).__name__}) {self.name} использует (Удар возмездия) и наносит урон {damage} противнику ({type(opponent).__name__}) {opponent.name}")