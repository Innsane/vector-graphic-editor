from enum import Enum


class Shapes(Enum):
    LINE = 'line'
    CIRCLE = 'circle'
    ELLIPSE = 'ellipse'
    SQUARE = 'square'
    RECTANGLE = 'rectangle'
    TRIANGLE = 'triangle'
    STAR = 'star'

class DrawShape():
    def __init__(self):
        self.shape = Shapes.LINE

    def draw(self, e):
        pass