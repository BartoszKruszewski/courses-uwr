import sys
from typing import List, Optional, Tuple
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QFrame
)
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRectF, QPointF

# === Shapes and Prototypes ===

class Shape:
    def __init__(self, x: float, y: float, color: QColor):
        self.x, self.y = x, y
        self.color = color

    def draw(self, painter: QPainter) -> None:
        raise NotImplementedError

    def contains(self, px: float, py: float) -> bool:
        raise NotImplementedError

    def move(self, dx: float, dy: float) -> None:
        self.x += dx
        self.y += dy

    def clone(self) -> 'Shape':
        return type(self)(self.x, self.y, self.color)


class Circle(Shape):
    def draw(self, painter: QPainter) -> None:
        painter.setBrush(self.color)
        painter.drawEllipse(QRectF(self.x - 20, self.y - 20, 40, 40))

    def contains(self, px: float, py: float) -> bool:
        return (self.x - px) ** 2 + (self.y - py) ** 2 <= 400


class Square(Shape):
    def draw(self, painter: QPainter) -> None:
        painter.setBrush(self.color)
        painter.drawRect(QRectF(self.x - 20, self.y - 20, 40, 40))

    def contains(self, px: float, py: float) -> bool:
        return abs(self.x - px) <= 20 and abs(self.y - py) <= 20


class Rectangle(Shape):
    def draw(self, painter: QPainter) -> None:
        painter.setBrush(self.color)
        painter.drawRect(QRectF(self.x - 30, self.y - 20, 60, 40))

    def contains(self, px: float, py: float) -> bool:
        return abs(self.x - px) <= 30 and abs(self.y - py) <= 20


# === Commands (Deltas) ===

class Command:
    def undo(self, canvas: 'Canvas') -> None: pass
    def redo(self, canvas: 'Canvas') -> None: pass


class AddShapeCommand(Command):
    def __init__(self, shape: Shape):
        self.shape = shape

    def undo(self, canvas: 'Canvas') -> None:
        canvas.shapes.remove(self.shape)

    def redo(self, canvas: 'Canvas') -> None:
        canvas.shapes.append(self.shape)


class DeleteShapeCommand(Command):
    def __init__(self, shape: Shape):
        self.shape = shape

    def undo(self, canvas: 'Canvas') -> None:
        canvas.shapes.append(self.shape)

    def redo(self, canvas: 'Canvas') -> None:
        canvas.shapes.remove(self.shape)


class MoveShapeCommand(Command):
    def __init__(self, shape: Shape, dx: float, dy: float):
        self.shape = shape
        self.dx = dx
        self.dy = dy

    def undo(self, canvas: 'Canvas') -> None:
        self.shape.move(-self.dx, -self.dy)

    def redo(self, canvas: 'Canvas') -> None:
        self.shape.move(self.dx, self.dy)


# === MementoManager (Caretaker) ===

class MementoManager:
    def __init__(self, canvas: 'Canvas'):
        self.canvas = canvas
        self.undo_stack: List[Command] = []
        self.redo_stack: List[Command] = []

    def execute(self, command: Command) -> None:
        command.redo(self.canvas)
        self.undo_stack.append(command)
        self.redo_stack.clear()
        self.canvas.update()

    def undo(self) -> None:
        if self.undo_stack:
            cmd = self.undo_stack.pop()
            cmd.undo(self.canvas)
            self.redo_stack.append(cmd)
            self.canvas.update()

    def redo(self) -> None:
        if self.redo_stack:
            cmd = self.redo_stack.pop()
            cmd.redo(self.canvas)
            self.undo_stack.append(cmd)
            self.canvas.update()


# === Canvas ===

class Canvas(QFrame):
    def __init__(self, memento: MementoManager):
        super().__init__()
        self.setFrameStyle(QFrame.Box)
        self.setMouseTracking(True)
        self.shapes: List[Shape] = []
        self.mode = 'circle'
        self.memento = memento

        self.prototypes = {
            'circle': Circle(0, 0, QColor("red")),
            'square': Square(0, 0, QColor("green")),
            'rect': Rectangle(0, 0, QColor("blue")),
        }

        self.selected_shape: Optional[Shape] = None
        self.last_pos: Optional[QPointF] = None

    def set_mode(self, mode: str) -> None:
        self.mode = mode

    def mousePressEvent(self, e) -> None:
        x, y = e.x(), e.y()
        if self.mode in self.prototypes:
            shape = self.prototypes[self.mode].clone()
            shape.x, shape.y = x, y
            self.memento.execute(AddShapeCommand(shape))
        elif self.mode == 'move':
            for shape in reversed(self.shapes):
                if shape.contains(x, y):
                    self.selected_shape = shape
                    self.last_pos = QPointF(x, y)
                    break
        elif self.mode == 'delete':
            for shape in reversed(self.shapes):
                if shape.contains(x, y):
                    self.memento.execute(DeleteShapeCommand(shape))
                    break

    def mouseMoveEvent(self, e) -> None:
        if self.mode == 'move' and self.selected_shape and self.last_pos:
            dx = e.x() - self.last_pos.x()
            dy = e.y() - self.last_pos.y()
            self.selected_shape.move(dx, dy)
            self.last_pos = QPointF(e.x(), e.y())
            self.update()

    def mouseReleaseEvent(self, e) -> None:
        if self.mode == 'move' and self.selected_shape and self.last_pos:
            dx = e.x() - self.last_pos.x()
            dy = e.y() - self.last_pos.y()
            if dx != 0 or dy != 0:
                self.memento.execute(MoveShapeCommand(self.selected_shape, dx, dy))
            self.selected_shape = None
            self.last_pos = None

    def paintEvent(self, _) -> None:
        painter = QPainter(self)
        for shape in self.shapes:
            shape.draw(painter)


# === MainWindow ===

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edytor graficzny z Memento")
        self.canvas: Optional[Canvas] = None
        self.init_ui()

    def init_ui(self) -> None:
        self.memento = MementoManager(None)
        self.canvas = Canvas(self.memento)
        self.memento.canvas = self.canvas  # późna referencja

        toolbar = QHBoxLayout()
        for label, mode in [
            ("Okrąg", 'circle'), ("Kwadrat", 'square'), ("Prostokąt", 'rect'),
            ("Przesuwaj", 'move'), ("Usuń", 'delete'), ("Undo", 'undo'), ("Redo", 'redo')
        ]:
            btn = QPushButton(label)
            btn.clicked.connect(self.make_handler(mode))
            toolbar.addWidget(btn)

        wrapper = QWidget()
        layout = QVBoxLayout()
        layout.addLayout(toolbar)
        layout.addWidget(self.canvas)
        wrapper.setLayout(layout)
        self.setCentralWidget(wrapper)

    def make_handler(self, mode: str):
        def handler():
            if mode == 'undo':
                self.memento.undo()
            elif mode == 'redo':
                self.memento.redo()
            else:
                self.canvas.set_mode(mode)
        return handler


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.resize(800, 600)
    win.show()
    sys.exit(app.exec_())