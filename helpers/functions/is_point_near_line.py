def is_point_near_line(x, y, x1, y1, x2, y2, line_width):
    # Проверка, находится ли точка (x, y) на линии между точками (x1, y1) и (x2, y2) с учетом ширины линии

    # Вычисление длины линии между точками (x1, y1) и (x2, y2) по теореме Пифагора
    line_length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    # Если начальная и конечная точки совпадают
    if line_length == 0:
        return False

    # Формула для вычисления расстояния от точки до линии
    distance = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1) / line_length

    # Если расстояние меньше, чем половина ширины линии, то точка находится в зоне клика по линии
    return distance <= line_width / 2