class Stationery:
    def __init__(self) -> None:
        self.title = ''
    def draw(self):
        pass

class Pen(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "Pen"
    def draw(self):
        print("This is pen")

class Pencil(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "Pencil"
    def draw(self):
        print("this is pencil")

class Handle(Stationery):
    def __init__(self) -> None:
        super().__init__()
        self.title = "Handle"
    def draw(self):
        print("this is Handle")

pen = Pen()
pencil = Pencil() 
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()