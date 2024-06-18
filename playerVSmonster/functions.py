from data import * 
from player import Player



################################################################################################################################################################################################################



def initialize_monsters():
    # lo que hago con esto es setear la salud de los monstruos para que quede como al principio del juego
    slime.set_health(15)
    fanged_beast.set_health(60)
    dragon.set_health(300)
    



################################################################################################################################################################################################################




def go_cave(player: Player):
    #dentro de la funcion go cave definimos otra funcion que nos permite seleccionar un arma de nuestro inventario antes de luchar con un montruo
    #luego llamamos al metodo pelear de la clase cave, si devuelve false significa que el jugador perdio y llamamos al funcion validar jugador para saber si el jugador puede seguir jugando
    def select_and_fight(monster):
        show_player_weapons(player)
        index_weapon = int(input("Seleccione un arma para luchar: "))
        weapon = player.get_selected_weapon(index_weapon - 1)
        if cave.Fight(player, monster, weapon) == False:
            validate_player(player)
    
    #si el jugador tiene salud le mostramos los monstruos y lo dejamos que elija uno para pelear
    while player.get_health() > 0:
        initialize_monsters()
        print("\n-------------------Arena-------------------\n")
        print(f"{cave}\n")
        print(f'Salud: {player.get_health()}\n')

        #le mostramos los monstruos disponibles para luchar, enumerate nos permite obtener tanto el indice como el monstruo
        for index, monster in enumerate(monsters, start=1):
            print(f"{index}-{monster}")

        index_monster = int(input("Seleccione un monstruo o 0 para salir: "))
        
        if index_monster == 0:
            #si el jugador selecciona 0 salimos
            break
        elif 1 <= index_monster <= len(monsters):
            #si el indice esta entre 1 y la longitud de la lista de monstruos siginifica que ingreso una opcion correcta
            #seleccionamos el monstruo con el que quiere luchar el jugador
            monster_selected = monsters[index_monster - 1]
            #si el indice es 1, es decir que eligio el slime, lo dejamos luchar
            #si eligio otros monstruos llamamos a la funcion validar monstruo
            if index_monster == 1 or validate_monster(monsters[index_monster - 2], player):
                #si el monstruo es el slime, o si validar monstruo devuelve true lo dejamos pelear llamando a la funcion que creamos antes select and figth
                select_and_fight(monster_selected)
                #luego de luchar, si el indice del monstruo seleccionado es igual a la longitud de la lista monstruos, es decir, si el jugador eligio el ultimo monstruo
                #si eligio el ultimo monstruo y la salud del jugador luego de luchar es mayor a cero, significa que gano, por lo que lo felicitamos y llamamos al menu_lose_win
                if index_monster == len(monsters) and player.get_health() > 0:
                    print(f"\n¡Felicitaciones {player.get_name()}! Has vencido al monstruo final!\n")
                    menu_lose_win(player)
        else:
            #sino le decimos que la opcion ingresada es incorrecta.
            print("\nOpción incorrecta.")
    else:
        #si el jugador no tiene suficiente salud se lo informamos y no lo dejamos elegir ni le mostramos ningun monstruo
        print("\nNo tienes suficiente salud.\n")




################################################################################################################################################################################################################





    ##comento esta funcion porque asi la habia hecho yo, se la pase a chat gpt y me la optimizo, me gustó como lo hizo y lo entiendo
    #pero por las dudas no borro la funcion que hice yo, la dejo comentada, con esa funcion andaba todo a la perfeccion.

# def go_cave(player:Player):
#     while True:
#         if player.get_health() > 0:
#             initialize_monsters()
#             print("\n-------------------Arena-------------------\n")
#             print(f"{cave}\n")
#             index = 0
#             #Le mostramos la lista de monstruos
#             for monster in monsters:
#                 print(f"{index + 1}-{monster}")
#                 index += 1
#             index_monster = int(input("Seleccione un monstruo o 0 para salir: "))
#             #en index monster nos guardamos la opcion que selecciona el jugador, esta opcion si le restamos 1 es el indice del monstruo
#             if index_monster == 1:
#                 monster_selected = monsters[index_monster - 1]
#                 show_player_weapons(player)
                
