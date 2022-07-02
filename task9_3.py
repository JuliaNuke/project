class Worker:
    def __init__(self, wage, bonus):
        self.name = ''
        self.surname = ''
        self.position = ''
        self._income = {'wage':wage, 'bonus':bonus}

class Position(Worker):
    def __init__(self, wage, bonus):
        super().__init__(wage, bonus)
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


pos = Position(20,80)
pos.name = 'Ivan'
pos.surname  = 'Karman'

print(pos.get_full_name())
print(pos.get_total_income())