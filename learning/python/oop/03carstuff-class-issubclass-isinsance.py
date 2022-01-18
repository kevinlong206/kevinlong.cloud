class Engine():
    def start(self):
        pass

    def stop(self):
        pass

class ElectricEngine(Engine):
    # Is-A Engine
    pass

class V8Engine(Engine):
    #Is-A Engine
    pass

class Car():
    engine_cls = Engine

    def __init__(self):
        self.engine = self.engine_cls() # Has-A Engine

    def start(self):
        print(
            'Starting engine {0} for car {1}... Wroom, wroom'
            .format(self.engine.__class__.__name__, self.__class__.__name__)
            )

    def stop(self):
        self.engine.stop()


class RaceCar(Car): # Is-A Car
    engine_cls = V8Engine

class CityCar(Car): #Is-A Car
    engine_cls = ElectricEngine

class F1Car(RaceCar): # Is-A RaceCar and Car
    engine_cls = V8Engine

car = Car()
racecar = RaceCar()
citycar = CityCar()
f1car = F1Car()
cars = [(car, 'car'), (racecar, 'racecar'), (f1car, 'f1car')]

car_classes = [Car, RaceCar, F1Car]

for class1 in car_classes:
    for class2 in car_classes:
        is_subclass = issubclass(class1,class2)
        msg = '{0} a subclass of'.format(
            'is' if is_subclass else 'is not')
        print(class1.__name__, msg, class2.__name__)
