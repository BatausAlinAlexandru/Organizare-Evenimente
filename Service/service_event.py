from Objects.Entities.event import Events
from Objects.Validators.validator_event import ValidatorEvent

from Repository.json_repository import JsonRepository


class ServiceEvent:
    def __init__(self, repo: JsonRepository, validate_event: ValidatorEvent):
        self.repo = repo
        self.validate = validate_event

    def get_all(self):
        return self.repo.read()

    def add_event(self, the_id, the_date, the_time, the_desc):
        try:
            event = Events(the_id, the_date, the_time, the_desc)
            self.validate.full_validation(event)
            self.repo.create(event)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def modify_event(self, the_id, new_date, new_time, new_desc):
        vector = self.get_all()
        for i in vector:
            if i.get_id() == the_id:
                i.set_date(new_date)
                i.set_time(new_time)
                i.set_desc(new_desc)
                self.validate.full_validation(i)  # Try to validate, if problems this is
                self.repo.update(i)

    def delete_event_id(self, the_id):
        vector = self.get_all()
        deleted = 0
        for i in vector:
            if i.get_id_entity() == the_id:
                self.repo.delete(the_id)
                deleted = 1

        if not deleted:
            raise ValueError("ID was not found")

    def search_event_by_id(self, the_id):
        vector = self.get_all()
        for i in vector:
            if i.get_id_entity() == the_id:
                return i

    def search_event_by_date(self, the_date):
        return_vec = []
        vector = self.get_all()
        for i in vector:
            if i.get_date() == the_date:
                return_vec.append(i)
        return return_vec

    def search_event_by_time(self, the_time):
        return_vec = []
        vector = self.get_all()
        for i in vector:
            if i.get_time() == the_time:
                return_vec.append(i)
        return return_vec
