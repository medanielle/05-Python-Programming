import turtle

turtle.showturtle()

count = 2
while count > 0:
    turtle.penup()
    turtle.forward(100)
    turtle.right(180)
    turtle.pendown()
    turtle.forward(200)
    turtle.right(180)    
    turtle.forward(100)
    turtle.right(90)    
    count -= 1
