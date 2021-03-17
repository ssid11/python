class Road:

    __cover_mass = 25


    def __init__(self, width=0, length=0):
        self._width = width
        self._length = length


    def calc_cover(self,higth=0):
        return self._width * self._length * higth * Road.__cover_mass

a = Road()
b = Road(20,5000)
