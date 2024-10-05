import turtle

# Set up the window

window = turtle.Screen()
window.title("Game Start Menu")
window.bgpic("bg2.gif")
window.setup(width=800, height=600)

# Set up colors
WHITE = "#FFFFFF"
RED = "#FF0000"
# Set up fonts
title_font = ("Arial", 48, "bold")
menu_font = ("Arial", 24, "normal")

# Set up text
title_text = turtle.Turtle()
title_text.color(RED)
title_text.penup()
title_text.goto(0, 90)
title_text.write("BATTLESHIP", align="center", font=title_font)

menu_options = [
    "Start Game",
    "Options",
    "Exit"
]

menu_texts = []
menu_turtles = []

for i, option in enumerate(menu_options):
    text = turtle.Turtle()
    text.color(WHITE)
    text.penup()
    text.goto(0, 10 - i * 50)
    text.write(option, align="center", font=menu_font)
    menu_texts.append(text)
    menu_turtles.append(text)


# Function to handle menu selection
def start_game():
    print("Starting the game...")
    # Add your game code here


def open_options():
    print("Opening options menu...")
    # Add your options menu code here


def exit_game():
    print("Exiting the game...")
    turtle.bye()


# Set up menu click handlers
menu_turtles[0].onclick(start_game)
menu_turtles[1].onclick(open_options)
menu_turtles[2].onclick(exit_game)

turtle.mainloop()
