from heroes.player import Player
from structures.logger import logger

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