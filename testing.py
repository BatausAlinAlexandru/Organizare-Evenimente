dictionar = {
    '1': {"nume": "Bataus Alin-Alexandru", "email": "bataus.alin.alexandru@anubis.ro", 'data': 'ceva', 'ora': '11:23'},
    '2': {"nume": "Paven Andrei", "email": "paven.andrei@anubis.ro", 'data': 'ceva', 'ora': '12:23'}
}

new_dict = {}

for i in dictionar:
    if not dictionar[i]['nume'] in new_dict:
        new_dict[dictionar[i]['nume']] = 5
