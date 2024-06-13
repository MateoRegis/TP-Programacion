
import itertools
from location import Location
from weapon import Weapon
from monster import Monster

class Player:
    index = itertools.count()
    

    def __init__(self, name:str, weapon:Weapon) -> None:
        self.__id = next(self.index)
        self.__health = 100
        self.__xp = 0
        self.__gold = 50
        self.__weapon = [weapon]
        self.__name: str = name
        self.__defeat_monsters = []

    def get_gold(self)->int:
        return self.__gold
    
    def add_weapon(self, weapon:Weapon):
        if weapon not in self.__weapon:
            self.__weapon.append(weapon)
            return True
        else:
            print("No se puede comprar el arma porque ya existe en el inventario.")
            return False
        
    def remove_weapon(self, weapon:Weapon):
        self.__weapon.remove(weapon)

    def get_name(self):
        return self.__name
    
    def get_xp(self):
        return self.__xp
    
    def set_xp(self, new_xp):
        self.__xp = new_xp
    
    def get_health(self):
        return self.__health
    

    def set_health(self, healt:int):
        self.__health = healt

    def set_gold(self, gold):
        self.__gold = gold
    
    def get_defeated_monsters(self):
        return self.__defeat_monsters

    

    def add_defeated_monster(self, monster:Monster):
        self.__defeat_monsters.append(monster)


    def __str__(self) -> str:
        return f"Health: {self.__health}\nXP: {self.__xp}\nGold: {self.__gold}\n"
    
    def GetWeapon(self):
        return self.__weapon
    
    def get_selected_weapon(self, index):
        return self.__weapon[index]