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
from campy.graphics.gimage import GImage

import random


BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 11  # Radius of the ball (in pixels).
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
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle_offset = paddle_offset
        self._paddle = GRect(self.paddle_width, self.paddle_height)
        self._paddle.filled = True
        self._paddle.fill_color = self.random_color()   # The paddle color will change for each round.
        self.window.add(self._paddle, (self.window_width - paddle_width) / 2, self.window_height - paddle_offset)

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.set_ball()

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmouseclicked(self.play)
        onmousemoved(self.paddle_move)

        # Draw bricks
        self.draw_bricks()

        # Set four probes on four corners of ball to detect object
        self.upper_left = self.window.get_object_at(self.ball.x, self.ball.y)
        self.lower_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.upper_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.lower_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.height)
        self.middle_bottom = self.window.get_object_at(self.ball.x+self.ball.width/2, self.ball.y + self.ball.height)

        # Set four probes on four corners of paddle to detect object
        self.paddle_coordinate_upper_left = self.window.get_object_at(self._paddle.x, self._paddle.y)
        self.paddle_coordinate_lower_left = \
            self.window.get_object_at(self._paddle.x, self._paddle.y + self._paddle.height)
        self.paddle_coordinate_upper_right = \
            self.window.get_object_at(self._paddle.x + self._paddle.width, self._paddle.y)
        self.paddle_coordinate_lower_right = \
            self.window.get_object_at(self._paddle.x + self._paddle.width, self._paddle.y + self._paddle.height)

        # Count bricks
        self.__brick = self.brick_cols * self.brick_rows
        self.__score = 0
        self.__score_count = GLabel('Score: ' + str(self.__score), x=0, y=self.window_height)
        self.__score_count.font = '-15-bold'
        self.window.add(self.__score_count)

        # Life board
        self.__live = 0
        self.live_count = GLabel('Life: ', x=self.window_width-135, y=self.window_height)
        self.live_count.font = '-15-bold'
        self.window.add(self.live_count)
        self.heart1 = GImage("heart.png")
        self.heart2 = GImage("heart.png")
        self.heart3 = GImage("heart.png")
        self.show_life()

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
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
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

    # getter of score
    def get_score_count(self):
        return self.__score_count

    # Getter of __dx
    def get_dx(self):
        return self.__dx

    # Getter of __dy
    def get_dy(self):
        return self.__dy

    # Show the scores on the window
    def show_scores(self):
        self.__score_count.text = 'Score: ' + str(self.__score)

    # Show the lives on the window
    def show_life(self):
        self.window.add(self.heart1, x=self.window.width-self.heart1.width-68, y=self.window.height-self.heart1.height)
        self.window.add(self.heart2, x=self.window.width-self.heart2.width-40, y=self.window.height-self.heart2.height)
        self.window.add(self.heart3, x=self.window.width-self.heart3.width-12, y=self.window.height-self.heart3.height)

    # When the ball reach the bottom, minus one life.
    def remove_life(self):
        """
        This function will remove the life imgs on window.
        """
        if self.ball.y + self.ball.height >= self.window.height:
            self.__live += 1
            if self.__live == 1:
                self.window.remove(self.heart3)
                self.window.remove(self._paddle)
                self._paddle = GRect(self.paddle_width*2, self.paddle_height)
                self.window.add(self._paddle, (self.window_width - self.paddle_width) / 2,
                                self.window_height - self.paddle_offset)
            elif self.__live == 2:
                self.window.remove(self.heart2)
                self.window.remove(self._paddle)
                self._paddle = GRect(self.paddle_width*5, self.paddle_height)
                self.window.add(self._paddle, (self.window_width - self.paddle_width) / 2,
                                self.window_height - self.paddle_offset)
            elif self.__live == 3:
                self.window.remove(self.heart1)

    # Mouseclick function
    def play(self, event):
        if self.ball.x == (self.window.width - self.ball.width * 2) / 2 \
                and self.ball.y == (self.window.height - self.ball.height * 2) / 2:
            self.__dx = random.randint(1, MAX_X_SPEED)
            self.__dy = INITIAL_Y_SPEED
            if random.random() > 0.5:
                self.__dx = -self.__dx

    # Paddle tracker
    def paddle_move(self, event):
        if event.x <= self._paddle.width / 2:
            self._paddle.x = 0
        elif event.x >= self.window.width - self._paddle.width / 2:
            self._paddle.x = self.window.width - self._paddle.width
        else:
            self._paddle.x = event.x - self._paddle.width / 2

    # Check if the ball hit any object
    def probe_check(self):
        # Set four probes on four corners of ball to detect object
        self.upper_left = self.window.get_object_at(self.ball.x, self.ball.y)
        self.lower_left = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.upper_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.lower_right = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.height)
        self.middle_bottom = self.window.get_object_at(self.ball.x + self.ball.width/2, self.ball.y + self.ball.height)

        # Set four probes on four corners of paddle to detect object
        self.paddle_coordinate_upper_left = self.window.get_object_at(self._paddle.x, self._paddle.y)
        self.paddle_coordinate_lower_left = \
            self.window.get_object_at(self._paddle.x, self._paddle.y + self._paddle.height)
        self.paddle_coordinate_upper_right = \
            self.window.get_object_at(self._paddle.x + self._paddle.width, self._paddle.y)
        self.paddle_coordinate_lower_right = \
            self.window.get_object_at(self._paddle.x + self._paddle.width, self._paddle.y + self._paddle.height)

        # Exclude the paddle, scoreboard, and life board(including heart imgs)
        if self.upper_left is not None \
                and self.upper_left is not self.__score_count \
                and self.upper_left is not self.live_count\
                and self.upper_left is not self.heart3 \
                and self.upper_left is not self.heart2 \
                and self.upper_left is not self.heart1:
            if self.upper_left is self.paddle_coordinate_lower_right \
                    or self.upper_left is self.paddle_coordinate_upper_right:
                self.__dx = - self.__dx
            else:
                self.window.remove(self.upper_left)
                self.__brick -= 1
                self.__score += random.randint(1, 10)   # Plus random scores
                self.__dy = -self.__dy
        elif self.lower_left is not None \
                and self.lower_left is not self.__score_count \
                and self.lower_left is not self.live_count\
                and self.lower_left is not self.heart3 \
                and self.lower_left is not self.heart2 \
                and self.lower_left is not self.heart1:
            if self.lower_left is self.paddle_coordinate_upper_right \
                    or self.lower_left is self.paddle_coordinate_upper_left:
                self.__dx = -self.__dx
                self.ball.y = self._paddle.y - self.ball.height
                self.__dy = -self.__dy
            if self.lower_left is self.paddle_coordinate_lower_right:
                self.__dx = -self.__dx
            else:
                self.window.remove(self.lower_left)
                self.__brick -= 1
                self.__score += random.randint(1, 10)   # Plus random scores
                self.__dy = -self.__dy
        elif self.upper_right is not None \
                and self.upper_right is not self.__score_count \
                and self.upper_right is not self.live_count\
                and self.upper_right is not self.heart3 \
                and self.upper_right is not self.heart2 \
                and self.upper_right is not self.heart1:
            if self.upper_right is self.paddle_coordinate_lower_left \
                    or self.upper_right is self.paddle_coordinate_upper_left:
                self.__dx = - self.__dx
            else:
                self.window.remove(self.upper_right)
                self.__brick -= 1
                self.__score += random.randint(1, 10)   # Plus random scores
                self.__dy = -self.__dy
        elif self.lower_right is not None \
                and self.lower_right is not self.__score_count \
                and self.lower_left is not self.live_count\
                and self.lower_left is not self.heart3 \
                and self.lower_left is not self.heart2 \
                and self.lower_left is not self.heart1:
            if self.lower_right is self.paddle_coordinate_upper_left \
                    or self.lower_right is self.paddle_coordinate_upper_right:
                self.__dx = -self.__dx
                self.ball.y = self._paddle.y-self.ball.height
                self.__dy = -self.__dy
            if self.lower_right is self.paddle_coordinate_lower_left:
                self.__dx = -self.__dx
            else:
                self.window.remove(self.lower_right)
                self.__brick -= 1
                self.__score += random.randint(1, 10)
                self.__dy = -self.__dy
        elif self.middle_bottom is not None:
            # If the ball hit the paddle rims, the ball will slightly speed up.
            if self.middle_bottom is self.paddle_coordinate_upper_left \
                    or self.middle_bottom is self.paddle_coordinate_upper_right:
                self.__dx = -self.__dx * 1.05
                self.ball.y = self._paddle.y - self.ball.height
                self.__dy = -self.__dy * 1.05

    # Bounce when hitting the wall
    def hit_wall(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self.__dx = -self.__dx
            self.ball.move(self.__dx, self.__dy)
        if self.ball.y <= 0:
            self.__dy = -self.__dy
            self.ball.move(self.__dx, self.__dy)

    # Case of win
    def win(self):
        win = GLabel('You win!\nThx for playing:-)!')
        win.font = '-18-bold'
        if self.__brick == 0:
            self.window.add(win, x=self.window.width/3, y=self.window.height/1.75)

    # Case of lose
    def lose(self):
        lose = GLabel('You lose :-(!')
        lose.font = '-18-bold'
        if self.__live == 3:
            self.window.add(lose, x=self.window.width/3, y=self.window.height/1.75)

    @staticmethod
    def random_color():
        """
        This function will be used to change the color of balls and paddle.
        :return: str, different colors.
        """
        num = random.choice(range(10))
        if num == 0:
            return 'red'
        if num == 1:
            return 'blue'
        if num == 2:
            return 'green'
        if num == 3:
            return 'slategray'
        if num == 4:
            return 'navy'
        if num == 5:
            return 'salmon'
        if num == 6:
            return 'yellow'
        if num == 7:
            return 'lightblue'
        if num == 8:
            return 'ivory'
        if num == 9:
            return 'rosybrown'
