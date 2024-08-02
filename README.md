# GUI Layout Design Tool
## Description

This program uses the PyQt6 library to create a graphical window where you can add, drag, and connect rectangles.

## Installation and Launch

1. Ensure you have Python 3.8 or higher installed.
2. Install the dependencies:

    ```bash
    pip install PyQt6
    ```
3. Run the `main.py` file:

    ```bash
    python main.py
    ```
## Usage

### Modes of Operation

- **Add Mode**: Double-clicking the left mouse button creates a rectangle.
- **Connection Mode**: Press `C` to toggle connection mode. In this mode, clicking on two different rectangles will create a line between them.
- **Delete Mode**: Press `D` to toggle delete mode. In this mode, clicking on a line will delete it.

## Notes

- Rectangles are not created if the click location is too close to the scene edges or intersects with another rectangle.
- Connections automatically update when rectangles are moved.
- Rectangles cannot be created in connection or delete mode.
