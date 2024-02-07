from heroes.player import Player
from structures.logger import logger

class Mage(Player):
    def __init__(self, name):
        super().__init__(name)

    def special_ability(self, opponent):
        logger.log(f"({type(self).__name__}) {self.name} использует (Заворожение) на противнике ({type(opponent).__name__}) {opponent.name}")
        opponent.skip_turn = True