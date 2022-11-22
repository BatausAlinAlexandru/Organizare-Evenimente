# Aici o sa punem toate lucrurile din meniu ce tin de persone
from Service.service_person import PersonService

from Objects.Entities.person import Person


class PersonUI:

    def __init__(self, service_person: PersonService):
        self.service_person = service_person

    @classmethod
    def print_info(cls):
        print("""
        1. Add person.
        2. Show persons.
        3. Modify person
        4. Delete person
        5. Search by id
        6. Search by name
        7. Search by email
        X. Exit
        """)

    def __add_person(self):
        try:
            the_id = input("Enter a ID: ")
            the_name = input("Enter a name: ")
            email = input("Enter a email: ")
            self.service_person.add_person(the_id, the_name, email)
        except ValueError as e:
            print(e)

    def __modify_person(self):
        try:
            id_search = input("Enter a id to modify: ")
            new_name = input("Enter a new name to modify the person: ")
            new_email = input("Enter a new email to modify the person: ")
            # TRebuie sa fac o validare aici
            self.service_person.validate_person.full_validate(Person(id_search, new_name, new_email))
            self.service_person.modify_person(id_search, new_name, new_email)
        except ValueError as e:
            print(e)

    def __delete_person(self):
        try:
            the_id = input("Enter a id: ")
            self.service_person.delete_person(the_id)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def search_id(self):
        try:
            the_id = input("Enter a id: ")
            person = self.service_person.search_person_by_id(the_id)
            print(person)
        except ValueError as e:
            print(e)

    def search_the_name(self):
        try:
            the_name = input("Enter a the_named: ")
            person = self.service_person.search_person_by_name(the_name)
            print(person)
        except ValueError as e:
            print(e)

    def search_the_email(self):
        try:
            email = input("Enter a the_named: ")
            person = self.service_person.search_person_by_email(email)
            print(person)
        except ValueError as e:
            print(e)

    def print_list(self, lista):
        for el in lista:
            print(el)

    def print_persons(self):
        self.print_list(self.service_person.get_all())

    def run(self):
        while True:
            self.print_info()

            cmd = input("Enter a command: ")
            if cmd == '1':
                self.__add_person()
            elif cmd == '2':
                self.print_persons()
            elif cmd == '3':
                self.__modify_person()
            elif cmd == '4':
                self.__delete_person()
            elif cmd == '5':
                self.search_id()
            elif cmd == '6':
                self.search_the_name()
            elif cmd == '7':
                self.search_the_email()
            elif cmd == 'x':
                break
            else:
                print("Enter a valid command !")
