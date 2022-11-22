from Objects.Entities.event import Events
import datetime


class ValidatorEvent:
    """ Validator class for event. """

    def date_validation(self, date):
        """ Date validation for event class. """
        try:
            dateformat = "%d-%m-%Y"
            datetime.datetime.strptime(date, dateformat)
        except ValueError:
            raise ValueError("Incorrect time format, should be DD-MM-YYY.")

    def time_validation(self, time):
        """ Time validation for event class. """
        try:
            time_format = "%H:%M"
            datetime.datetime.strptime(time, time_format)
        except ValueError:
            raise ValueError("Incorrect time format, should be HH:MM.")

    def validate(self, event: Events):
        list_of_error_messages = []

        if event.get_date() == '':
            list_of_error_messages.append("The date cannot be empty")

        date = event.get_date().split('/')
        for i in date:
            if not i.isdigit():
                list_of_error_messages.append('The date has letters.')

        if event.get_time() == '':
            list_of_error_messages.append("The time cannot be empty")

        time_split = event.get_time().split(":")
        for i in time_split:
            if not i.isdigit():
                list_of_error_messages.append("The time has letters")

        if list_of_error_messages:
            raise ValueError(list_of_error_messages)

    def full_validation(self, event: Events):
        """ Full validation for event class (time & date) """
        list_of_error_messages = []

        if event.get_id_entity() == '':
            list_of_error_messages.append("Id is null.")

        try:
            dateformat = "%d-%m-%Y"
            datetime.datetime.strptime(event.get_date(), dateformat)
        except ValueError:
            list_of_error_messages.append("Incorrect time format, should be DD-MM-YYY.")

        try:
            timeformat = "%H:%M"
            datetime.datetime.strptime(event.get_time(), timeformat)
        except ValueError:
            list_of_error_messages.append("Incorrect time format, should be HH:MM.")

        if list_of_error_messages:
            raise ValueError(list_of_error_messages)
