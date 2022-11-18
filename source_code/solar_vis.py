# coding: utf-8
# license: GPLv3

import pygame as pg
from matplotlib import pyplot as plt

"""Модуль визуализации.
Нигде, кроме этого модуля, не используются экранные координаты объектов.
Функции, создающие гaрафические объекты и перемещающие их на экране, принимают физические координаты
"""

header_font = "Arial-16"
"""Шрифт в заголовке"""

window_width = 1000
"""Ширина окна"""

window_height = 900
"""Высота окна"""

scale_factor = 1
"""Масштабирование экранных координат по отношению к физическим.

Тип: float

Мера: количество пикселей на один метр."""


def calculate_scale_factor(max_distance):
    """Вычисляет значение глобальной переменной **scale_factor** по данной характерной длине"""
    global scale_factor
    scale_factor = 0.5*min(window_height, window_width)/max_distance
    print('Scale factor:', scale_factor)


def scale_x(x):
    """Возвращает экранную **x** координату по **x** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **x** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.

    Параметры:

    **x** — x-координата модели.
    """

    return int(x*scale_factor) + window_width//2


def scale_y(y):
    """Возвращает экранную **y** координату по **y** координате модели.
    Принимает вещественное число, возвращает целое число.
    В случае выхода **y** координаты за пределы экрана возвращает
    координату, лежащую за пределами холста.
    Направление оси развёрнуто, чтобы у модели ось **y** смотрела вверх.

    Параметры:

    **y** — y-координата модели.
    """
    return window_height // 2 - int(y * scale_factor)


def draw_plots(name, x_data, y_data, x_label, y_label):
    """
       Создаёт картинку с графиком
       Args:
           x_data - данные по оси x
           y_data - данные по оси y
           x_label - подпись оси x
           y_label - подпись оси y
       """
    if name == 'V(t)':
        title = 'Скорость от времени'
    elif name == 'Dist(t)':
        title = 'Расстояние от времени'
    else:
        title = 'Скорость от расстояния'
    plt.figure()
    plt.title(title)
    plt.grid()
    plt.minorticks_on()

    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.plot(x_data, y_data)
    plt.savefig(name + '.jpg')


if __name__ == "__main__":
    print("This module is not for direct call!")


class Drawer:
    def __init__(self, screen):
        self.screen = screen

    def update(self, figures, ui):
        self.screen.fill((0, 0, 0))
        for figure in figures:
            figure.draw(self.screen)
        
        ui.blit()
        ui.update()
        pg.display.update()


class DrawableObject:
    def __init__(self, obj):
        self.obj = obj

    def draw(self, surface):
        x = scale_x(self.obj.x)
        y = scale_y(self.obj.y)
        r = self.obj.R
        pg.draw.circle(surface, self.obj.color, (x, y), r)
