import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

from constants import WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_X, WINDOW_Y
from canvas import Canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rectangles Test Task') # Установка заголовка окна
        self.setGeometry(WINDOW_X, WINDOW_Y, WINDOW_WIDTH, WINDOW_HEIGHT) # Установка положения и размеров окна
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)  # Установка Canvas в качестве центрального виджета окна


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()  # Создание экземпляра главного окна
    window.show()  # Отображение главного окна
    sys.exit(app.exec())  # Запуск приложения и выход из программы при его завершении
