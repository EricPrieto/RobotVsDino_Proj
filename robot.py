from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon("gatling", 30)

        def attack_dino(self, dinosaur):
            if dinosaur.health > 0:
                dinosaur.health -= self.weapon
                print(f"{self.name} attacked {dinosaur.name} and health is down to {dinosaur.health}")
            else:
                print("Opponent has been ELIMINATED")


            print(f"Your weapon is {self.weapon} and has a power of {self.attack_power}")


        # def weapon_status (self):
        #     weapon = input(""" SELECT your weapon from list below for {self.name}: 
        #     /n 1 for Gatling Gun with power of 20
        #     /n 2 fro Pac-3 with power of 25 
        #     /n or 3 for MisselS with power of 50""")
        #     self.weapon.weapon_selection(weapon)
        #     print(weapon)    
