from abc import ABC, abstractmethod
from math import pi, sqrt

class Figure(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Figure):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        area = pi * self.radius ** 2
        return area

class Triangle(Figure):
    def __init__(self, side1: float, side2: float, side3: float):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calculate_area(self) -> float:
        part_perimeter = (self.side1 + self.side2 + self.side3) / 2
        area = sqrt(part_perimeter *
                            (part_perimeter - self.side1) *
                            (part_perimeter - self.side2) *
                            (part_perimeter - self.side3))
        return area

    def is_rectangular(self) -> bool:
        sides = sorted([self.side1, self.side2, self.side3])
        return abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < 1e-6