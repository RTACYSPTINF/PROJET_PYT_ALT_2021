import turtle
from CONFIGS import *

print(ZONE_PLAN_MINI)


turtle.setup(480,480,50,50)
turtle.bgcolor("yellow")
turtle.exitonclick()

# tracer une carré colorié 
"""
def trace_carre(x, y, taillek):
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor("red")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(taille)
        turtle.left(-90)
    turtle.penup()
    turtle.end_fill()
    turtle.goto(x,y-taille)

trace_carre(-240,240,30)


for i in range(5):
    trace_carre(-240, 240-i*30, 30)
turtle.mainloop()


"""
