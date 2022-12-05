from Repository.json_repository import JsonRepository
from Service.service_activity import ActivityService


class ActivitiesUI:
    def __init__(self, repo: JsonRepository, activities: ActivityService):
        self.repo = repo
        self.activities = activities

    def print_list(self, lista):
        for el in lista:
            print(el)

    def __add_activities(self):
        try:
            id_activity = input("ID activity: ")
            id_person = input("ID person: ")
            id_event = input("ID event: ")
            self.activities.add_activity_id_person_id_event(id_activity, id_person, id_event)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)
        pass

    def __modify_activity(self):
        pass

    def __delete_activity(self):
        try:
            id_activity = input("ID activity: ")
            self.activities.delete_activity(id_activity)
        except ValueError as e:
            print(e)

    def print_info(self):
        print("""
        1. Add activities [ID PERSON - ID EVENT].
        2. Show activities.
        3. Delete activity
        x. EXIT.
        """)

    def run(self):
        while True:
            self.print_info()
            cmd = input("Enter a command: ")

            if cmd == '1':
                self.__add_activities()
            elif cmd == '2':
                self.print_list(self.activities.get_all_activities())
            elif cmd == '3':
                self.__delete_activity()
            elif cmd == 'x':
                break
            else:
                print("Enter a valid command.")

