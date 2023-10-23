from turtle import Turtle, Screen
from random import randint

# Set up the screen
window = Screen()
window.title("Catch the Turtle Game")
window.bgcolor("light green")
# window.bgpic("grass.png") # If you want you can add background picture to the game

# Set default font type for project.
FONT = ("Arial", 24, "normal")

# Create game_over variable to determine game is over or not
game_over = False

# Set top_height of screen to design a responsive game
top_height = window.window_height() / 2 # We divide 2 because the turtle starts on the center of the screen as default

# Create the Moving Turtle
main_turtle = Turtle()
def setup_main_turtle():
    main_turtle.shape("turtle") # Set shape the turtle
    main_turtle.color("black") # Set outline of the turtle
    main_turtle.fillcolor("green") # Set inside color of the turtle
    main_turtle.penup() # penup() for deleting the moving lines of turtle
    main_turtle.speed(0) # Set fastest speed to appear on the screen quickly
    main_turtle.shapesize(2) # Set size of the turtle

# Create the Scoreboard Turtle
score = 0
scoreboard_turtle = Turtle()
def setup_scoreboard():
    scoreboard_turtle.speed(0)  # Set fastest speed to appear on the screen quickly
    scoreboard_turtle.color("black") # Set scoreboard text color
    scoreboard_turtle.penup() # penup() for deleting the moving lines of turtle
    scoreboard_turtle.hideturtle() # hideturtle() to only see text
    scoreboard_turtle.setposition(0, top_height * 0.8) # Set scoreboard position
    scoreboard_turtle.write("Score: 0", align="center", font=FONT) # Write scoreboard on the screen

# With on_click_update_score function when user click on the turtle score increase 1
def update_score(x, y):
    global score
    if not game_over:
        score += 1 # Increase score
        scoreboard_turtle.clear() # Clear previous scoreboard
        scoreboard_turtle.write(f"Score: {score}", align="center", font=FONT) # Write updated score on the screen

# With onclick function when user click on the turtle we can call on_click_update_score() function
main_turtle.onclick(update_score)  # Default left click

# With move_turtle function the turtle move to a random location.
def move_turtle():
    coordinate_value = int(top_height * 0.75) # Set coordinates value to determine border for turtle moves
    if not game_over:
        x = randint(-coordinate_value, +coordinate_value) # give random x coordinate within coordinate_value
        y = randint(-coordinate_value, +coordinate_value) # give random y coordinate within coordinate_value
        main_turtle.setposition(x, y) # Set turtle position with using x and y
        window.ontimer(move_turtle, 500)  # Use ontimer() to call move_turtle() function every 500 ms
    else:
        main_turtle.hideturtle() # Hide turtle when game is over

# Create Countdown Timer
countdown_turtle = Turtle()
def setup_countdown_timer():
    countdown_turtle.speed(0) # Set fastest speed to appear on the screen quickly
    countdown_turtle.color("black") # Set countdown text color
    countdown_turtle.penup() # penup() for deleting the moving lines of turtle
    countdown_turtle.hideturtle() # hideturtle() to only see the text
    countdown_turtle.goto(0, top_height * 0.9) # Set countdown timer position

# Function to update the countdown timer
def start_countdown_timer(second):
    global game_over

    if second > 0:
        countdown_turtle.clear() # Clear previous time
        countdown_turtle.write(f"Time: {second}", align="center", font=FONT) # Write down the remaining time
        window.ontimer(lambda: start_countdown_timer(second-1),1000) # Call same function every 1 second = 1000 ms
    else:
        countdown_turtle.clear() # Clear time text
        countdown_turtle.write(f"GAME OVER!", align="center", font=FONT) # Write down GAME OVER when second = 0
        game_over = True # Return game_over variable True to approve game is finished.

# Collect all functions to start game in one function
def start_game():
    setup_main_turtle()
    setup_scoreboard()
    setup_countdown_timer()
    move_turtle()
    start_countdown_timer(10) # Set countdown timer to 10 second
    window.mainloop() # Main game loop

# Start Game
start_game()