from Objects.Entities.entity import Entity

from dataclasses import dataclass


@dataclass
class Person(Entity):
    """ Person class. """
    name: str
    email: str

    def get_id_entity(self):
        return self.id_entity

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_name(self, value: str):
        self.name = value

    def set_email(self, value: str):
        self.email = value

    def space(self, lenght):
        string = "               "
        for i in range(lenght):
            string = string - " "

    def space_string(self, lenght):
        vec = []
        for i in range(50):
            vec += " "
        for i in range(lenght):
            vec.pop()

        string = ""
        for i in vec:
            string += i
        return string

    def __str__(self):
        return f"ID: {self.id_entity} {self.space_string(len(self.id_entity))} NUME: {self.name} \
        {self.space_string(len(self.name))} EMAIL: {self.email}"
