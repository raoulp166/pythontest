from sporter import Sporter

def run_school():
    member_id = 0
    john = Sporter("John", member_id)
    member_id +=1
    jenny = Sporter("Jenny", member_id)
    jenny.set_gender(3)


if __name__ == '__main__':
    try:
        run_school()
    except Exception as e:
        print("Exception!")
        print(e)
