from fleet import Fleet
from herd import Herd
import random

from weapon import Weapon

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()

    def display_welcome(self):
        print("Welcome to ROBOTS vs DINOSAURS !_!")
        
    def battle(self):
        pass

    def dino_turn(self, dinosaur):
        pass
    
    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass

