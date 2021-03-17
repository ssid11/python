class Car:
    speed = 0
    color = None
    name = None
    is_police = None

    def go(self):
        print("Едем")


    def stop(self):
        print("Остановились")

    def turn(self,direction=None):
        print(f"Мы повернули {direction}")

    def show_speed(self):
        print(f"Наша скорость {self.speed}")

class TownCar(Car):


    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f"вы превысили скорость")

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"вы превысили скорость")


class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

c = Car()
t = TownCar()
w = WorkCar()
s = SportCar()
p = PoliceCar()
c.show_speed()
t.show_speed()
w.show_speed()
s.show_speed()
p.show_speed()
w.speed = 80
t.speed = 100
t.show_speed()
w.show_speed()