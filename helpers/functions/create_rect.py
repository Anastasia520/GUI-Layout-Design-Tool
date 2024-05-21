from PyQt6.QtCore import QRect

from helpers.functions.is_valid_position import is_valid_position


def create_rect(center_x, center_y, width, height, existing_rectangles, canvas_width, canvas_height):
    # Создание нового прямоугольника

    # Вычисление координат верхнего левого угла нового прямоугольника на основе центра
    top_left_x = center_x - width // 2
    top_left_y = center_y - height // 2

    # Создание прямоугольника по координатам
    new_rect = QRect(top_left_x, top_left_y, width, height)

    # Проверка расположения прямоугольника
    # Если расположение валидно, то прямоугольник создается
    if (is_valid_position(new_rect, existing_rectangles, canvas_width, canvas_height)):
        return new_rect
    # Если разместить нельзя, то возвращает None
    return None


