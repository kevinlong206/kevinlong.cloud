class Shape:
    geometric_type = 'Generic Shape'

    def area(self): # placeholder for interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type

class Plotter:
    def plot(self, ratio, topleft):
        # Image some nice plotting logic
        print('Plotting at {}, ratio {}.'.format(topleft, ratio))


class Polygon(Shape, Plotter): # base class for polygons
    geometric_type = 'Polygon'

class RegularPolygon(Polygon): # Is-A Polygon
    geometric_type = 'Regular Polyogon'

    def __init__(self, side):
        self.side = side

class RegularHexagon(RegularPolygon): # Is-A RegularPolygon
    geometric_type = 'Regular Hexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)

class Square(RegularPolygon): # is a RegularPolygon
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side


hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75,77))

square = Square(12)
print(square.area())
print(square.get_geometric_type())
square.plot(0.93,(74,75))


# Get the method resolution order
print(square.__class__.__mro__)
print(Square.mro())
