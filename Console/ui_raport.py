from Service.raports import ServiceRaports


class RaportUI:
    def __init__(self, service_raports: ServiceRaports):
        self.service_raports = service_raports

    def print_info(self):
        print("""
        1. Afisare evenimente persoana
        2. Persoane care participa la cele mai multe evenimente
        x. EXIT
        """)

    def print_lista(self, lista):
        for i in lista:
            print(i)

    def lista_evenimente_la_care_participa_o_persona(self):
        optiune = input("Dupa ce vreti sa ordonati ? \n1 - Descriere\t2 - Data\nAlegeti optiunea: ")
        if optiune == '1':
            try:
                name = input("Enter the name: ")
                lista = self.service_raports.lista_evenimente_persoana(name)
                self.print_lista(lista)
            except KeyError:
                print("In database exist 2 persons with the same name.")
                email = input("Enter the email:")
                lista = self.service_raports.lista_evenimente_persoana_email(email)
                self.print_lista(lista)
            except ValueError as e:
                print(e)
        else:
            try:
                name = input("Enter the name: ")
                lista = self.service_raports.lista_evenimente_persoana_ordonata_dupa_data(name)
                self.print_lista(lista)
            except KeyError:
                print("In database exist 2 persons with the same name.")
                email = input("Enter the email:")
                lista = self.service_raports.lista_evenimente_ordonata_dupa_data_email(email)
                self.print_lista(lista)
            except ValueError as e:
                print(e)

    def persoane_care_participa_la_cele_mai_multe_evenimente(self):
        self.service_raports.persoane_participante()

        pass

    def run(self):
        while True:
            self.print_info()

            cmd = input("Enter a command: ")

            if cmd == '1':
                self.lista_evenimente_la_care_participa_o_persona()
            elif cmd == '2':
                self.persoane_care_participa_la_cele_mai_multe_evenimente()
            elif cmd == 'x' or cmd == 'X':
                break

            else:
                print("Enter a valid command !!!")
