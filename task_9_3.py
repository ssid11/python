class Woker:


    def __init__(self, name="",surname="", position="", income={"wage":0,"bonus":0}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Woker):


    def get_full_Name(self):
        return f"{self.surname} {self.name}"

    def get_total_income(self):
        return sum([self._income[key] for key in self._income])


w = Position("Zen","Zenov", income={"wage":10000,"bonus":5000})
print(w.get_full_Name())
print(w.get_total_income())
w.surname = "Roshkin"
print(w.get_full_Name())