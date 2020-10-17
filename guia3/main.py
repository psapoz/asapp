import math


class Point:
    __quadrants = {
        1: 'cuadrante 1',
        2: 'cuadrante 2',
        3: 'cuadrante 3',
        4: 'cuadrante 4',
        (True, False): 'eje x',
        (False, True): 'eje y',
        (False, False): 'origen'
    }

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.x, self.y}'

    def quadrant(self):
        if self.x > 0:
            if self.y > 0:
                return self.__quadrants[1]
            else:
                return self.__quadrants[4]
        elif self.x < 0:
            if self.y > 0:
                return self.__quadrants[2]
            else:
                return self.__quadrants[3]
        else:
            return self.__quadrants[bool(self.x), bool(self.y)]


class Vector:
    def __init__(self, point_1: Point, point_2: Point):
        self.__point_1 = point_1
        self.__point_2 = point_2

    def __str__(self):
        """
        Calcula el vector resultante entre 2 puntos
        """
        return f'{{{self.__point_2.x - self.__point_1.x}; ' \
               f'{self.__point_2.y - self.__point_1.y}}}'

    def module(self):
        """
        Calcula la distancia entre 2 puntos
        """
        return math.sqrt((self.__point_2.x - self.__point_1.x) ** 2
                         + (self.__point_2.y - self.__point_1.y) ** 2)


class Rectangle:
    def __init__(self, start: Point, end: Point):
        self.__start = start
        self.__end = end

    def area(self):
        return self.base() * self.height() / 2

    def base(self):
        return self.__end.x - self.__start.x

    def height(self):
        return self.__end.y - self.__start.y


def main():
    point_a = Point(2, 3)
    point_b = Point(5, 5)
    point_c = Point(-3, -1)
    point_d = Point()

    print(f'Punto A: {point_a}')
    print(f'Punto B: {point_b}')
    print(f'Punto C: {point_c}')
    print(f'Punto D: {point_d}')

    print(f'Cuadrante Punto A: {point_a.quadrant()}')
    print(f'Cuadrante Punto B: {point_b.quadrant()}')
    print(f'Cuadrante Punto C: {point_c.quadrant()}')

    vector_ab = Vector(point_a, point_b)
    print(f'Vector AB: {vector_ab}')

    vector_ba = Vector(point_b, point_a)
    print(f'Vector BA: {vector_ba}')

    print(f'Distancia entre los puntos A y B: {vector_ab.module()}')
    print(f'Distancia entre los puntos B y A {vector_ba.module()}')

    distance_to_origin = {
        Vector(point_a, Point()).module(): 'A',
        Vector(point_b, Point()).module(): 'B',
        Vector(point_c, Point()).module(): 'C'
    }

    print(f'El punto {distance_to_origin[max(distance_to_origin.keys())]} '
          f'se encuentra más lejos del origen.')

    rectangulo = Rectangle(point_a, point_b)
    print(f'Base: {rectangulo.base()}')
    print(f'Altura: {rectangulo.base()}')
    print(f'Área: {rectangulo.area()}')


if __name__ == '__main__':
    main()
