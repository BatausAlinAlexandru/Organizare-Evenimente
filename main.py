from Repository.json_repository import JsonRepository

from Objects.Validators.validator_event import ValidatorEvent
from Objects.Validators.validator_person import Validatorperson

from Service.raports import ServiceRaports
from Service.service_event import ServiceEvent
from Service.service_person import PersonService
from Service.service_activity import ActivityService

from Console.menu import Menu
from Console.ui_event import EventUI
from Console.ui_person import PersonUI
from Console.ui_raport import RaportUI
from Console.ui_activity import ActivitiesUI

#  Nu este necesar sa folosim ci doar sa importam pentru a rula testele
import Tests.test
import Tests.test_services

# Validations
validate_event = ValidatorEvent()
validate_person = Validatorperson()


# Repo
repo_event = JsonRepository("Events.json")
repo_person = JsonRepository("Persons.json")
repo_activities = JsonRepository("Activities.json")

# Service
service_event = ServiceEvent(repo_event, validate_event)
service_person = PersonService(repo_person, validate_person)
service_raports = ServiceRaports(repo_event, repo_person, repo_activities)
service_activity = ActivityService(repo_activities, service_person, service_event)

# Console
ui_event = EventUI(service_event)
ui_person = PersonUI(service_person)
ui_raports = RaportUI(service_raports)
ui_activities = ActivitiesUI(repo_activities, service_activity)

menu = Menu(ui_person, ui_event, ui_activities, ui_raports)

# RUN MENU
menu.run_ui()
