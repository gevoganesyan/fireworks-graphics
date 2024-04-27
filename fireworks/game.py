from random import randint
from time import sleep
from main import args_parsing
import turtle

from projectiles.rocket import Rocket
from projectiles.spark import Spark

# from main: return tuple of the values (20, 30)
DEFAULT_AMOUNTS_OF_SPARKS = args_parsing()

class Game:

    def __init__(self, def_amount=DEFAULT_AMOUNTS_OF_SPARKS ):
        self.projectiles: list = list()
        self.def_amount = DEFAULT_AMOUNTS_OF_SPARKS

        turtle.setup(800, 600)
        turtle.onkey(self.exit, "Escape")
        turtle.onkey(self.rocket_launch, "space")
        turtle.listen()

        self.window = turtle.Screen()
        self.window.tracer(0)
        self.window.title("Rio fireworks demo animation")
        self.window.bgcolor("#13008D")

        self.draw_text('Press SPACE to firework // Press ESC to close', 0, 250, '#FFFFFF')

    def draw_text(self, text, x, y, fill="black"):
        my_text = turtle.Turtle()
        my_text.speed(0)
        my_text.penup()
        my_text.goto(x, y)
        my_text.color(fill)
        my_text.write(text, align='center', font=('Verdana', 20, 'normal'))
        my_text.hideturtle()

    def animate(self):
        self.window.update()
        if not self.projectiles:
            return
        for item in self.projectiles:
            item.update()
            if not item.is_alive:
                self.kill_projectile(item)

    def run(self):
        while True:
            try:
                self.animate()
            except turtle.Terminator:
                return
            sleep(0.02)

    def rocket_launch(self):
        rocket = Rocket()
        self.projectiles.insert(0, rocket)
    
    def kill_projectile(self, projectile):
        self.projectiles.remove(projectile)
        projectile.kill()
        if projectile.is_rocket:
            self.explode_rocket(projectile)
    
    def explode_rocket(self, rocket):
        coordinates = (rocket.xcor(), rocket.ycor())
        for _ in range(randint(self.def_amount[0], self.def_amount[1])):
            spark = Spark(*coordinates)
            self.projectiles.insert(0, spark)

    def exit(self):
        turtle.bye()
