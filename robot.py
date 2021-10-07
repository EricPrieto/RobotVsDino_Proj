from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon()
    
        def weapon_status (self):
            weapon = input(""" SELECT your weapon from list below for {self.name}: 
            /n 1 for Gatling Gun with power of 20
            /n 2 fro Pac-3 with power of 25 
            /n or 3 for MisselS with power of 50""")
            self.weapon.weapon_selection(weapon)
            print(weapon)
            
            
            
        
        #print(f"Your weapon is {self.weapon_name} and has a power of {self.attack_power}")

        def attack_dino(self, dinosaur):
            pass