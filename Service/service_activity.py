from Objects.Entities.activity import Activity
# from Objects.Validators.validator_person import Validatorperson
from Repository.json_repository import JsonRepository
from Service.service_person import PersonService
from Service.service_event import ServiceEvent


class ActivityService:
    def __init__(self, repo: JsonRepository, service_person: PersonService, service_event: ServiceEvent):
        self.repo = repo
        self.service_person = service_person
        self.service_event = service_event

    def get_all_activities(self):
        return self.repo.read()

    def get_all_persons(self):
        return self.service_person.get_all()

    def get_all_events(self):
        return self.service_event.get_all()

    def add_activity_id_person_id_event(self, id_activity, id_person, id_event):
        person = None
        event = None
        persons = self.get_all_persons()
        events = self.get_all_events()

        for i in persons:
            if i.get_id_entity() == id_person:
                person = i
        for i in events:
            if i.get_id_entity() == id_event:
                event = i

        try:
            add = Activity(id_activity, person.get_name(), person.get_email(), event.get_date(), event.get_time(),
                           event.get_desc())
            self.repo.create(add)
            print(add)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def delete_activity(self, id_activity):
        vector = self.get_all_activities()
        deleted = 0
        for i in vector:
            if i.get_id_entity() == id_activity:
                self.repo.delete(id_activity)
                deleted = 1
        if not deleted:
            raise KeyError("ID was not found")

