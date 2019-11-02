# Создать иерархию наследования классов: место (локация), город, область, мегаполис


class Place:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coordinates(self):
        return f'{self.x}, {self.y}'


class City(Place):

    def __init__(self, x, y, name):
        super().__init__(x, y)
        self.name = name

    @property
    def coordinates(self):
        return f'{self.x}, {self.y}'

class Region(Place):

    def __init__(self, x, y, name, cities):
        super().__init__(x, y)
        self.name = name
        self.cities = cities

    def get_cities(self):
        c = ', '.join(self.cities)
        return f'Region: {self.name}. Cities: {c}'

    @property
    def coordinates(self):
        return f'{self.x}, {self.y}'


class Metropolis(City):

    def __init__(self, x, y, name, subway_stations):
        super().__init__(x, y, name)
        self.subway_stations = subway_stations

    def get_stations(self):
        c = ', '.join(self.subway_stations)
        return f'Metropolis: {self.name}. Subway stations: {c}'

    @property
    def coordinates(self):
        return f'{self.x}, {self.y}'