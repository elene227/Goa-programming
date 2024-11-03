import turtle

def draw_rectangle(color, x, y, width, height):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill()

def draw_tower(x, y):
    draw_rectangle("gray", x, y, 50, 100)  # Tower
    turtle.fillcolor("darkgray")
    turtle.goto(x + 50, y)
    turtle.goto(x + 50, y + 100)
    turtle.goto(x + 25, y + 125)  # Roof
    turtle.goto(x, y + 100)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_castle():
    turtle.speed(0)  
    
    
    draw_rectangle("lightgray", -200, -100, 400, 100)

    
    draw_tower(-200, 0)
    draw_tower(150, 0)

    
    turtle.fillcolor("blue")
    for x in range(-150, 200, 100):
        draw_rectangle("blue", x, -50, 30, 30)

   
    draw_rectangle("brown", -25, -100, 50, 60)

    turtle.hideturtle()


draw_castle()


turtle.exitonclick()
