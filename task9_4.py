class Car:
    def __init__(self) -> None:
        self.speed = 0
        self.color = 'transparent'
        self.name = ''
        self.is_police = False
    def go(self, speed):
        self.speed = speed
    def stop(self):
        self.speed = 0
    def turn(direction):
        print(f'Turn {direction}')
    def show_speed(self):
        pass

class TownCar(Car):
    def __init__(self) -> None:
        super().__init__()
        self.color = 'White'
        self.name = 'Town car'
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")

class WorkCar(Car):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Work Car'
        self.color = 'Sandy'
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")

class SportCar(Car):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Sport Car'
        self.color = 'Red'

class PoliceCar(Car):
    def __init__(self) -> None:
        super().__init__()
        self.name = 'Police Car'
        self.color = 'Gray'
        self.is_police = True

town = TownCar()
town.go(100)
print(f'Машина {town.name} цвета {town.color}.')
town.show_speed()

work = WorkCar()
work.go(100)
print(f'Машина {work.name} цвета {work.color}.')
work.show_speed()

sport = SportCar()
sport.go(100)
print(f'Машина {sport.name} цвета {sport.color}.')
sport.show_speed()

police = PoliceCar()
police.go(100)
print(f'Машина {police.is_police} {police.name} цвета {police.color}.')
police.show_speed()