import json
import time

print('hw_10_task_1')  # class auto с атрибутами


class Auto:

    def move(self):
        print('The car is moving')

    def stop(self):
        print('The car stopped')

    def birth(self):
        self.age += 1

    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight


auto = Auto('Volvo', 5, 'Xc90', 'black', 2300)
auto.birth()
auto.move()
auto.stop()

print('hw_10_task_2')


class Truck(Auto):

    def move(self):
        print('Attention!')
        super().move()

    def load(self):
        time.sleep(1)
        print('load')
        time.sleep(1)

    def __init__(self, max_load, brand=None, age=None, mark=None):
        self.max_load = max_load
        super().__init__(brand, age, mark)


class Car(Auto):

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move(self):
        super().move()
        print(f'max speed is {self.max_speed}')


truck1 = Truck(500)
truck2 = Truck(1000)
truck1.move()
truck2.move()
truck1.load()
truck2.load()
print(truck1.max_load)
print(truck2.max_load)
car1 = Car(100)
car2 = Car(150)
car1.move()
car2.move()

print('hw_10_task_3*')


class Contact:

    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class PhoneBook:
    def __init__(self, file_name):
        self.file_name = file_name

    def load_contacts(self):
        with open(self.file_name) as f:
            contacts = json.load(f)

    def save_contacts(self):
        with open(self.file_name, 'w') as f:
            json.dump([], f)

    def add_contacts(self, name, phone):
        cont = Contact(name, phone)
        self.load_contacts.append(cont)
        self.save_contacts()

    def search_cont_name(self, name):
        return

    def search_cont_phone(self, phone):
        pass

    def remove_cont_name(self, name):
        pass

    def remove_cont_phone(self, phone):
        pass
