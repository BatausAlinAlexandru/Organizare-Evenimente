from Repository.json_repository import JsonRepository

from Service.service_person import PersonService
from Service.service_event import ServiceEvent

from Objects.Validators.validator_person import Validatorperson
from Objects.Validators.validator_event import ValidatorEvent

from Objects.Entities.person import Person


def test_person():
    repo = JsonRepository("./Tests/Test_Person.json")
    person_validator = Validatorperson()
    person_service = PersonService(repo, person_validator)
    #  Stergem tot
    for i in person_service.get_all():
        repo.delete(i.get_id_entity())

    assert person_service.get_all() == []
    person_service.add_person('1', 'Bataus Alin-Alexandru', 'bataus.alin.alexandru@anubis.ro')
    assert person_service.get_all()[0].get_id_entity() == '1'
    assert person_service.get_all()[0].get_name() == "Bataus Alin-Alexandru"
    assert person_service.get_all()[0].get_email() == 'bataus.alin.alexandru@anubis.ro'


def test_event():
    repo = JsonRepository("./Tests/Test_Person.json")
    event_validator = ValidatorEvent()
    event_service = ServiceEvent(repo, event_validator)

    #  Stergem tot
    for i in event_service.get_all():
        repo.delete(i.get_id_entity())
    assert event_service.get_all() == []

    event_service.add_event('1', '17-12-2022', '15:22', 'Ceva')

    assert event_service.get_all()[0].get_id_entity() == '1'
    assert event_service.get_all()[0].get_date() == "17-12-2022"
    assert event_service.get_all()[0].get_time() == '15:22'


def test_repo():
    repo = JsonRepository("./Tests/Test_Person.json")

    #  Sterge tot
    for i in repo.read():
        repo.delete(i.get_id_entity())

    repo.create(Person('1', 'Bataus Alin-Alexandru', 'bataus.alin.alexandru@anubis.ro'))

    assert repo.read()[0].get_id_entity() == '1'
    repo.create(Person('2', 'Testing', 'lucas.hood@gmail.com'))
    assert repo.read()[1].get_id_entity() == '2'
    assert repo.read()[1].get_name() == 'Testing'


#  Las asta aici
test_person()
test_event()
test_repo()
