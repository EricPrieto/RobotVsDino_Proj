from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("Ozzie", 10)
    
    def attack_dino(self, dinosaur):
       pass