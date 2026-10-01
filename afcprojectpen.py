import turtle
screen=turtle.Screen()
screen.title("Pen project 2")
screen.bgcolor("black")
artist=turtle.Turtle()
artist.speed('fastest')
artist.hideturtle()
artist.pensize(2)
def draw_petal(size,colour):
    artist.color(colour)
    artist.begin_fill()
    for _ in range(2):
        artist.circle(size,120)
        artist.left(60)
    artist.end_fill()
color=["red","orange","yellow","green","blue","indigo","violet"]
for i in range(36):
    draw_petal(90,color[i%len(color)])
    artist.right(10)
artist.penup()
artist.goto(0,-25)
artist.pendown()
artist.color("white")
artist.begin_fill()
artist.circle(25)
artist.end_fill()
turtle.done()