import random
from secrets import choice 
from robot import Robot
from dinosaur import Dinosaur
from weapon import weapons

turn=[1, 2, 3, 4, 5, 6]
class Battlefield:
    def __init__(self):
        self.dinosaur_one= Dinosaur('Little Foot', 30)
        self.robot_one= Robot("Clap Trap")
        self.weapon_one = weapons("Plasma Coil", 50)

    def run_game(self):
        print ('Welcom to Robot versus Dino Fight Night!')
        print (f'Representing Team Robot is {self.robot_one.name} and fighting for Team Dino is {self.dinosaur_one.name}!')
        print (f'{self.robot_one.name} will be fighting with the {self.weapon_one.name} that has an attack power of {self.weapon_one.power}!')
        self.battle_phase()
        self.display_winner

    def battle_phase(self):
        while self.dinosaur_one.health > 0 and self.robot_one.health > 0:
            attack_turn= (random.choice(turn))
        if attack_turn > 3:
            self.dinosaur_one.dino_attack(self.robot_one)
            return self.battle_phase
        if attack_turn < 3:
            self.robot_one.attack(self.dinosaur_one)
            return self.battle_phase
        else:
            self.display_winner()
        

    def display_winner(self): 
        if self.robot_one.health <= 0:
            print(f'{self.dinosaur_one.name} is the WINNER!!!!')
        elif self.dinosaur_one.health <= 0:
            print(f'{self.robot_one.name} is the WINER!!!!!')        



#             def battle_phase(self):
# #         while self.dinosaur_one.health > 0 and self.robot_one.health > 0:
# #             self.dinosaur_one.dino_attack(self.robot_one)
# #             self.robot_one.attack(self.dinosaur_one)
# #         else:
# #             self.display_winner()