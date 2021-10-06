class Weapon:
    def __init__(self, weapon_name, attack_power):
        self.weapon_name = weapon_name
        self.attack_power = attack_power

    def weapon_status (self):
        print (f"Your weapon is {self.weapon_name} and has a power of {self.attack_power}")


