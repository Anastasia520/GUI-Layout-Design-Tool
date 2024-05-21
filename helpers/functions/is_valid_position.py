def is_valid_position(new_rect, existing_rectangles, canvas_width, canvas_height):
    # Проверка можно ли разместить прямоугольник в данной точке

    # Проверка находится ли прямоугольник в пределах холста
    if new_rect.left() < 0 or new_rect.top() < 0 or \
       new_rect.right() > canvas_width or \
       new_rect.bottom() > canvas_height:
        return False

    # Перебором всех существующих прямоугольников происходит проверка,
    # пересекается ли новый прямоугольник с текущими существующими прямоугольниками
    for rect, _ in existing_rectangles:
        if new_rect.intersects(rect):
            return False
    return True
