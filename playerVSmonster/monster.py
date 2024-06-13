import math
import random

class Monster:
    def __init__(self, name, level, health):
        self.__name = name
        self.__level = level
        self.__health = health

    def __str__(self):
        return f"Monstruo: {self.__name}\nNivel: {self.__level}\nSalud: {self.__health}\n"
    
    def getMonsterAttackValue(self, xp):
        hit = (self.__level * 5) - (math.floor(random.random() * xp))
        if hit > 0:
            return hit
        else:
            return 0
        
    def get_health(self)->int:
        return self.__health
    
    def set_health(self, health):
        self.__health = health

    def get_level(self)->int:
        return self.__level