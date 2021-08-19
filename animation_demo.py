import arcade, animation

class AnimationDemo(arcade.Window):
    def __init__(self):
        super().__init__(800, 600, 'Animation Demo')

        arcade.set_background_color(arcade.color.BLACK)

        self.y = 300

        self.colour = arcade.color.GREEN
        self.animations = [
            animation.Animation( # Change colour of box
                [
                    'self.colour = arcade.color.GREEN',
                    'self.colour = arcade.color.YELLOW',
                    'self.colour = arcade.color.RED'
                ],
                20
            ),
            animation.Animation( # Move box up and down
                [
                    'self.y += 5',
                    '_10',     #_ means repeat, the following number is the amount of times repeated
                    'self.y -= 5',
                    '_20',
                    'self.y += 5',
                    '_10'
                ],
                1
            ),
        ]

    def setup(self):
        self.tick = 0

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(300, 300, 100, 100, self.colour)
        arcade.draw_rectangle_filled(500, self.y, 100, 100, (0,255,0))

    def on_update(self, dt):
        self.tick += 1
        for animation in self.animations:
            frame = animation.update(self.tick)
            exec(frame)
    
def main():
    game = AnimationDemo()
    game.setup()
    arcade.run()
main()


