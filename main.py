class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        self._type = "Unknown"
        self.__secret = "12345"


    def get_info(self):
        return f"Brand: {self.brand}, Type: {self._type}"

    def __secret_info(self):
        return f"Secret Code: {self.__secret}"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand)
        self._type = "Car"
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()}, Doors: {self.doors}"

class Motorcycle(Vehicle):
    def __init__(self, brand, has_sidecar):
        super().__init__(brand)
        self._type = "Motorcycle"
        self.has_sidecar = has_sidecar

    def get_info(self):
        sidecar_info = "with sidecar" if self.has_sidecar else "no sidecar"
        return f"{super().get_info()}, {sidecar_info}"

car = Car("McLaren", 2)
motorcycle = Motorcycle("Honda", False)

print(car.get_info())
print(motorcycle.get_info())