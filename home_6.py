# class Shape:
#     def draw(self):
#         print("Рисуем фигуру")

# class Circle(Shape):
#     def draw(self):
#         print("Рисуем Круг")

# class Rectangle(Shape):
#     def draw(self):
#         print("Рисуем Прямаугольник")


# shape = Shape()
# shape.draw()
# circle = Circle()
# circle.draw()
# rectangle = Rectangle()
# rectangle.draw()


class Counter:
    def __init__(self):
        self.value = 0

    def increment(self, value):
        self.value += value

    def get_value(self):
        return self.value

counter = Counter()
print(counter.get_value())
counter.increment(8)
print(counter.get_value())