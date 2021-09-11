import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _directions (Dict): A dictionary containing Points for U, D, L and R.
        _current (Point): The last direction that was pressed.
    """

    def __init__(self, screen):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        self._screen = screen
        self._keys = {}
        self._keys[119] = Point(0, -1) # UP
        self._keys[115] = Point(0, 1) # LEFT
        self._keys[97] = Point(-1, 0) # DOWN
        self._keys[100] = Point(1, 0) # RIGHT
        self._current = Point(1, 0)
        
    def get_direction(self):
        """Gets the selected direction. If one hasn't been selected the last 
        one is returned.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            Point: The selected direction.
        """
        event = self._screen.get_event()
        if isinstance(event, KeyboardEvent):
            if event.key_code == 27:
                sys.exit()
            self._current = self._keys.get(event.key_code, self._current)
        return self._current