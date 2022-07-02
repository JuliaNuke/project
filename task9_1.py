from time import sleep

class TrafficLight:
    def __init__(self):
        self.__color = 'red'
    def running(self):
        print(self.__color)
        if self.__color == 'red':
            sleep(7)
            self.__color = 'yellow'
            print(self.__color)
        if self.__color == 'yellow':
            sleep(2)
            self.__color = 'green'
            print(self.__color)
        if self.__color == 'green':
            sleep(1)
            self.__color = 'red'

tl = TrafficLight()
tl.running()