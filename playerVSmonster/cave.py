from location import Location
from player import Player
from monster import Monster
from weapon import Weapon
import math
import random

class Cave(Location):

    def __init__(self, name, message):
        super().__init__(name, message)

    def Fight(self, player:Player, monster:Monster, weapon:Weapon):
        print(f"Peleando con el monstruo {monster}")
        if self.attack(player, monster, weapon):
            print("Venciste al monstruo. Felicitaciones!!!")
            player.add_defeated_monster(monster)
            print("Se agrego el montruo a lalista de monstruos vencidos.")

    def Exit(self):
        super().Exit()

    def __str__(self):
        return f"{self._message}"
    

    def isMonsterHit(self, player:Player):
        if random.random() > 0.2 or player.get_health() < 20:
            return True
        return False
    

    def attack(self, player:Player, monster:Monster, weapon:Weapon):
        banTerminar = False
        gano = False
        while True:
            player.set_health(monster.getMonsterAttackValue(player.get_xp()))
            if self.isMonsterHit(player):
                monster.set_health(weapon.get_power() + math.floor(random.random() * player.get_xp() + 1))
            else:
                print("Erraste.")
            
            
            if (player.get_health() <= 0):
                print("Perdiste.")
                banTerminar = True
                
            elif (monster.get_health() <= 0):
                print("Ganaste")
                banTerminar = True
                gano = True
                
            
            if random.random() <= 0.1 and len(player.GetWeapon()) != 1 :
                print("Tu arma se rompió")
                player.remove_weapon(weapon)

            if banTerminar == True:
                break
            
        
        return gano
   
   
