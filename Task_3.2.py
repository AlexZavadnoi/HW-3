"""
Task 3.2
Создать класс Point2D. Координаты точки задаются 2 параметрами -
координатами x, y на плоскости.
Реализовать метод distance который принимает экземпляр класса Point2D и
рассчитывает расстояние между 2мя точками на плоскости.
Создать защищенный атрибут класса - счетчик созданных экземпляров класса.
Чтение количества экземпляров реализовать через метод getter.
Создать класс Point3D, который является наследником класса Point2D.
Координаты точки задаются 3 параметрами - координатами x, y, z в пространстве.
Переопределить конструктор с помощью super().
Переопределить метод distance для определения расстояния между 2-мя точками в пространстве.
"""


class Points2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanse2D(self):
        return ("Расстояние от точки х до то у", self.x - self.y)

    # Check Value
    def __checkValue(x):
        if isistance(x, int) or isistance(x, float):
            return True
        return False


class Points3D(Points2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def distanse3D(self):
        return ("Расстояние от точки х до то у", self.x - self.y,
                "от точки х до то z", self.x - self.z,
                "от точки х до то z", self.y - self.z)


def __getter__(self, item):
    print()
    return


point2D = Points2D(10, 20)
point3D = Points3D(30, 10, 15)

# print(Points2D().distanse2D())

print(point2D.distanse2D())
print(point3D.distanse3D())
