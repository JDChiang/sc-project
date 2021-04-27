"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

Name: Jo-Di(Frank), Chiang

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball.

# global variable


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self._paddle = GRect(paddle_width, paddle_height)
        self._paddle.filled = True
        self._paddle.fill_color = 'black'
        self.window.add(self._paddle, (window_width - paddle_width) / 2, window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.set_ball()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.play)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.draw_bricks()

        # Count bricks
        self.__brick = brick_cols * brick_rows

    # Set ball in the middle of the window
    def set_ball(self):
        self.window.add(self.ball, (self.window.width - self.ball.width * 2) / 2,
                        (self.window.height - self.ball.height * 2) / 2)
        self.__dx = 0
        self.__dy = 0

    def draw_bricks(self):
        """
        This function will add bricks on the window
        """
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                __brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                __brick.filled = True
                if i == 0 or i == 1:
                    __brick.fill_color = 'red'
                elif i == 2 or i == 3:
                    __brick.fill_color = 'orange'
                elif i == 4 or i == 5:
                    __brick.fill_color = 'yellow'
                elif i == 6 or i == 7:
                    __brick.fill_color = 'green'
                else:
                    __brick.fill_color = 'blue'
                self.window.add(__brick, j * (BRICK_WIDTH + BRICK_SPACING),
                                BRICK_OFFSET + i * (BRICK_HEIGHT + BRICK_SPACING))

    # getter of brick count
    def get_brick_count(self):
        return self.__brick

    # Mouseclick function
    def play(self, event):
        if self.ball.x == (self.window.width - self.ball.width * 2) / 2 \
                and self.ball.y == (self.window.height - self.ball.height * 2) / 2:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # Getter __dx
    def get_dx(self):
        return self.__dx

    # Getter __dy
    def get_dy(self):
        return self.__dy

    # Paddle tracker
    def paddle_move(self, event):
        if event.x <= self._paddle.width / 2:
            self._paddle.x = 0
        elif event.x >= self.window.width - self._paddle.width / 2:
            self._paddle.x = self.window.width - self._paddle.width
        else:
            self._paddle.x = event.x - self._paddle.width / 2

    def probe_check(self):
        # Set four probes on four corners of ball to detect object
        upper_left = self.window.get_object_at(self.ball.x, self.ball.y)
        lower_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        upper_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        lower_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.height)

        # Set four probes on four corners of paddle to detect object
        paddle_coordinate_upper_left = self.window.get_object_at(self._paddle.x, self._paddle.y)
        paddle_coordinate_lower_left = self.window.get_object_at(self._paddle.x, self._paddle.y + self._paddle.height)
        paddle_coordinate_upper_right = self.window.get_object_at(self._paddle.x + self._paddle.width, self._paddle.y)
        paddle_coordinate_lower_right = self.window.get_object_at(self._paddle.x + self._paddle.width, self._paddle.y
                                                                  + self._paddle.height)
        # Exclude the paddle
        if upper_left is not None:
            if upper_left is paddle_coordinate_lower_right or upper_left is paddle_coordinate_upper_right:
                self.__dx = - self.__dx
            else:
                self.window.remove(upper_left)
                self.__brick -= 1
                self.__dy = -self.__dy
        elif lower_left is not None:
            if lower_left is paddle_coordinate_upper_right or lower_left is paddle_coordinate_upper_left:
                self.__dx = -self.__dx
                self.ball.y = self._paddle.y - self.ball.height
                self.__dy = -self.__dy
            if lower_left is paddle_coordinate_lower_right:
                self.__dx = -self.__dx
            else:
                self.window.remove(lower_left)
                self.__brick -= 1
                self.__dy = -self.__dy
        elif upper_right is not None:
            if upper_right is paddle_coordinate_lower_left or upper_right is paddle_coordinate_upper_left:
                self.__dx = - self.__dx
            else:
                self.window.remove(upper_right)
                self.__brick -= 1
                self.__dy = -self.__dy
        elif lower_right is not None:
            if lower_right is paddle_coordinate_upper_left or lower_right is paddle_coordinate_upper_right:
                self.__dx = -self.__dx
                self.ball.y = self._paddle.y - self.ball.height
                self.__dy = -self.__dy
            if lower_right is paddle_coordinate_lower_left:
                self.__dx = -self.__dx
            else:
                self.window.remove(lower_right)
                self.__brick -= 1
                self.__dy = -self.__dy

    # Bounce when hitting the wall
    def hit_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
            self.ball.move(self.__dx, self.__dy)
        if self.ball.y <= 0:
            self.__dy = -self.__dy
            self.ball.move(self.__dx, self.__dy)

