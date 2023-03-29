"""
Написать программу телефонная книга используя классы.
Написать класс телефонной книги, который хранит список контактов.
Он должен иметь возможность искать контакты по имени и по телефону
(два разных метода), добавлять новые контакты и удалять контакты по имени или телефону.
Контакты реализовать в виде объектов класса Контакт. Данные телефонной книги хранить в json файле.
"""

import json


class Contact:
    def __init__(self, name: str, phone: str) -> None:
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

    def __repr__(self):
        return f"Contact({self.name}, {self.phone})"


class PhoneBook:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        with open(file_name) as file:
            list_of_dicts = json.load(file)
            self.contacts: list[Contact] = [
                Contact(**contact_dict) for contact_dict in list_of_dicts
            ]
            # Contact(name=contact_dict['name'], phone=contact_dict['phone'])

    def find_by_name(self, name: str) -> Contact | None:
        for contact in self.contacts:
            if contact.name == name:
                return contact

    def find_by_phone(self, phone: str) -> Contact | None:
        for contact in self.contacts:
            if contact.phone == phone:
                return contact

    # self.contacts = [Contact('Ivan', '+2..'), ...]
    # add_contact(Contact('Ivan', '+3..'))
    def add_contact(self, contact: Contact) -> Contact | None:
        if not self.find_by_name(contact.name) or not self.find_by_phone(contact.phone):
            self.contacts.append(contact)
            return Contact

    def _delete_contact(self, contact: Contact | None) -> Contact | None:
        if contact is not None:
            self.contacts.remove(contact)
            return contact

    def delete_by_name(self, name: str) -> Contact | None:
        contact = self.find_by_name(name)
        return self._delete_contact(contact)

    def delete_by_phone(self, phone: str) -> Contact | None:
        contact = self.find_by_phone(phone)
        return self._delete_contact(contact)

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            # contacts_list_of_dicts: list[dict] = [
            #     vars(contact) for contact in self.contacts
            # ]
            json.dump(self.contacts, file, indent=4, default=vars)


my_phone_book = PhoneBook("my_phone_book.json")
contacts = [
    Contact("Joe", "+375000000000"),
    Contact("Ann", "+375000000001"),
    Contact("Jack", "+375000000002"),
    Contact("Nick", "+375000000003"),
    Contact("Dan", "+375000000004"),
    Contact("Dan", "+375000000004"),
]
for contact in contacts:
    added_contact = my_phone_book.add_contact(contact)
    print(f"{contact} is added") if added_contact else print(f"{contact} is already in the book")
#
#
phones = ["+375000000002", "000"]
for phone in phones:
    contact = my_phone_book.find_by_phone(phone)
    if contact is not None:
        print(f"found by phone {contact}")
    else:
        print(f"{phone} not found")

    contact = my_phone_book.delete_by_phone(phone)
    if contact is not None:
        print(f"deleted by phone: {contact}")
    else:
        print(f"{phone} not found")
#
#
names = ["Dan", "Egor"]
for name in names:
    contact = my_phone_book.find_by_name(name)
    if contact is not None:
        print(f"found by name {contact}")
    else:
        print(f"{name} not found")

    contact = my_phone_book.delete_by_name(name)
    if contact is not None:
        print(f"deleted by name: {contact}")
    else:
        print(f"{name} not found")

print(my_phone_book.contacts)
my_phone_book.save_to_file()


contact = Contact("Ann", "+375000000001")
print(vars(contact))
print(contact.__dict__)

