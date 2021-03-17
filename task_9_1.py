import datetime
from time import sleep

class TrafficLigth:
    __red_time = 7
    __yellow_time = 2
    __color = None


    def __init__(self, green_time=7):
        self.__green_time = green_time
        self.__running = False
        self.__period = sum([TrafficLigth.__red_time, TrafficLigth.__yellow_time,self.__green_time])



    def running(self):
        self.__running = True
        self.__start_on = datetime.datetime.now()


    def get_color(self):
        if self.__running:
            delta = (datetime.datetime.now() - self.__start_on).seconds % self.__period
            if 0 <= delta <= 6:
                return "Red"
            elif 7 <= delta <= 8:
                return "Yellow"
            else:
                return "Green"
        else:
            return None


a = TrafficLigth(7)
print(a.get_color())
a.running()
print(a.get_color())
sleep(7)
print(a.get_color())
sleep(5)
print(a.get_color())

