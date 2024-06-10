from data import * 


def go_cave():
    print(f"{cave}\n")
    index = 0
    #Le mostramos la lista de monstruos
    for monster in monsters:
        print(f"{index + 1}-{monster}")
        index += 1
    index_monster = int(input("Seleccione un monstruo: "))
    #en index monster nos guardamos la opcion que selecciona el jugador, esta opcion si le restamos 1 es el indice del monstruo
    

    #si el juugador elige la opcion 2, estaria eligiendo al monstruo en el indice 1, en nuestro caso seria el monstruo fanged_beast, entonces validamos que primero haya vencido al
    # monstruo en el indice 0, que en nuestro caso seria el slime, para seleccionar el slime, como el jugador eligio la opcion 2, lo que hacemos es restarle 2 y asi accedemos al indice 0
    #y lo guardamos en una variable llamada monster_last
    if index_monster == 1:
        monster_selected = monsters[index_monster - 1]
        index = 0
        print("\nArmas disponibles: ")
        for weapon in player1.GetWeapon():
            print(f"{index + 1}-{weapon}")
            index += 1
        
        index_weapon = int(input("Seleccione un arma para luchar: "))
        weapon = player1.get_selected_weapon(index_weapon - 1)
        cave.Fight(player1, monster_selected, weapon)
    elif index_monster == 2:
        monster_last = monsters[index_monster - 2]
        #preguntamos si el mosnter_last esta en la lista de monstruos vencidos del jugador
        if monster_last in player1.get_defeated_monsters():
            #si esta entonces guardamos el mosntruo seleccionado por el usuario y llamamos al metodo fight de cave
            monster_selected = monsters[index_monster - 1]
            index = 0
            print("\nArmas disponibles: ")
            for weapon in player1.GetWeapon():
                print(f"{index + 1}-{weapon}")
                index += 1
            
            index_weapon = int(input("Seleccione un arma para luchar: "))
            weapon = player1.get_selected_weapon(index_weapon - 1)
            cave.Fight(player1, monster_selected, weapon)
        else:
            #si no esta, entonces no lo dejamos seleccionar el monstruo que habia seleccionado
            print("No puedes seleccionar este monstruo, primero debes vencer al anterior.")
    elif index_monster == 3:
        monster_last = monsters[index_monster - 2]
        if monster_last in player1.get_defeated_monsters():
            monster_selected = monsters[index_monster - 1]
            index = 0
            print("\nArmas disponibles: ")
            for weapon in player1.GetWeapon():
                print(f"{index + 1}-{weapon}")
                index += 1
            
            index_weapon = int(input("Seleccione un arma para luchar: "))
            weapon = player1.get_selected_weapon(index_weapon - 1)
            cave.Fight(player1, monster_selected, weapon)
        else:
            print("No puedes seleccionar este monstruo, primero debes vencer al anterior.")
    else:
        print("Opción incorrecta.")



def buy_health():
    pass

def sell_weapon():
    pass

def buy_weapon():
    weapon = show_weapons()
    store.BuyWeapon(player1, weapon)

def show_weapons():
    print("\nArmas disponibles: ")
    index = 0
    for weapon in weapons:
        print(f"{index + 1}-{weapon}\n")
        index += 1

    index_weapon = int(input("Seleccione un arma: "))
    weapon_selected = weapons[index_weapon - 1]
    return weapon_selected

def menu_store():
    print(store)
    while True:
                
                print("\n1.Comprar arma")
                print("2.Vender arma")
                print("3.Comprar salud")
                print("4.Salir de la tienda\n")
                option_store = int(input("Elija una opción: "))

                if option_store == 1:
                    buy_weapon()
                elif option_store == 2:
                    sell_weapon()
                elif option_store == 3:
                    buy_health()
                elif option_store == 4:
                    print("Saliendo de la tienda...")
                    break
                else:
                    print("Opción incorrecta.")


def menu():
    while True:
        print("\n----------------------Menú----------------------\n")
        print("1.Ir a la tienda")
        print("2.Ir a la arena")
        print("3.Salir\n")
        option = int(input("Elija una opción: "))

        if option == 1:
            menu_store()
        elif option == 2:
            go_cave()
        elif option == 3:
            print("Saliendo del juego...")
            break
        else:
            print("Opción incorrecta.")

menu()