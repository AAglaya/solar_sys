# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
from solar_vis import DrawableObject

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename, 'r') as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем

            object_type = line.split()[0].lower()
            if object_type == "star":
                star_parameters = parse_star_parameters(line)
                star = Star(**star_parameters)
                objects.append(star)
            elif object_type == "planet":
                planet_parameters = parse_planet_parameters(line)
                planet = Planet(**planet_parameters)
                objects.append(planet)
            else:
                print("Unknown space object")

    return [DrawableObject(obj) for obj in objects]


def parse_star_parameters(line):
    """Считывает данные о звезде из строки.

    Входная строка должна иметь слеюущий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.

    Пример строки:

    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.

    **star** — объект звезды.
    """

    line_to_list = list(line.split())
    parameters = {'R': int(line_to_list[1]), 'color': str(line_to_list[2]), 'm': float(line_to_list[3]),
                  'x': float(line_to_list[4]), 'y': float(line_to_list[5]), 'Vx': float(line_to_list[6]),
                  'Vy': float(line_to_list[7])}
    return parameters

def parse_planet_parameters(line):
    """Считывает данные о планете из строки.
    Входная строка должна иметь слеюущий формат:

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.

    Пример строки:

    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.

    **planet** — объект планеты.
    """
    line_to_list = list(line.split())
    parameters = {'R': int(line_to_list[1]), 'color': str(line_to_list[2]), 'm': float(line_to_list[3]),
                  'x': float(line_to_list[4]), 'y': float(line_to_list[5]), 'Vx': float(line_to_list[6]),
                  'Vy': float(line_to_list[7])}
    return parameters

def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.

    Строки должны иметь следующий формат:

    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла

    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            out_file.write(str(obj.obj.type).title()  + ' ' + str(obj.obj.R) + ' ' + str(obj.obj.color) + ' ' + str(obj.obj.m) + ' ' +
                               str(obj.obj.x) + ' ' + str(obj.obj.y) + ' ' + str(obj.obj.Vx) + ' ' + str(obj.obj.Vy) + '\n')



if __name__ == "__main__":
    print("This module is not for direct call!")
