from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robots = []

        
    def create_fleet(self):
        bot1 = Robot("XYZ")
        bot2 = Robot("Vince")
        bot3 = Robot("Doom")
        self.robots.append(bot1)
        self.robots.append(bot2)
        self.robots.append(bot3)
    
    