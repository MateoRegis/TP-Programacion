from weapon import Weapon
from monster import Monster
from cave import Cave
from store import Store
from player import Player

#Vamos a crear las armas
stick = Weapon("Stick", 7, 20)
dagger = Weapon("Dagger", 18, 30)
claw_hammer = Weapon("Claw Hammer", 33, 40)
sword = Weapon("Sword", 50, 50)


#vamos a crear una lista de armas
weapons = []

#en esa lista vamos a añadir las armas que creamos
weapons.append(stick)
weapons.append(dagger)
weapons.append(claw_hammer)
weapons.append(sword)


#ahora vamos a crear los monstruos

slime = Monster("Slime", 3, 15)
fanged_beast = Monster("Fanged Beast", 8, 60)
dragon = Monster("Dragon", 20, 300)

#ahora vamos a crear una lista de monstruos

monsters = []
#en ea lista vamos a ñadir los lomnstruos que creamos
monsters.append(slime)
monsters.append(fanged_beast)
monsters.append(dragon)

#ahora vamos a crear la tienda

store = Store("Store", "Bienvenido a la tienda.")

#ahora creamos la arena

cave = Cave("Cave", "Entraste a la arena. Ves algunos monstruos.")


#ahor avamos a crear un jugador para poder realizar pruebas
player1 = Player("Juancito", stick)

