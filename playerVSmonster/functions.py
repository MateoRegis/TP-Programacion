from data import * 


def go_cave():
    print(f"{cave}\n")
    index = 0
    #Le mostramos la lista de monstruos
    for monster in monsters:
        print(f"{index + 1}-{monster}")
        index += 1
    index_monster = int(input("Seleccione un monstruo o 0 para salir: "))
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
    elif index_monster == 0:
        menu()
    else:
        print("Opción incorrecta.")



def buy_health():
    print("\nCada 10% de salud que quiera comprar cuesta 10 monedas de oro\n")
    while True:
        option = int(input("Seleccione 1 si quiere comprar, o 0 para cancelar: "))
        if option == 1:
            store.BuyHealth(player1)
        elif option == 0:
            break
        else:
            print("Opción incorrecta.\n")

def sell_weapon():
    print("\nArmas disponibles del jugador: ")
    index = 0
    if len(player1.GetWeapon()) > 1 and weapons[0] in player1.GetWeapon():
        for weapon in player1.GetWeapon():
            print(f"{index + 1}-{weapon}")
            index += 1

        index_weapon = int(input("Seleccione el arma que quiere vender: "))
        weapon_selected = player1.get_selected_weapon(index_weapon - 1)
        store.SellWeapon(player1, weapon_selected)
    else:
        print("No puedes vender tu arma.\n")

def buy_weapon():
    index_weapon = show_weapons() - 1
    if index_weapon == 0:
        #Si el indice es 0, significa que eligio la stick, entonces lo dejamos comprar si no la tiene
        weapon_selected = weapons[index_weapon]
        store.BuyWeapon(player1, weapon_selected)
    elif index_weapon == 1:
        #si el indice es 1, significa que eligio la dagger, entonces tenemos que verificar si tiene la stick
        if weapons[0] in player1.GetWeapon():
            weapon_selected = weapons[index_weapon]
            store.BuyWeapon(player1, weapon_selected)
        else:
            print("No puede comprar esta arma, primero debe comprar el arma anterior.")
    elif index_weapon == 2:
        if weapons[1] in player1.GetWeapon():
            weapon_selected = weapons[index_weapon]
            store.BuyWeapon(player1, weapon_selected)
        else:
            print("No puede comprar esta arma, primero debe comprar el arma anterior.")
    elif index_weapon == 3:
        if weapons[2] in player1.GetWeapon():
            weapon_selected = weapons[index_weapon]
            store.BuyWeapon(player1, weapon_selected)
        else:
            print("No puede comprar esta arma, primero debe comprar el arma anterior.")
    else:
        print("Opción incorrecta.")
            

def show_weapons():
    print("\nArmas disponibles: ")
    index = 0
    for weapon in weapons:
        print(f"{index + 1}-{weapon}\n")
        index += 1

    index_weapon = int(input("Seleccione un arma: "))
    
    return index_weapon

def show_player():
    print(player1)

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
        print("3.Ver datos del jugador")
        print("4.Salir\n")
        option = int(input("Elija una opción: "))

        if option == 1:
            menu_store()
        elif option == 2:
            go_cave()
        elif option == 3:
            show_player()
        elif option == 4:
            print("Saliendo del juego...")
            break
        else:
            print("Opción incorrecta.")

menu()