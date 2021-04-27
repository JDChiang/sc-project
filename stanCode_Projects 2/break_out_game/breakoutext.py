"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Name: Jo-Di(Frank), Chiang
"""

from campy.gui.events.timer import pause
from breakoutgraphicsext import BreakoutGraphics

FRAME_RATE = 1000 / 100  # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    frame_rate = FRAME_RATE
    if lives > 0:
        while True:     # Add animation loop here!
            frame_rate -= 0.001     # Increase moving speed
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            brick_count = graphics.get_brick_count()
            pause(frame_rate)
            graphics.ball.move(dx, dy)
            graphics.hit_wall()
            graphics.ball.fill_color = graphics.random_color()
            graphics.probe_check()
            graphics.show_scores()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                lives -= 1
                graphics.remove_life()
                graphics._paddle.fill_color = graphics.random_color()
                frame_rate = FRAME_RATE     # Reset to default speed
                if lives == 0:  # When using up 3 attempts, close the game
                    graphics.lose()
                    break
                else:
                    graphics.set_ball()
            if brick_count == 0:    # When no bricks are left, close the game
                graphics.win()
                break


if __name__ == '__main__':
    main()
