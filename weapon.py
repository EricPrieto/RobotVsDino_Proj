class Weapon:
    def __init__(self):
        self.weapon_name = ''
        self.attack_power = 0

    def weapon_selection(self, selection):        
        if selection == "1":
            self.weapon_name = "gatling gun "
            self.attack_power = 20
        elif selection == "2":
            self.weapon_name = "pac-3"
            self.attack_power = 25
        elif selection == "3":
            self.weapon_name = "missel"
            self.attack_power = 50
        
    
    


