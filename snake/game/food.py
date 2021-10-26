import random
from game import constants
from game.actor import Actor
from game.point import Point

# TODO: Define the Food class here


class Food(Actor):
    def __init__(self) -> None:
        super().__init__()

        self._points = 0
        self.text("@")
        self.reset()

    def get_points(self):
        return self._points

    def text(self, text):
        self._text = text

    def reset(self):
        self._points = random.randint(1, 5)

        x = random.randint(1, constants.MAX_X - 2)
        y = random.randint(1, constants.MAX_Y - 2)
        position = Point(x, y)
        self.set_position(position)
