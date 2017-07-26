from sporter import Sporter
from fitness_school import FitnessSchool


if __name__ == '__main__':
    try:
        school = FitnessSchool("Vette workout!")
        school.register()
        #school.run()
        school.dumpSportersToFile("testdump.txt")
        #school.run()
    except Exception as e:
        print("Exception!")
        print(e)
