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
            if weapon not in player.GetWeapon():
                if player.add_weapon(weapon):
                    print(f"\nEl jugador {player.get_name()} compró el arma:\n\n{weapon}") # # Si el jugador tiene suficiente oro  el arma se agrega al inventario del jugador
                    gold = player.get_gold() - weapon.get_price()
                    player.set_gold(gold)
            else:
                print("No puede comprar la misma arma dos veces.")
        else:
            print("No tienes suficiente oro.")

        

    def SellWeapon(self, player:Player, weapon:Weapon):
        
        if weapon in player.GetWeapon():
            player.remove_weapon(weapon)
            gold = player.get_gold() + weapon.get_price() 
            player.set_gold(gold)
            print(f"\n{player.get_name()} ha vendido:\n\n{weapon.__str__()}")
        

        

    def BuyHealth(self, player:Player):
        if player.get_gold() >= 10:
            health = player.get_health() + 10
            player.set_health(health)
            gold = player.get_gold() - 10
            player.set_gold(gold)
            print(f"\n{player.get_name()} ha comprado 10 puntos de salud\n")
        else:
            print("\nOro insuficiente.\n")
    
    
    def change_xp_for_gold(self, player:Player, xp, gold):
        new_xp = player.get_xp() - xp
        player.set_xp(new_xp)
        new_gold = player.get_gold() + gold
        player.set_gold(new_gold)
        print(f"\nCompraste {gold} monedas de oro.\n")