'''
Задание 3.
Классы. Наследование, волшебные методы.
'''


# Необходимо реализовать семейство классов, обеспечивающих прозрачную работу с такими единицами
# измерения, как миллиметры, сантиметры, метры, километры, дюймы, футы, ярды, фэнь, чи и инь.
# Требуется реализовать метод __str__, который будет возвращать текущее значение и единицу измерения,
# например "1 км", "2.35 мили" и т. д.
# Требуется реализовать методы __eq__ и __lt__ для сравнения любых единиц измерения между собой.
# Требуется реализовать методы __add__, __iadd__, __sub__ и __isub__, принимающие в качестве
# аргумента любой класс единиц, а также просто число. Если в качестве аргумента выступает число,
# то оно трактуется, как количество текущих единиц измерения.
# Требуется реализовать методы __mul__ и __imul__, принимающие числовое значение в качестве аргумента.
# Требуется реализовать методы __div__ и __idiv__, принимающие как числовое значение, так и любой класс
# единиц измерения. В случае, если в качестве аргумента выступает числовое значение, то результат
# возвращается в тех же единицах измерения, что и текущая. В остальных случаях возвращается число.
# Требуется добавить способ конвертации из одной системы единиц в другую (желательно с использованием
# __init__.
# Необходимо выбрать базовую единицу измерения, к которой во время выполнения операций будут
# приводиться все значения. Ее же использовать и в базовом классе. Практически вся функциональность
# реализуется в базовом классе. Иерархию наследования можно сделать двухуровневой, задача подходит
# для этого.


class LengthUnits:
    UNIT = 'm'
    FACTOR = 1

    def __init__(self, value):
        self.value = value * self.FACTOR if type(value) in (float, int) else value.value

    def __str__(self):
        return f'{self.value / self.FACTOR} {self.UNIT}'

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __add__(self, other):
        if not isinstance(other, (float, int, LengthUnits)):
            raise TypeError('Unsupported operand type.')
        return type(self)(self.value / self.FACTOR + other) if type(other) in (float, int) else type(self)(
            (self.value + other.value) / self.FACTOR)

    def __iadd__(self, other):
        if not isinstance(other, (float, int, LengthUnits)):
            raise TypeError('Unsupported operand type.')
        self.value += other * self.FACTOR if type(other) in (float, int) else other.value
        return self

    def __sub__(self, other):
        if not isinstance(other, (float, int, LengthUnits)):
            raise TypeError('Unsupported operand type.')
        return type(self)(self.value / self.FACTOR - other) if type(other) in (float, int) else type(self)(
            (self.value - other.value) / self.FACTOR)

    def __isub__(self, other):
        if not isinstance(other, (float, int, LengthUnits)):
            raise TypeError('Unsupported operand type.')
        self.value -= other * self.FACTOR if type(other) in (float, int) else other.value
        return self

    def __mul__(self, other):
        if type(other) not in (float, int):
            raise TypeError('Unsupported operand type.')
        return type(self)(self.value / self.FACTOR * other)

    def __imul__(self, other):
        if type(other) not in (float, int):
            raise TypeError('Unsupported operand type.')
        self.value *= other
        return self

    def __truediv__(self, other):
        if not isinstance(other, (float, int, LengthUnits)):
            raise TypeError('Unsupported operand type.')
        return type(self)(self.value / self.FACTOR / other) if type(other) in (
            float, int) else self.value / other.value

    def __itruediv__(self, other):
        if type(other) not in (float, int):
            raise TypeError('Unsupported operand type.')
        self.value /= other
        return self


class Millimeters(LengthUnits):
    UNIT = 'mm'
    FACTOR = 0.001


class Centimeters(LengthUnits):
    UNIT = 'cm'
    FACTOR = 0.01


class Meters(LengthUnits):
    UNIT = 'm'
    FACTOR = 1


class Kilometers(LengthUnits):
    UNIT = 'km'
    FACTOR = 1000


class Inches(LengthUnits):
    UNIT = 'in'
    FACTOR = 0.0254


class Feets(LengthUnits):
    UNIT = 'ft'
    FACTOR = 0.3048


class Yards(LengthUnits):
    UNIT = 'yd'
    FACTOR = 0.9144


class Miles(LengthUnits):
    UNIT = 'mi'
    FACTOR = 1609.34


class Fen(LengthUnits):
    UNIT = 'fen'
    FACTOR = 1 / 300


class Chi(LengthUnits):
    UNIT = 'chi'
    FACTOR = 1 / 3


class In(LengthUnits):
    UNIT = 'in'
    FACTOR = 100 / 3
