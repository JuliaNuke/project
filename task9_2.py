class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calc_mass(self, thikness):
        return self._length * self._width * 25 * thikness

road = Road(100,4)
print(f"Масса асфальта для дорого толщиной 5 см {road.calc_mass(5)} кг")