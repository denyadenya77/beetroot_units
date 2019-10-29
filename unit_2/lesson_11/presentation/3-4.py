# Создать абстрактный класс Device, создать от него два класса наследника Scanner, Printer.
# Создать класс Copier наследуясь от классов Scanner, Printer.

# В предыдущих родительских и дочерних классах создать методы, которые могут иметь
# общий интерфейс но различную реализацию (полиморфизм)

from abc import ABC, abstractmethod

class Device(ABC):

    def __init__(self, name, paper, copies = 0, cartridge = 100):
        self.name = name
        self.paper = paper
        self.copies = copies
        self.cartridge = cartridge




    @abstractmethod
    def printing(self, pages):
        if self.paper >= pages and self.cartridge >= pages / 2:
            self.paper -= pages
            self.cartridge -= pages / 2
            self.copies += pages
        else:
            return 'Charge up the cartridge of load paper!'


    @abstractmethod
    def cartridge_replacement(self):
        self.cartridge = 100

    @abstractmethod
    def new_paper(self, new_paper):
        self.paper = self.paper + new_paper


class Printer(Device):

    def __init__(self, name, paper, copies = 0, cartridge = 100):
        super().__init__(name, paper, copies, cartridge)

    def printing(self, pages):
        if self.paper >= pages and self.cartridge >= pages / 2:
            self.paper -= pages
            self.cartridge -= pages / 2
            self.copies += pages
        else:
            print('Charge up the cartridge of load paper!')

    def cartridge_replacement(self):
        self.cartridge = 100

    def new_paper(self, new_paper):
        self.paper = self.paper + new_paper

    def __str__(self):
        return f'{self.name}: paper - {self.paper}, copies - {self.copies}, cartridge - {self.cartridge}.'


printer_1 = Printer('Epson', 60)
print(printer_1)
printer_1.printing(50)
print(printer_1)


class Scanner(Device):

    def __init__(self, name, paper, copies = 0, cartridge = 100, scanns = 0):
        super().__init__(name, paper, copies, cartridge)
        self.scanns = scanns

    def scanning(self):
        self.scanns += 1
        print('Scanning is successfully completed!')


class Copier(Printer, Scanner):

    def __init__(self, name, paper, copies = 0, cartridge = 100, scanns = 0):
        super().__init__(name, paper, copies, cartridge, scanns)

    def printing(self, pages):
        if self.paper >= pages and self.cartridge >= pages / 2:
            self.paper -= pages
            self.cartridge -= pages / 2
            self.copies += pages
        else:
            print('Charge up the cartridge of load paper!')

    def cartridge_replacement(self):
        self.cartridge = 100

    def new_paper(self, new_paper):
        self.paper = self.paper + new_paper

    def scanning(self):
        self.scanns += 1
        print('Scanning is successfully completed!')

    def __str__(self):
        return f'{self.name}: paper - {self.paper}, copies - {self.copies}, scanns - {self.scanns}, cartridge - {self.cartridge}.'