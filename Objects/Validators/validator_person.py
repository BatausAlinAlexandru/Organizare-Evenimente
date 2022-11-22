from Objects.Entities.person import Person
import re  # this is regex


class Validatorperson:
    def name_validation(self, name):
        """ Name validation. """
        list_of_error_messages = []
        if name == '':
            list_of_error_messages.append("The name cannot be empty")

        for iterator in name:
            if iterator.isdigit():
                list_of_error_messages.append("The name has digits")
                break  # It helps stop the search if we find a digit in the name
        if list_of_error_messages:
            raise ValueError(list_of_error_messages)

    def email_validation(self, email):
        """ Email validation. """
        email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.fullmatch(email_format, email):
            raise ValueError("Email is not valid.")

    def full_validate(self, person: Person):
        """Full validation (ID & NAME & EMAIL). """
        list_of_error_messages = []
        email_format = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if person.get_id_entity() == '':
            list_of_error_messages.append("Id is null.")

        if person.get_name() == '':
            list_of_error_messages.append("The name cannot be empty")

        for iterator in person.get_name():
            if iterator.isdigit():
                list_of_error_messages.append("The name has digits")
                break  # It helps stop the search if we find a digit in the name

        if not re.fullmatch(email_format, person.get_email()):
            list_of_error_messages.append("Email is not valid.")

        if list_of_error_messages:
            raise ValueError(list_of_error_messages)
