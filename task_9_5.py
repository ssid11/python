class Stationery:

    title = ""

    def draw(self):
        print(f"Запуск отрисовки»")
        # print(self.title) Не лучше ли сделать так, чем переопределять функцию в дочернем классе?


    def __init__(self,name):
        self.title = name


class Pen(Stationery):


    def draw(self):
        super().draw()
        print(f"Рисую Pen")


class Pencil(Stationery):


    def draw(self):
        super().draw()
        print(f"Рисую Pencil")

class Handle(Stationery):


    def draw(self):
        super().draw()
        print(f"Рисую Handle")
p = Pen("Pen")
p.draw()
pc = Pencil("Pencil")
pc.draw()
h = Handle("Handle")
h.draw()

