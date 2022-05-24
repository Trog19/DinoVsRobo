from weapon import weapons

class Robot:
    def __init__(self, name):
        self.name = name
        self.health= 100
        self.attack_weapon= weapons("Plasma Coil", 50) #attack power based on weapon

    def attack(self, dinosaur):
        dinosaur.health -= self.attack_weapon.power 
