from Objects.Entities.entity import Entity
from Objects.Entities.person import Person
from Objects.Entities.event import Events

from dataclasses import dataclass


@dataclass
class Activity(Events, Person):
    def space_string(self, lenght):
        vec = []
        for i in range(38):
            vec += " "
        for i in range(lenght):
            vec.pop()

        string = ""
        for i in vec:
            string += i
        return string

    def __str__(self):
        return f"ID: {self.id_entity} {self.space_string(len(self.id_entity))} " \
               f"NAME: {self.name} {self.space_string(len(self.name))} " \
               f"EMAIL: {self.email} {self.space_string((len(self.email)))} " \
               f"DATE: {self.the_date} \t\t " \
               f"TIME: {self.time} \t\t {self.desc}"
