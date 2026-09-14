from turtle import*
import math

speed(0)
bgcolor("black")
color("blue")
pensize(2)

hideturtle()

for i in range(600):
    t= i / 20

    x = 16 * math.sin(t) ** 3
    y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)

    penup()
    goto(x * 15, y * 15)
    pendown()
    if i%1==0:
        write("Puta" , align="center", font=("Arial", 8, "bold"))

done()
