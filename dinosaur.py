#Creat class for Dino

class Dinosaur:
    def __init__(self, name, attack_power):
        self.name= name
        self.health= 150
        self.attack= int(attack_power) #attack power selected randomly [5, 15, 30]
    
    # def Dino_Health(self):
    #     for robo_attack in self.health -= weapon_one

    
    
    def dino_attack(self, robot):
        robot.health -= self.attack
