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

    def __init__(self, brand, age, mark, max_load, color=None, weight=None):
        self.max_load = max_load
        super().__init__(brand, age, mark, color, weight)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color=None, weight=None):
        self.max_speed = max_speed
        super().__init__(brand, age, mark, color, weight)

    def move(self):
        super().move()
        print(f'{self.brand}{self.mark} max speed is {self.max_speed}')


truck1 = Truck('MACK', 10, 'rw', 500)
truck2 = Truck('Mercedes-Benz', 5, 'Flat Bed Trailer', 1000)
truck1.move()
truck2.move()
truck1.load()
truck2.load()
print(truck1.max_load)
print(truck2.max_load)
car1 = Car('BMW', 7, 'x5', 260)
car2 = Car('Porsche', 1, '911 Turbo S', 330)
car1.move()
car2.move()

print('hw_10_task_3*')


class Contact:

    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.name}: {self.phone}'

    def __repr__(self):
        return f'Contact({self.name}, {self.phone})'


class PhoneBook:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        with open(file_name) as f:
            list_of_dict = json.load(f)
            self.contacts: list[Contact] = [
                Contact(**contact_dict) for contact_dict in list_of_dict
            ]

    def search_cont_name(self, name: str) -> Contact | None:
        for cont in self.contacts:
            if cont.name == name:
                return cont

    def search_cont_phone(self, phone: str) -> Contact | None:
        for cont in self.contacts:
            if cont.name == phone:
                return cont

    def load_contacts(self, cont: Contact) -> Contact | None:
        if not self.search_cont_phone(cont.name) or not self.search_cont_phone(cont.phone):
            self.contacts.append(cont)
            return cont

    def remove_contacts(self, cont: Contact) -> Contact | None:
        if cont is not None:
            self.contacts.remove(cont)
            return cont

    def remove_cont_name(self, name: str) -> Contact | None:
        cont = self.search_cont_name(name)
        return self.remove_contacts(cont)

    def remove_cont_phone(self, phone: str) -> Contact | None:
        cont = self.search_cont_phone(phone)
        return self.remove_contacts(cont)

    def save_contacts_file(self):
        with open(self.file_name, 'w') as f:
            json.dump(self.contacts, f, indent=4, default=vars)


my_contacts = PhoneBook("my_contacts.json")
contacts = [
    Contact("A", "+1111111"),
    Contact("B", "+2222222"),
    Contact("C", "+3333333"),
    Contact("E", "+4444444"),
    Contact("E", "+4444444"),
    ]
for cont in contacts:
    load_cont = my_contacts.load_contacts(cont)
    print(f'{cont} is added') if load_cont else print(f'{cont} is already in my_contacts')


phones = ["+1111111", "+6666666"]
for phone in phones:
    cont = my_contacts.search_cont_phone(phone)
    if cont is not None:
        print(f'search phone is {cont}')
    else:
        print(f'{phone} not found')


names = ["T", "A"]
for name in names:
    cont = my_contacts.search_cont_name(name)
    if cont is not None:
        print(f'search phone is {cont}')
    else:
        print(f'{name} not found')


print(my_contacts.contacts)
my_contacts.save_contacts_file()


cont = Contact("B", "+2222222")
print(vars(cont))
print(cont.__dict__)
