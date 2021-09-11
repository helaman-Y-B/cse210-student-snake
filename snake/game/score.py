import random
from game.actor import Actor
from game.point import Point

class Score(Actor):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        self._points = 0
        position = Point(1, 0)
        self.set_position(position)
        self.set_text(f"Score: {self._points}")
    
    def add_points(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        self._points += points
        self.set_text(f"Score: {self._points}")