#                 index_weapon = int(input("Seleccione un arma para luchar: "))
#                 weapon = player.get_selected_weapon(index_weapon - 1)
#                 if cave.Fight(player, monster_selected, weapon) == False:
#                     validate_player(player)
#             elif index_monster == 2:
#                 #si el juugador elige la opcion 2, estaria eligiendo al monstruo en el indice 1, en nuestro caso seria el monstruo fanged_beast, entonces validamos que primero haya vencido al
#                 # monstruo en el indice 0, que en nuestro caso seria el slime, para seleccionar el slime, como el jugador eligio la opcion 2, lo que hacemos es restarle 2 y asi accedemos al indice 0
#                 #y lo guardamos en una variable llamada monster_last
#                 monster_last = monsters[index_monster - 2]
#                 #preguntamos si el mosnter_last esta en la lista de monstruos vencidos del jugador
#                 if validate_monster(monster_last, player):
#                     monster_selected = monsters[index_monster - 1]
#                     show_player_weapons(player)
#                     index_weapon = int(input("Seleccione un arma para luchar: "))
#                     weapon = player.get_selected_weapon(index_weapon - 1)
#                     if cave.Fight(player, monster_selected, weapon) == False:
#                         validate_player(player)
#             elif index_monster == 3:
#                 monster_last = monsters[index_monster - 2]
#                 if validate_monster(monster_last, player):
#                     monster_selected = monsters[index_monster - 1]
#                     show_player_weapons(player)
                    
#                     index_weapon = int(input("Seleccione un arma para luchar: "))
#                     weapon = player.get_selected_weapon(index_weapon - 1)
#                     if cave.Fight(player, monster_selected, weapon) == False:
#                         validate_player(player)
#                     else:
#                         print(f"\nFelicitaciones {player.get_name()} has vencido al monstruo final!\n")
#                         menu_lose_win(player)
#             elif index_monster == 0:
#                 break
#             else:
#                 print("\nOpción incorrecta.")
#         else:
#             print("\nNo tienes suficiente salud.\n")
#             break





################################################################################################################################################################################################################






#esta funcion es igual a la que usamos para validar armas
# lo que hacemos aca es preguntar si el jugador vemcio el monstruo que le estamos pasando por parametro
#el monstruo que le pasamos por parametro es en realidad el monstruo anterior al que el jugador eligio
#esto para validar que si quiere pelear con cierto monstruo, primero haya vencido al anterior
def validate_monster(monster:Monster, player:Player):
    if monster in player.get_defeated_monsters():
        return True
    else:
        print("\nNo puedes seleccionar este monstruo, primero debes vencer al anterior.")
    return False
        



################################################################################################################################################################################################################



#la funcion para comprar salud es bastante sencilla, le decimos cuanto vale y le preguntamos si quiere comprar o no
#llamamos al metodo comprar salud de la clase store
def buy_health(player:Player):
    print("\nCada 10% de salud que quiera comprar cuesta 10 monedas de oro\n")
    while True:
        option = int(input("Seleccione 1 si quiere comprar, o 0 para cancelar: "))
        if option == 1:
            store.BuyHealth(player)
        elif option == 0:
            break
        else:
            print("Opción incorrecta.\n")



################################################################################################################################################################################################################



#para vender armas lo primero que hacemos es verificar si el jugador tiene armas para vender
#luego para dejarlo vender validamos que tenga mas de 1 arma, esto lo hacemos para que no pueda quedarse sin ningun arma
def sell_weapon(player:Player):
    if len(player.GetWeapon()) > 0:
        show_player_weapons(player)
        if len(player.GetWeapon()) > 1:
            index_weapon = int(input("Seleccione el arma que quiere vender: "))
            weapon_selected = player.get_selected_weapon(index_weapon - 1)
            store.SellWeapon(player, weapon_selected)
        else:
            print("No puedes vender tu arma.")
    else:
        print("No tienes armas.\n")




################################################################################################################################################################################################################





