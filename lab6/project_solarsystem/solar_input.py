# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet
#def calc(a):
    #if 'E' in a:
        #b = a.split('E')
        #c = float(b[0])*10**(float(b[1]))
   # else:
       # c = float(a)
    #return c

def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    input_filename — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXED
                star = Star()
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # FIXED
                planet = Planet()
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects


def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    line — строка с описание звезды.
    star — объект звезды.
    """
    a = line.split()
    star.R = float(a[1])
    star.color = a[2]
    star.m = float(a[3])
    star.x = float(a[4])
    star.y = float(a[5])
    star.Vx = float(a[6])
    star.Vy = float(a[7])




    #pass  # FIXED

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 100 red 1010 1 2 3 4
    Параметры:
    planet — объект планеты.
    line — строка с описание планеты.
    """

    a = line.split()
    planet.R = float(a[1])
    planet.color = a[2]
    planet.m =float(a[3])
    planet.x =float(a[4])
    planet.y = float(a[5])
    planet.Vx = float(a[6])
    planet.Vy =float(a[7])






def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    space_objects — список объектов планет и звёзд
    output_filename — имя входного файла
    """
    out_file = open(output_filename, 'w')
    for obj in space_objects:
        out_file.write(obj.type + ' ' + str(obj.R) + ' ' + obj.color + ' ' + str(obj.m) + ' ' + str(obj.x) +
                       ' ' + str(obj.y) + ' ' + str(obj.Vx) + ' ' + str(obj.Vy) + '\n')
    out_file.close()



if __name__ == "__main__":
    print("This module is not for direct call!")