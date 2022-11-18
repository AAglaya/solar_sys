# coding: utf-8
# license: GPLv3


class Star:
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 1
    """Масса звезды"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус звезды"""

    color = "red"
    """Цвет звезды"""

    def __init__(self, m, x, y, Vx, Vy, R, color):
        """ Конструктор класса Star
        Args:
            type - Признак объекта звезды
            m - Масса звезды
            x - Координата по оси **x**
            y - Координата по оси **y**
            Vx - Скорость по оси **x**
            Vy - Скорость по оси **y**
            R - Радиус звезды
            color - Цвет звезды
        """
        self.type = "star"
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.R = R
        self.color = color


class Planet:
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 1
    """Масса планеты"""

    x = 0
    """Координата по оси **x**"""

    y = 0
    """Координата по оси **y**"""

    Vx = 0
    """Скорость по оси **x**"""

    Vy = 0
    """Скорость по оси **y**"""

    Fx = 0
    """Сила по оси **x**"""

    Fy = 0
    """Сила по оси **y**"""

    R = 5
    """Радиус планеты"""

    color = "green"
    """Цвет планеты"""

    def __init__(self, m, x, y, Vx, Vy, R, color):
        """ Конструктор класса Star
        Args:
            type - Признак объекта планеты
            m - Масса планеты
            x - Координата по оси **x**
            y - Координата по оси **y**
            Vx - Скорость по оси **x**
            Vy - Скорость по оси **y**
            R - Радиус планеты
            color - Цвет планеты
        """
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.R = R
        self.color = color
        self.list_of_velocity = []
        self.list_of_distance = []

    def log_velocity(self):
        self.list_of_velocity.append((self.Vx ** 2 + self.Vy ** 2) ** 0.5)

    def log_distance(self, distance):
        self.list_of_distance.append(distance)

    def data_velocity(self):
        return self.list_of_velocity

    def data_distance(self):
        return self.list_of_distance
