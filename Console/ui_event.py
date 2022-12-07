from Service.service_event import ServiceEvent
# from Objects.Entities.person import Person


class EventUI:
    def __init__(self, service: ServiceEvent):
        self.service = service

    def print_info(self):
        print("""
        1. Add event
        2. Show event
        3. Modify event
        4. Delete event
        5. Search by id
        6. Search by date
        7. Search by time
        X. Exit
        """)

    def print_list(self, lista):
        for el in lista:
            print(el)

    def print_events(self):
        self.print_list(self.service.get_all())

    def __add_event(self):
        try:
            the_id = input("Enter a id: ")
            the_date = input("Enter a date (DD-MM-YYYY): ")
            the_time = input("Enter a time (HH:MM): ")
            the_desc = input("Enter a desc: ")
            self.service.add_event(the_id, the_date, the_time, the_desc)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def __modify_event(self):
        try:
            the_id = input("Enter a id: ")
            new_date = input("Enter a new date (DD-MM-YYYY): ")
            new_time = input("Enter a new time (HH:MM): ")
            new_desc = input("Enter a new desc: ")
            self.service.validate.time_validation(new_time)
            self.service.validate.date_validation(new_date)
            self.service.modify_event(the_id, new_date, new_time, new_desc)
        except ValueError as e:
            print(e)

    def __delete_event(self):
        try:
            the_id = input("Enter a id: ")

            self.service.delete_event_id(the_id)
        except ValueError as e:
            print(e)

    def search_id(self):
        try:
            the_id = input("Enter a id: ")
            event = self.service.search_event_by_id(the_id)
            print(event)
        except ValueError as e:
            print(e)

    def search_date(self):
        try:
            the_date = input("Enter a date (DD-MM-YYYY): ")
            self.service.validate.date_validation(the_date)
            event = self.service.search_event_by_date(the_date)
            self.print_list(event)
        except ValueError as e:
            print(e)

    def search_time(self):
        try:
            time = input("Enter a date (HH:MM): ")
            self.service.validate.time_validation(time)
            event = self.service.search_event_by_time(time)
            self.print_list(event)
        except ValueError as e:
            print(e)

    def run(self):
        while True:
            self.print_info()
            cmd = input("Enter a command: ")
            if cmd == '1':
                self.__add_event()
            elif cmd == '2':
                self.print_events()
            elif cmd == '3':
                self.__modify_event()
            elif cmd == '4':
                self.__delete_event()
            elif cmd == '5':
                self.search_id()
            elif cmd == '6':
                self.search_date()
            elif cmd == '7':
                self.search_time()
            elif cmd == 'x':
                break
            else:
                print("Enter a valid command !")
