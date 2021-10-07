class Weapon:
    def __init__(self):
        self.weapon_name = ''
        self.attack_power = 0

    def weapon_selection(self, selection):
        if selection == "alpha":
            self.weapon_name = "gatling gun "
            self.attack_power = 10
        elif selection == "bravo":
            self.weapon_name = "pac-3"
            self.attack_power = 20
        elif selection == "charlie":
            self.weapon_name = "missel"
            self.attack_power = 30
        
    
    def weapon_status (self):
        print (f"Your weapon is {self.weapon_name} and has a power of {self.attack_power}")