#en esta funcion lo que hacemos es llamar a la funcion mostrar armas, que nos devuelve una opcion seleccionada por el jugador, si le restamos 1 se convierte en el indice que podemos usar de la lista de weapons que nosotros tenemos en data
def buy_weapon(player:Player):
    index_weapon = show_weapons() - 1
    if index_weapon == 0:
        #Si el indice es 0, significa que eligio la stick, entonces lo dejamos comprar si no la tiene
        weapon_selected = weapons[index_weapon]
        store.BuyWeapon(player, weapon_selected)
    elif index_weapon == 1:
        #si el indice es 1, significa que eligio la dagger, entonces tenemos que verificar si tiene la stick
        if validate_weapon(weapons[0], player):
            weapon_selected = weapons[index_weapon]
            store.BuyWeapon(player, weapon_selected)
    elif index_weapon == 2:
        #si el indice es 2, significa que eligio la claw hammer, entonces tenemos que verificar si tiene la dagger
        if validate_weapon(weapons[1], player):
            weapon_selected = weapons[index_weapon]
            store.BuyWeapon(player, weapon_selected)
    elif index_weapon == 3:
        #si el indice es 3, significa que eligio la sword, entonces tenemos que verificar si tiene la claw hammer
        if validate_weapon(weapons[2], player):
            weapon_selected = weapons[index_weapon]
            store.BuyWeapon(player, weapon_selected)
    else:
        print("Opción incorrecta.")
            





################################################################################################################################################################################################################





#esta funcion la usamos para saber si un jugador tiene un arma en su inventario
#en realidad el arma que nosotros pasamos a esta funcion por parametro es el arma anterior a la que el jugador quiere comprar, asi validamos que pueda comprar el arma nueva
#esto es porque no permitimos que un jugador pueda comprar un arma sin comprar primero el arma anterior
def validate_weapon(weapon:Weapon, player:Player):
    if weapon in player.GetWeapon():
        return True
    else:
        print("\nNo puede comprar esta arma, primero debe comprar el arma anterior.\n")
    return False





################################################################################################################################################################################################################





#esta funcion la usamos para mostrar las armas que tiene el jugador, esta funcion la llamamos cuando el jugador quiere vender sus armas, le tenemos que mostrar las armas que tiene
def show_player_weapons(player:Player):
    print(f"\nArmas disponibles de {player.get_name()}: ")
    print("")
    index = 0
    for weapon in player.GetWeapon():
        print(f"{index + 1}-{weapon}")
        index += 1





################################################################################################################################################################################################################





#esta funcion la usamos para mostrarle al jugador las armas disponibles para comprar, estas armas estan en la lista weapons que importamos desde data
#nos guardamos el indice (la opcion que selecciona el jugador) y lo retornamos
def show_weapons():
    print("\nArmas disponibles: ")
    print("\n")
    index = 0
    for weapon in weapons:
        print(f"{index + 1}-{weapon}\n")
        index += 1

    index_weapon = int(input("Seleccione un arma: "))
    
    return index_weapon




################################################################################################################################################################################################################




#esta funcion la usamos para mostrar los datos del jugador, lo unico que hacemos es invocar el metodo str de la clase player
def show_player(player:Player):
    print(f"\nDatos de {player.get_name()}\n")
    print(player)




################################################################################################################################################################################################################




#esta funcion que es para comprar oro, muestra un menu al usuario con varias opciones
#lo que hacemos cuando el jugador elige una opcion es validar si le alcanzan los xp
#si los xp le alcanzan llamamos al metodo change xp for gold de la clase store y le pasamos el jugador, los xp que le vamos a restar y el oro que le vamos a sumar
def buy_gold(player:Player):
    print("\nPuedes comprar oro con tus punto de experiencia\n")
    while True:
        print(f"Tus XP: {player.get_xp()}\n")
        print("1- 20 monedas de oro por 50xp\n")
        print("2- 50 monedas de oro por 100xp\n")
        print("3- 100 monedas de oro por 200xp\n")
        print("4- Salir\n")
        option = int(input("Elija una opción: "))
        if option == 1:
            xp = 50
            if validate_xp(player, xp):
                gold = 20
                store.change_xp_for_gold(player, xp, gold)
        elif option == 2:
            xp = 100
            if validate_xp(player, xp):
                gold = 50
                store.change_xp_for_gold(player, xp, gold)
        elif option == 3:
            xp = 200
            if validate_xp(player, xp):
                gold = 100
                store.change_xp_for_gold(player, xp, gold)
        elif option == 4:
            break
        else:
            print("\nOpción incorrecta.")






################################################################################################################################################################################################################




#esta funcion la usamos para saber si un jugador tiene los xp suficientes para comprar oro
def validate_xp(player:Player, xp):
    if player.get_xp() >= xp:
        return True
    else:
        print("\nNo te alcanzan los XP.\n")
    return False





