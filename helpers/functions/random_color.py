import random
from PyQt6.QtGui import QColor

# Генерация случайного цвета
def random_color():
    return QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
