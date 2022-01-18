class Rectangle():
    def __init__(self, sideA, sideB):
        self.sideA = sideA
        self.sideB = sideB

    def area(self):
        return self.sideA * self.sideB


r1 = Rectangle(10, 4)
print(r1.sideA, r1.sideB) # 10 4
print(r1.area()) #40

r2 = Rectangle(7, 3)
print(r2.area()) #21
