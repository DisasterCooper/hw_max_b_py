import time


class Auto:
    def __init__(self, brand: str, age: int, mark: str, color: str | None = None, weight: int | None = None) -> None:
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):
    def __init__(
            self,
            brand: str,
            age: int,
            mark: str,
            max_load: int,
            color: str | None = None,
            weight: int | None = None,
    ):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("load")
        time.sleep(1)


class Car(Auto):
    def __init__(
            self,
            brand: str,
            age: int,
            mark: str,
            max_speed: int,
            color: str | None = None,
            weight: int | None = None,
    ):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")


mack_truck = Truck("MACK", 10, "GRANITE", 42000, "black", 10000)
kenworth_truck = Truck("KENWORTH", 5, "W990", 108000, "silver", 1200)

print(f"{mack_truck.brand=}, {mack_truck.age=}, {mack_truck.mark=}, "
      f"{mack_truck.max_load=}, {mack_truck.weight=}, {mack_truck.color=}")
mack_truck.birthday()
print(f"{mack_truck.age=}")
mack_truck.move()
mack_truck.stop()
mack_truck.load()

print(f"{kenworth_truck.brand=}, {kenworth_truck.age=}, {kenworth_truck.mark}, "
      f"{kenworth_truck.max_load}, {kenworth_truck.weight}, {kenworth_truck.color}")
kenworth_truck.birthday()
print(f"{kenworth_truck.age=}")
kenworth_truck.move()
kenworth_truck.stop()
kenworth_truck.load()

toyota_car = Car("Toyota", 2, "Corolla", 188, "white")
kia_car = Car("Kia", 7, "Rio", 173, "grey")

print(f"{toyota_car.brand=}, {toyota_car.age=}, {toyota_car.mark}, "
      f"{toyota_car.max_speed}, {toyota_car.weight}, {toyota_car.color}")
toyota_car.birthday()
print(f"{toyota_car.age=}")
toyota_car.move()
toyota_car.stop()

print(f"{kia_car.brand=}, {kia_car.age=}, {kia_car.mark}, "
      f"{kia_car.max_speed}, {kia_car.weight}, {kia_car.color}")
kia_car.birthday()
print(f"{kia_car.age=}")
kia_car.move()
kia_car.stop()

