from math import sqrt as kvadrkoren


class Point:
    """конструктор"""
    def __init__(self, x, y):
        self.x = x
        self.y = y


    """"метод"""
    def dist(self, pp2):
        dx = pp2.x - self.x
        dy = pp2.y - self.y
        return kvadrkoren(dx*dx + dy*dy)

    """операция"""
    def __eq__(self, other):
        return  self.x == other.x and self.y == other.y
