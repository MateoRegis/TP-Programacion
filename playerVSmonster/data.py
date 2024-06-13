from weapon import Weapon
from monster import Monster
from cave import Cave
from store import Store

#Vamos a crear las armas
stick = Weapon("Stick", 5, 10)
dagger = Weapon("Dagger", 30, 30)
claw_hammer = Weapon("Claw Hammer", 50, 50)
sword = Weapon("Sword", 100, 60)


#vamos a crear una lista de armas
weapons = []

#en esa lista vamos a añadir las armas que creamos
weapons.append(stick)
weapons.append(dagger)
weapons.append(claw_hammer)
weapons.append(sword)


#ahora vamos a crear los monstruos
slime = Monster("Slime", 2, 15)
fanged_beast = Monster("Fanged Beast", 8, 60)
dragon = Monster("Dragon", 20, 300)

#creamos una lista de monstruos vacia, en esta lista vamos a añadir los monstruos
monsters = []

#en ea lista vamos a ñadir los lomnstruos que creamos
monsters.append(slime)
monsters.append(fanged_beast)
monsters.append(dragon)

#ahora vamos a crear la tienda

store = Store("Store", "Bienvenido a la tienda.")

#ahora creamos la arena

cave = Cave("Cave", "Entraste a la arena. Ves algunos monstruos.")




