"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Jo-Di(Frank), Chiang
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 80  # 80 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES   # Record the lives
    if lives > 0:
        while True:     # Add animation loop here!
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            brick_count = graphics.get_brick_count()
            pause(FRAME_RATE)
            graphics.ball.move(dx, dy)
            graphics.hit_wall()
            graphics.probe_check()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                if lives == 0:  # When using up 3 attempts, close the game
                    break
                else:
                    graphics.set_ball()
            if brick_count == 0:    # When no bricks are left, close the game
                break
        graphics.set_ball()


if __name__ == '__main__':
    main()
