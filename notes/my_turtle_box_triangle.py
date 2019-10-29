import turtle
        #make turtle pretty
turtle.showturtle()
turtle.pensize(5)
turtle.color('green')
turtle.shape('turtle')
turtle.speed(1)

        #nest while to create each triangle
triangles = 2
while triangles > 0:
    count = 4
    while count > 0: 
        turtle.left(120)
        turtle.forward(100)
        count -= 1
    turtle.left(180)
    #triangles -= 1