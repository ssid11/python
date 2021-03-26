from datetime import datetime
class Date:

    def __init__(self,new_date):
        self.date = new_date.strip().split(sep="-")

    @classmethod
    def c_method(cls):
        return (int(datetime.now().day), int(datetime.now().month), int(datetime.now().year))

    @staticmethod
    def is_valid_date(*args):
        d, m, y = args
        return d in range(1,32)  and m in range(1,13) and isinstance(y,int)


d= Date("11-11-2021")
print(d.c_method())

