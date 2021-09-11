from game import constants
from game.actor import Actor
from game.point import Point

class Snake:
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Snake): An instance of snake.
        """
        super().__init__()
        self._segments = []
        self._prepare_body()
    
    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._segments

    def get_body(self):
        """Gets the snake's body.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's body.
        """
        return self._segments[1:]

    def get_head(self):
        """Gets the snake's head.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            Actor: The snake's head.
        """
        return self._segments[0]

    def grow_tail(self):
        """Grows the snake's tail by one segment.
        
        Args:
            self (Snake): An instance of snake.
        """
        tail = self._segments[-1]
        offset = tail.get_velocity().reverse()
        text = "#"
        position = tail.get_position().add(offset)
        velocity = tail.get_velocity()
        self._add_segment(text, position, velocity)
    
    def move_head(self, direction):
        """Moves the snake in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        count = len(self._segments) - 1
        for n in range(count, -1, -1):
            segment = self._segments[n]
            if n > 0:
                leader = self._segments[n - 1]
                velocity = leader.get_velocity()
                segment.set_velocity(velocity)
            else:
                segment.set_velocity(direction)
            segment.move_next()

    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_body(self):
        """Prepares the snake body by adding segments.
        
        Args:
            self (Snake): an instance of Snake.
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(constants.SNAKE_LENGTH):
            text = "8" if n == 0 else "#"
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(text, position, velocity)