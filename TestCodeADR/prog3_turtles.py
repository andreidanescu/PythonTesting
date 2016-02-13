import turtle

def drawSquare(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)
    


    
def drawTrig(some_turtle):
    some_turtle.right(60)
    some_turtle.forward(100)
    some_turtle.right(60)
    some_turtle.forward(100)
    some_turtle.right(150)
    some_turtle.forward(170)
        

def drawArt():
    window = turtle.Screen()
    window.bgcolor("red")
        
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    for i in range(1,36):
        #drawSquare(brad)
        brad.circle(100)
        brad.right(10)
    
    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("yellow")
    #angie.speed(5)
    #angie.circle(100)

    #ang = turtle.Turtle()
    #ang.shape("arrow")
    #ang.color("yellow")
    #ang.speed(1.5)
    #drawTrig(ang)

    window.exitonclick()
    
drawArt()
