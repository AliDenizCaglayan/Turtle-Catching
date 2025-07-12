import turtle
import random

my_screen = turtle.Screen()
my_screen.title("Catch_The_Turtle")
my_screen.bgcolor("light blue")
my_screen.setup(width=700,height=600)

turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_instance.speed(0)
turtle_instance.shapesize(1.5)
turtle_instance.penup()
turtle_instance.shape("turtle")  # bu kod ile tıpkı renkler gibi imleci belirli şekillere değiştirebiliyoruz

turtle_score = turtle.Turtle()
turtle_score.hideturtle()
turtle_score.penup()
turtle_score.speed(0)
turtle_score.goto(0,220)
turtle_score.color("yellow")
FONT = ("Arial", 30, "normal")

turtle_time = turtle.Turtle()
turtle_time.hideturtle()
turtle_time.penup()
turtle_time.speed(0)
turtle_time.goto(0,250)
turtle_time.color("yellow")

turtle_finish = turtle.Turtle()
turtle_finish.hideturtle()
turtle_finish.penup()
turtle_finish.speed(0)
turtle_finish.goto(0,15)
turtle_finish.color("red")

turtle_final_score = turtle.Turtle()
turtle_final_score.hideturtle()
turtle_final_score.penup()
turtle_final_score.speed(0)
turtle_final_score.goto(0,-15)
turtle_final_score.color("green")

time = 30
Score = 0
difficulty = 30.0
game_active = True

def timeDown():
    global time
    if time > 0 and game_active:
        turtle_time.clear()
        turtle_time.write(f"Time:{time}", align="center", font=FONT)
        turtle_score.clear()
        turtle_score.write(f"Score:{Score}", align="center", font=FONT)
        time -= 1
        my_screen.ontimer(timeDown, 1000)

timeDown()

def turtle_apper():
    global difficulty
    if difficulty > 0:
        numX = random.choice(range(-325, 326))
        numY = random.choice(range(-275, 216))
        num = random.choice(range(1, 37))
        turtle_instance.right(10 * num)
        turtle_instance.goto(numX, numY)

        difficulty -= 0.6
        my_screen.ontimer(turtle_apper, 600)  # 0.5 saniye sonra kendini tekrar çağır
    else:
        global game_active
        game_active = False
        turtle_time.clear()
        turtle_score.clear()
        turtle_instance.hideturtle()
        turtle_finish.write("Time Finish", align= "center", font=FONT)
        turtle_final_score.write(f"Your Score:{Score}",align= "center", font=FONT)

turtle_apper()  # ilk çağrı başlatılır

def click_turtle(x,y):
    global Score
    if difficulty > 0:
        Score += 1

my_screen.listen()
turtle_instance.onclick(click_turtle)

my_screen.mainloop()
