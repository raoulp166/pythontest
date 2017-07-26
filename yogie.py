from sporter import Sporter

class Yogie(Sporter):
    def __init__(self, real_name, yogy_name, member_number, friskyness=100):
        super().__init__(name=real_name, member_number=member_number)
        self.friskyness = friskyness
        self.yogy_name = yogy_name

    def get_friskyness(self):
        return self.friskyness

    def get_yogy_name(self):
        return self.yogy_name