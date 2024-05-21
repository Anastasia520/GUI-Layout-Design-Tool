# Rectangles Test Task

## Описание

Эта программа с использованием библиотеки PyQt6 создает графическое окно, в котором можно добавлять, перетаскивать и соединять прямоугольники. 

## Установка и запуск

1. Убедитесь, что у вас установлен Python 3.8 или выше.
2. Установите зависимости:

    ```bash
    pip install PyQt6
    ```
3. Запустите файл `main.py`:

    ```bash
    python main.py
    ```
## Использование

### Режимы работы

- **Режим добавления**: По двойному клику левой кнопкой мыши создается прямоугольник.
- **Режим соединений**: Нажмите `C` для включения/выключения режима соединений. В этом режиме по клику на два разных прямоугольника между ними создается линия.
- **Режим удаления**: Нажмите `D` для включения/выключения режима удаления. В этом режиме по клику на линию она удаляется.

## Примечания

- Прямоугольники не создаются, если место клика слишком близко к краям сцены или пересекается с другим прямоугольником.
- Связи автоматически обновляются при перемещении прямоугольников.
- Прямоугольник нельзя создать в режиме соединения или удаления.
