from location import Location
from player import Player
from weapon import Weapon

class Store(Location):

    def __init__(self, name, message):
        super().__init__(name, message)

    def __str__(self):
        return f"{self._message}"

    def BuyWeapon(self, player:Player, weapon:Weapon):
        if player.get_gold() >= weapon.get_price():
            if player.add_weapon(weapon):
                print(f"El jugador {player.get_name()} compró el arma:\n{weapon}") # # Si el jugador tiene suficiente oro  el arma se agrega al inventario del jugador
                player.set_gold(weapon.get_price())
        else:
            print("No tienes suficiente oro.")

        

    def SellWeapon(self, player:Player, weapon:Weapon):
        if weapon in player.__weapon:
            player.__weapon.remove(weapon)  
            player.__gold += weapon.__price // 2
            print(f"{player.__name__} ha vendido {weapon.__name__}.")

        

    def BuyHealth(self, player:Player):
        if player.__gold >= 10:
            player.__health += 10
            player.__gold -= 10
            print(f"{player.__name} ha comprado 10 puntos de salud")
    
    
    def Exit(self):
        super().Exit()