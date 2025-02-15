import turtle
import pandas
states_found = []
score = 0
screen = turtle.Screen()
screen.title("U.S. Name Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
states = pandas.read_csv("50_states.csv")
game_on =True
while game_on and score < 50:
    guess = screen.textinput(title=f"Guess a State: {score}/50",
                                   prompt="Don't you know the name of another state? ").title()
    if not guess:
        game_on = False
    if guess in states["state"].values and guess not in states_found:
        states_found.append(guess)
        score += 1
        state_info = states[states["state"] == guess]
        x, y= int(state_info["x"]), int(state_info["y"])
        writer.goto(x, y)
        writer.write(guess, align="center", font=("Arial", 10, "normal"))
if score == 50:
    writer.goto(0,0)
    writer.write("Congrats you're actually smart!", align="center", font=("Arial", 24, "bold"))
screen.mainloop()
screen.exitonclick()