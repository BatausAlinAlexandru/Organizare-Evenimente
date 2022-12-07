from Repository.json_repository import JsonRepository
from operator import getitem


class ServiceRaports:
    def __init__(self, event_repo: JsonRepository, person_repo: JsonRepository, activities_repo: JsonRepository):
        self.event_repo = event_repo
        self.person_repo = person_repo
        self.activities_repo = activities_repo

    def get_events(self):
        return self.event_repo.read()

    def get_persons(self):
        return self.person_repo.read()

    def get_activities(self):
        return self.activities_repo.read()

    def print_list(self, lista):
        for i in lista:
            print(i)

    def lista_evenimente_persoana(self, name_person):
        """ DESCRIERE """

        """ Verificare daca exista mai multe id-uri cu acelasi nume"""
        persoane = self.get_persons()
        count = 0
        for i in persoane:
            if i.get_name() == name_person:
                count += 1
        if count > 1:
            raise KeyError

        lista = []
        activities = self.get_activities()

        for act in activities:
            if act.get_name() == name_person:
                lista.append(act)

        new_list = sorted(lista, key=lambda d: d.get_desc())

        return new_list

    def lista_evenimente_persoana_email(self, the_email):
        lista = []
        activities = self.get_activities()

        for act in activities:
            if act.get_email() == the_email:
                lista.append(act)

        new_list = sorted(lista, key=lambda d: d.get_desc())

        return new_list

    def lista_evenimente_persoana_ordonata_dupa_data(self, name_person):
        persoane = self.get_persons()
        count = 0
        for i in persoane:
            if i.get_name() == name_person:
                count += 1
        if count > 1:
            raise KeyError

        lista = []
        activities = self.get_activities()

        for act in activities:
            if act.get_name() == name_person:
                lista.append(act)

        new_list = sorted(lista, key=lambda d: d.get_date())

        return new_list

    def lista_evenimente_ordonata_dupa_data_email(self, the_email):
        lista = []
        activities = self.get_activities()

        for act in activities:
            if act.get_email() == the_email:
                lista.append(act)

        new_list = sorted(lista, key=lambda d: d.get_date())

        return new_list

    #  persoane participante la cele mai multe evenimente

    def __return_name_by_email(self, the_email):
        persoane = self.get_persons()
        for i in persoane:
            if i.get_email() == the_email:
                return i.get_name()

    def persoane_participante(self):
        activitati = self.get_activities()
        persoanele = {}
        for act in activitati:
            if not act.get_email() in persoanele:
                persoanele[act.get_email()] = 1
            else:
                persoanele[act.get_email()] += 1

        sorted_persoanele = sorted(persoanele.items(), key=lambda d: d[1], reverse=True)
        # print(sorted_persoanele)
        # for i in sorted_persoanele:
        # print(f"{self.__return_name_by_email(i[0])} participa la {i[1]} evenimente.")
        return sorted_persoanele

    def primele_20_la_suta(self):
        activitati = self.get_activities()
        persoanele = {}
        for act in activitati:
            if not act.get_desc() in persoanele:
                persoanele[act.get_desc()] = 1
            else:
                persoanele[act.get_desc()] += 1

        sorted_persoanele = sorted(persoanele.items(), key=lambda d: d[1], reverse=True)
        cati_sa_afiseze = int(0.2 * len(sorted_persoanele))
        new_list = []
        for i in range(cati_sa_afiseze):
            new_list.append(sorted_persoanele[i])
        return new_list
