class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.attack_power = attack_power
        self.health = 100

    def attack_robot(self,robot):
        if robot.health > 0:
            robot.health -= self.health
            print(f"{self.name} attacked {robot.name} and health is down to {robot.health}")
        else:
            print("Opponent has been defeated")