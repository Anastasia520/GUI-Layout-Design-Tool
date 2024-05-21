from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt, QTimer, QRect

from constants import RECT_WIDTH, RECT_HEIGHT, LINE_WIDTH, TIMER_INTERVAL
from helpers.functions.is_point_near_line import is_point_near_line
from helpers.functions.create_rect import create_rect
from helpers.functions.is_valid_position import is_valid_position
from helpers.functions.random_color import random_color


class Canvas(QWidget):
    def __init__(self):
        super().__init__()
        self.rectangles = []  # Массив прямоугольников
        self.connections = []  # Массив с соединениями
        self.selected_rect = None  # Текущий выбранный прямоугольник
        self.offset = None  # Смещение при перетаскивании прямоугольника
        self.connection_mode = False  # Режим соединения прямоугольников
        self.deletion_mode = False  # Режим удаления соедениний
        self.start_connection = None  # Выбранный прямоугольник для соедениния
        self.timer = QTimer()  # Таймер для обновления виджета
        self.timer.timeout.connect(self.update)
        self.timer.start(TIMER_INTERVAL) # Установка интервала таймера\fps
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)  # Позволяет виджету принимать фокус на клавиши

    # Обработка события отрисовка
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing) # Включение сглаживания

        pen = QPen(Qt.GlobalColor.black, LINE_WIDTH)
        painter.setPen(pen)

        # Рисование соединений
        for rect1, rect2 in self.connections:
            painter.drawLine(rect1.center(), rect2.center())

        # Рисование прямоугольников
        for rect, color in self.rectangles:
            painter.setBrush(color)
            painter.drawRect(rect)

        # Добавление надписи при включении режима соединения
        if self.connection_mode:
            painter.setPen(QPen(Qt.GlobalColor.red))
            painter.drawText(10, 20, "Connect Mode")
        # Добавление надписи при включении режима удаления соединений
        elif self.deletion_mode:
            painter.setPen(QPen(Qt.GlobalColor.red))
            painter.drawText(10, 20, "Delete Mode")

    # Обработка события двойной клик мыши
    def mouseDoubleClickEvent(self, event):
        # Если включен какой-то режим, то добавить прямоугольник нельзя
        if event.button() == Qt.MouseButton.LeftButton and not self.deletion_mode and not self.connection_mode:
            # Точка центра прямоугольника
            center_x, center_y = int(event.position().x()), int(event.position().y())

            # Создание прямоугольника
            rect = create_rect(center_x, center_y, RECT_WIDTH, RECT_HEIGHT, self.rectangles, self.width(),
                               self.height())

            # Если прямоугольник создался, то происходит добавление его в массив прямоугольников
            if rect:
                color = random_color()  # Генерация случайного цвета для нового прямоугольника
                self.rectangles.append((rect, color))
                self.update()

    # Обработка события клик мыши
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            click_pos = event.position().toPoint()

            # Если режим удаления соединений
            if self.deletion_mode:
                for rect1, rect2 in self.connections:
                    # Проверка клика в отдалености от соединения между прямоугольниками
                    if is_point_near_line(event.position().x(), event.position().y(), rect1.center().x(), rect1.center().y(),rect2.center().x(), rect2.center().y(), LINE_WIDTH):
                        self.connections.remove((rect1, rect2))
                        self.update()
                        return
            else:
                for rect, _ in self.rectangles:
                    # Проверка находится ли клик в прямоугольнике
                    if rect.contains(click_pos):

                        # Если режим соединения, то создание соединения между прямоугольниками
                        if self.connection_mode:
                            if self.start_connection is None:
                                self.start_connection = rect
                            else:
                                self.connections.append((self.start_connection, rect))
                                self.start_connection = None

                        # Иначе выбор прямоугольника для перетаскивания
                        else:
                            self.selected_rect = rect
                            self.offset = click_pos - rect.topLeft()
                        self.update()
                        return

 # Обработка события движения мыши
    def mouseMoveEvent(self, event):
        # Если выбран прямоугольник, то перетаскивание выбранного прямоугольника
        if self.selected_rect:
            new_top_left = event.position().toPoint() - self.offset
            new_rect = QRect(new_top_left, self.selected_rect.size())

            # Проверка валидной позиции прямоугольника при перемещении
            if is_valid_position(new_rect, self.rectangles, self.width(), self.height()):
                self.selected_rect.moveTo(new_top_left)
            self.update()

    # Обработка события отпускание кнопки мыши
    def mouseReleaseEvent(self, event):
        # Сброс выбранного прямоугольника для перетаскивания
        if event.button() == Qt.MouseButton.LeftButton:
            self.selected_rect = None

    # Обработка события нажатий на клавиши
    def keyPressEvent(self, event):
        # Если нажата C, то включается режим соединений
        if event.key() == Qt.Key.Key_C:
            self.connection_mode = not self.connection_mode
            self.deletion_mode = False

        # Если нажата D, то включается режим удаления соединений
        elif event.key() == Qt.Key.Key_D:
            self.deletion_mode = not self.deletion_mode
            self.connection_mode = False
