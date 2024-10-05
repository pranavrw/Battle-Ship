import turtle
import random
import winsound

# Set up screen
wn = turtle.Screen()
wn.setup(800, 600)
wn.bgcolor("black")
wn.title("Space Shooting ")
wn.tracer(0)

# Register shapes (images)
images = ["player.gif", "enemy.gif", "boss.gif", "missile.gif",
          "red_star.gif", "white_star.gif", "yellow_star.gif"]
for image in images:
    wn.register_shape(image)


# Create classes
# Pen class for rendering Health Meters, Ammo Counter, and Score
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("green")
        self.width(2)
        self.speed(0)
        self.setheading(0)

    def health_meter(self):
        if player:
            self.goto(player.xcor() - 20, player.ycor() + 15)
            self.pendown()
            self.fd(40 * (player.health / player.max_health))
            self.penup()
            self.hideturtle()

        if enemies:
            self.goto(enemy.xcor() - 15, enemy.ycor() + 15)
            self.pendown()
            self.fd(30 * (enemy.health / enemy.max_health))
            self.penup()
            self.hideturtle()

    def ammo_counter(self):
        ammo = 0
        for missile in missiles:
            if missile.state == "ready":
                ammo += 1

            for x in range(ammo):
                self.goto(300 + 30 * x, 280)
                self.shape("missile.gif")
                self.stamp()

    def draw_score(self):
        self.goto(-80, 270)
        self.write(f"Score: {player.score}  Kills: {player.kills}", font=("Comic sans", 16, "normal"))
        