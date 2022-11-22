from Objects.Validators.validator_person import Validatorperson
from Objects.Validators.validator_event import ValidatorEvent
from Service.service_person import PersonService
from Service.service_event import ServiceEvent
from Service.service_activity import ActivityService
from Repository.json_repository import JsonRepository
from Console.ui_person import PersonUI
from Console.menu import Menu
from Console.ui_event import EventUI
from Console.ui_activity import ActivitiesUI

# Validations
validate_person = Validatorperson()
validate_event = ValidatorEvent()

# Repo
repo_person = JsonRepository("Persons.json")
repo_event = JsonRepository("Events.json")
repo_activities = JsonRepository("Activities.json")

# Service
service_person = PersonService(repo_person, validate_person)
service_event = ServiceEvent(repo_event, validate_event)
service_activity = ActivityService(repo_activities, service_person, service_event)

# Console
ui_activities = ActivitiesUI(repo_activities, service_activity)
ui_person = PersonUI(service_person)
ui_event = EventUI(service_event)
menu = Menu(ui_person, ui_event, ui_activities)

# RUN MENU
menu.run_ui()
