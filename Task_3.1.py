"""
Создать класс дробь(Fraction), конструктор которого принимает целые числа (num, den  -  числитель(numerator),
знаменатель(denominator) ).

Выполнить
Атрибуты числитель и знаменатель в классе сделать приватными. Доступ к атрибутам реализовать через свойства.

Переопределить методы __sub__, __add__, __mull__, __truediv__
для того, чтобы можно было выполнять соответствующие математические действия  с объектами класса дробь.
(Вычитание, сложение, умножение и деление).

В миксине реализовать статические методы, для этих же операций(add, sub, mull, div).

Добавить в класс миксин.
Создать classmethod который из строки типа 'числитель/знаменатель' возвращает объект класса дробь.
Переопределить метод __str__, который при выводе объекта на печать будет выводить строку вида num / den.

Создать объекты класса дробь.
Выполнить все реализованные методы.
"""


class BestFraction:
    def __init__(self, num, den):
        # self.__num = num
        # self.__den = den
        self.set_numbers_num = num
        self.set_numbers_den = den

    # checking for integer and division by zero
    def set_numbers(self, num, den):
        if type(num) in (int, float) and type(den) in (int, float):
            self.__num = num
            self.__den = den

            # Check division by zero
            try:
                if self.__den == 0:
                    print("Check", num / den)
            except ZeroDivisionError as zero:
                print(zero, "Cannot division by 0")
        else:
            raise ValueError("Enter integer number")

    def get_numbers(self):
        return self.__num, self.__den


class AddMixin:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __add__(self):
        print("add call")
        return self.__num + self.__den


class SubMixin:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __sub__(self):
        print("sub call")
        return self.__num - self.__den


class MulMixin:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __mul__(self):
        print("Mul call")
        return self.__num * self.__den


class DivMixin:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def __truediv__(self):
        print("Truediv call")
        return self.__num / self.__den


class TestMixin(AddMixin, SubMixin, MulMixin, DivMixin):

    @staticmethod
    def Add(num, den):
        return num + den

    @staticmethod
    def Sub(num, den):
        return num - den

    @staticmethod
    def Mul(num, den):
        return num * den

    @staticmethod
    def Div(num, den):
        return num / den

    # @classmethod

    def __str__(self):
        return f"Fraction: {self.__num} / {self.__den}"


class Fraction(TestMixin, BestFraction):
    pass


Fr = Fraction(100, 10)
print(dir(Fr))
print(Fr.Div(123, 88))
print(Fr.__add__())
# print(Fr.__sub__())
