from Objects.Entities.entity import Entity

from dataclasses import dataclass


@dataclass
class Events(Entity):
    """ Event class. """
    the_date: str
    time: str
    desc: str

    def get_id_entity(self):
        return self.id_entity

    def get_date(self):
        return self.the_date

    def get_time(self):
        return self.time

    def get_desc(self):
        return self.desc

    def set_date(self, value: str):
        self.the_date = value

    def set_time(self, value: str):
        self.time = value

    def set_desc(self, value: str):
        self.desc = value

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
        return f"ID: {self.id_entity} {self.space_string(len(self.id_entity))} DATE: {self.the_date} \
        {self.space_string(len(self.the_date))} TIME: {self.time} {self.space_string(len(self.time))} DESC: {self.desc}"
