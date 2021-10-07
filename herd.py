from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dinosaurs = []

        
    def create_herd(self):
        dino1 = Dinosaur("Deno",20)
        dino2 = Dinosaur("Lizardo", 25)
        dino3 = Dinosaur("Godzilla", 40)
        self.dinosaurs.append(dino1)
        self.dinosaurs.append(dino2)
        self.dinosaurs.append(dino3)