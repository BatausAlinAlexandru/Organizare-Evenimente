from Console.ui_person import PersonUI
from Console.ui_event import EventUI
from Console.ui_activity import ActivitiesUI

class Menu:

    def __init__(self, menu_person: PersonUI, menu_event: EventUI, menu_activiy: ActivitiesUI):
        self.menu_person = menu_person
        self.menu_event = menu_event
        self.menu_activity = menu_activiy

    def print_menu(self):
        print("""
    1. PERSON
    2. EVENTS
    3. ACTIVITY
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
            elif cmd == 'x':
                break
            else:
                print("Enter a valid command.")
