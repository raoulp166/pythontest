from datetime import date, timedelta

class Sporter:
    # constructor
    def __init__(self, name, member_number):
        self.name = name
        self.member_number = member_number
        self.date_of_birth = None
        self.gender = None
        self.fitness = 4

        print('creating sporter {} with id {}'.format(self.name,
                                                      self.member_number))
    # setter
    def set_gender(self, gender_value):
        # test if valid
        if gender_value >= 0 and gender_value <= 10:
            self.gender = gender_value
        else:
            raise Exception("{} is an invalide gender value".format(gender_value))

    # getter
    def get_gender(self):
        return self.gender

    # setter
    def set_date_of_birth(self, year, month, day):
        # use date
        pass

    def get_age(self):
        # use timedelta
        pass