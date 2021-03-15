import datetime

class TrafficLigth():
    __red_time = 7
    __yellow_time = 2


    def __init__(self, green_time=7):
        self.__green_time = green_time
        self.__running = False
        self.__period = sum([TrafficLigth.__red_time, TrafficLigth.__yellow_time+2,self.__green_time])



    def running(self):
        self.__running = True
        self.__start_on = datetime.datetime.now()
        self.__revolver()


    def get_color(self):
        if self.__running:
            delta = (datetime.datetime.now() - self.__start_on).seconds % self.__period
            if 0 <= delta <= 6:
                return "Red"
            elif 7 <= delta <= 8:
                return "Yellow"
            elif 9 <= delta <= 9+self.__green_time-1:
                return "Green"
            else:
                return "Yellow"
        else:
            return None


    def __revolver(self):
        beg_time = datetime.datetime.now()
        while True:
            if (datetime.datetime.now() - beg_time).seconds > 6:
                beg_time = datetime.datetime.now()


a = TrafficLigth(10)