################################################################################################################################################################################################################





#esta funcion muestra el menu de la tienda
#se muestran las opciones y dependiendo de lo que el jugador elija se llaman a la funciones correspondientes
def menu_store(player:Player):
    while True:
                print("\n-------------------------Tienda-------------------------\n")
                print(f"{store}\n")
                print(f'Oro Disponible: {player.get_gold()}\n')
                print("1.Comprar arma\n")
                print("2.Vender arma\n")
                print("3.Comprar salud\n")
                print("4.Comprar oro\n")
                print("5.Salir de la tienda\n")
                option_store = int(input("Elija una opción: "))

                if option_store == 1:
                    buy_weapon(player)
                elif option_store == 2:
                    sell_weapon(player)
                elif option_store == 3:
                    buy_health(player)
                elif option_store == 4:
                    buy_gold(player)
                elif option_store == 5:
                    print("\nSaliendo de la tienda...")
                    break
                else:
                    print("\nOpción incorrecta.")

################################################################################################################################################################################################################





#la funcion restar lo que hace es primero recuperar el nombre del jugador
#luego eliminamos la instancia de ese objeto
#y finalmente creamos una nueva instancia con el mismo nombre del jugador
def restart(player:Player):
    #con esta funcion lo que hacemos es recuperar el nombre del jugador, eliminamos el objeto actual, y creamos un nuevo jugador a partir del nombre recuperado.
    name = player.get_name()
    del player
    new_player = Player(name, weapons[0])
    print("\nReiniciando...")
    menu(new_player)





################################################################################################################################################################################################################





#esta funcion le pregunta al jugador si quiere reiniciar o si quiere salir del juego
#si quiere reiniciar llamamos a la funcion reiniciar
#si quiere salir cerramos la aplicacion
def menu_lose_win(player:Player):
    while True:
        print("1.Reiniciar\n")
        print("2.Salir\n")
        option = int(input("Elija una opción: "))
        if option == 1:
            restart(player)
        elif option == 2:
            print("\nSaliendo del juego...")
            exit()
        else:
            print("\nOpción incorrecta.\n")



################################################################################################################################################################################################################





#validar jugador es una funcion que nos va a servir para saber si un jugador no puede seguir jugando
#un jugador no puede seguir jugando si si salud llega a cero, no tiene oro para comprar salud, y no tiene xp para cambiar por oro
#en caso de que un jugador no pueda seguir jugando se llama a un menu_lose_win
#si el jugador si puede seguir jugando la funcion devuelve false
#el false puede llegar a confundir un poco, porque devuelve false ? xq la funcion valida si un jugador NO puede seguir jugando
#entonces si: false (jugador NO puede seguir jugando) == puede seguir jugando
def validate_player(player:Player):
    if player.get_health() <= 0 and player.get_xp() < 50 and player.get_gold() < 10:
        print("\nGAME OVER\n")
        menu_lose_win(player)
    else:
        return False
        



################################################################################################################################################################################################################





#la funcion menu va a recibir por parametro un jugador
#se muestran las opciones y dependiendo lo que el jugador elija se llama a la funciones correspondientes
def menu(player:Player):
    while True:
        print("\n----------------------Menú----------------------\n")
        print("1.Ir a la tienda\n")
        print("2.Ir a la arena\n")
        print("3.Ver datos del jugador\n")
        print("4.Empezar de nuevo\n")
        print("5.Salir\n")
        try:
            option = int(input("Elija una opción: "))
        
            if option == 1:
                menu_store(player)
            elif option == 2:
                go_cave(player)
            elif option == 3:
                show_player(player)
            elif option == 4:
                #otra forma de hacer esto es simplemente llamar al loguin, la diferencia es que el jugador actual no se elimina, sigue existiendo
                restart(player)
            elif option == 5:
                print("\nSaliendo del juego...")
                exit()
            else:
                print("\nOpción incorrecta.")
        except ValueError: print("\nOpción incorrecta")

################################################################################################################################################################################################################


#Esta funcion es la que se va a ejecutar al iniciar el juego
#se pide un nombre y se crea un jugador nuevo a partir de ese nombre, luego se llama al menu y se le pasa por parametro el jugador
def loguin():
    print("\nBienvenido a programadores VS reclutadores\n")
    name = input("Ingrese su nombre: ")
    player = Player(name, weapons[0])
    menu(player)
