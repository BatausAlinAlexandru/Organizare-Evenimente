from Objects.Entities.person import Person
from Objects.Validators.validator_person import Validatorperson

from Repository.json_repository import JsonRepository

import uuid  # Random ID


class PersonService:
    def __init__(self, repo: JsonRepository, validate_person: Validatorperson):
        self.repo = repo
        self.validate_person = validate_person

    def get_all(self):
        return self.repo.read()

    def add_person(self, the_id, the_name, email):
        try:
            person = Person(the_id, the_name, email)
            self.validate_person.full_validate(person)
            self.repo.create(person)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modify_person(self, the_id, new_name, new_email):
        vector = self.get_all()
        for i in vector:
            if i.get_id_entity() == the_id:
                i.set_name(new_name)
                i.set_email(new_email)
                self.validate_person.full_validate(i)  # Try to validate, if problems this is
                self.repo.update(i)

    def delete_person(self, the_id):
        """ This function will delete the person from json file with the id specified. """
        vector = self.get_all()
        found = 0
        for i in vector:
            if i.get_id_entity() == the_id:
                self.repo.delete(the_id)
                found = 1

        if not found:
            raise KeyError("ID was not found")

    def search_person_by_id(self, the_id):
        """ Search in json file the entity with the id specified. """
        vector = self.get_all()
        for i in vector:
            if i.get_id_entity() == the_id:
                return i
        return None

    def search_person_by_name(self, the_name):
        """ Search in json file the entity with the name specified. """
        vector = self.get_all()
        for i in vector:
            if i.get_name() == the_name:
                return i
        return None

    def search_person_by_email(self, email):
        """ Search in json file the entity with the email specified. """
        vector = self.get_all()
        for i in vector:
            if i.get_email() == email:
                return i

        return None
