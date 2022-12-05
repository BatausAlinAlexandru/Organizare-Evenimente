from Console.ui_person import PersonUI
from Console.ui_event import EventUI
from Console.ui_activity import ActivitiesUI
from Console.ui_raport import RaportUI


class Menu:

    def __init__(self, menu_person: PersonUI, menu_event: EventUI, menu_activiy: ActivitiesUI, menu_raports: RaportUI):
        self.menu_person = menu_person
        self.menu_event = menu_event
        self.menu_activity = menu_activiy
        self.menu_rapots = menu_raports

    def print_menu(self):
        print("""
    1. PERSON
    2. EVENTS
    3. ACTIVITY
    4. RAPORTS
    x. EXIT
        """)

    def run_ui(self):
        while True:
            self.print_menu()
            cmd = input("Enter a command: ")

            if cmd == '1':
                self.menu_person.run()
            elif cmd == '2':
                self.menu_event.run()
            elif cmd == '3':
                self.menu_activity.run()
            elif cmd == '4':
                self.menu_rapots.run()
            elif cmd == 'x':
                break
            else:
                print("Enter a valid command.")
