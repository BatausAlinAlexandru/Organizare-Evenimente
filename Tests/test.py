from Objects.Entities.person import Person
from Objects.Entities.event import Events
from Objects.Entities.activity import Activity


def test():
    p = Person('1', 'Bataus Alin-Alexandru', 'bataus.alin.alexandru@anubis.ro')
    assert p.get_name() == 'Bataus Alin-Alexandru'
    assert p.get_email() == 'bataus.alin.alexandru@anubis.ro'
    assert p.get_id_entity() == '1'

    e = Events('1', '11-05-2002', '15:42', 'Hackathon')
    assert e.get_id_entity() == '1'
    assert e.get_date() == '11-05-2002'
    assert e.get_time() == '15:42'
    assert e.get_desc() == 'Hackathon'

    a = Activity('1', 'Bataus Alin-Alexandru', 'bataus.alin.alexandru@anubis.ro', '17-05-2002', '23:59', 'BORN')
    assert a.get_id_entity() == '1'
    assert a.get_name() == 'Bataus Alin-Alexandru'
    assert a.get_email() == 'bataus.alin.alexandru@anubis.ro'
    assert a.get_date() == '17-05-2002'
    assert a.get_desc() == 'BORN'


test()
