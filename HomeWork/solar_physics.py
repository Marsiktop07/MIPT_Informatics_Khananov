from math import atan


gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


class Star():
    """Тип данных, описывающий звезду.
    Содержит массу, координаты, скорость звезды,
    а также визуальный радиус звезды в пикселах и её цвет.
    """

    type = "star"
    """Признак объекта звезды"""

    m = 0
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

    image = None
    """Изображение звезды"""


class Planet():
    """Тип данных, описывающий планету.
    Содержит массу, координаты, скорость планеты,
    а также визуальный радиус планеты в пикселах и её цвет
    """

    type = "planet"
    """Признак объекта планеты"""

    m = 0
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

    image = None
    """Изображение планеты"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    global gravitational_constant
    body.Fx = 0
    body.Fy = 0

    for obj in space_objects:
        if body != obj:
            x = obj.x - body.x
            y = obj.y - body.y
            r = (x ** 2 + y ** 2) ** 0.5
            sina = y / r
            cosa = x / r
            F = (gravitational_constant * obj.m * body.m) / (r ** 2)
            body.Fx += F * cosa
            body.Fy += F * sina

def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.
    Считает угловую скорость

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx / body.m
    ay = body.Fy / body.m
    body.Vx += ax * dt
    body.Vy += ay * dt
    body.x += body.Vx * dt
    body.y += body.Vy * dt



def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)

def calculate_angle_speed(body, space_objects, dt):
    if body.type != 'star':
        for obj in space_objects:
            if obj.type == 'star':
                x = obj.x
                y = obj.y
        r = ((body.x - x) ** 2 + (body.y - y) ** 2) ** 0.5
        dS = (body.Vx ** 2 + body.Vy ** 2) ** 0.5 * dt
        alfa = atan(dS / r)
        omega = alfa / dt
        S = dS * r / 2
        return omega, S
    else:
        return


if __name__ == "__main__":
    print("This module is not for direct call!")