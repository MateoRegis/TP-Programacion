
class Weapon:

    def __init__(self, name:str, power:int, price:int) -> None:
        self.__name = name
        self.__power = power
        self.__price = price


    def get_price(self)->int:
        return self.__price
    
    def get_power(self):
        return self.__power
    
    def __str__(self):
        return f"{self.__name}\nPoder: {self.__power}\nPrecio: {self.__price}\n"

