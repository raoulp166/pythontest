from sporter import Sporter
from yogie import Yogie
from datetime import datetime

class FitnessSchool:
    def __init__(self, name):
        self.name = name
        self.latest_member_number = 0
        self.sporters = []
        self.sporter_types = ("yogie", "bodybuilder", "flex", "spin")

    def run(self):
        print("creating John")
        member_id = 0
        john = Sporter("John", member_id)
        self.sporters.append(john)
        member_id += 1
        print("creating Jenny")
        jenny = Sporter("Jenny", member_id)
        self.sporters.append(jenny)
        jenny.set_gender(3)


    def register(self):
        name = input("Wat is je naam?: ")
        gender_value = input("Hoe scoren je vrienden jou op de schaal van gender identifiction? "
                             " tussen 0-10 (vrouwelijk - mannelijk)"
                             )

        known_sport_type = False
        sport_type = None
        while not known_sport_type:
            print("Wat wens je voor sporttype?")
            for type in self.sporter_types:
                print("* {}".format(type))
            sport_type = input()

            if sport_type.lower() in self.sporter_types:
                known_sport_type = True

        # verder uitwerken
        if sport_type == "yogie":
            yogie_name = input("Wat is je yogie-naam?")
            yogie = Yogie(name, yogie_name, self.latest_member_number)
        self.sporters.append(yogie)
        self.latest_member_number += 1

    def enter(self, member_id):
        now = datetime.now()
        pass

    def dumpSportersToFile(self, filename):
        # can we write to file?
        nb_sporters = len(self.sporters)
        print("duming {} sporters to file {}".format(nb_sporters, filename))
        sporters_string = ''
        for sporter in self.sporters:
            json_sporter = sporter.toJSON()
            sporters_string += json_sporter

        with open(filename, 'w', encoding="utf-8") as fout:
            fout.write(sporters_string)

