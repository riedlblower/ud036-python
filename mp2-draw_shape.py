import turtle
import os


def draw_shape():
    os.system("start D:\udacity\ud036-python\circus2.wav")
    window = turtle.Screen()
    window.bgcolor("green")

    frank = turtle.Turtle()
    draw_flower(frank)

#    brad = turtle.Turtle()
#    draw_square(brad)

    michael = turtle.Turtle()
    draw_letters(michael)

    window.exitonclick()
    return

def draw_flower(abc):
# code for flower design
    abc.shape("classic")
    abc.color("blue")
    abc.speed(10)

    abc.pu()            # lift the pen (i.e. no writing)
    abc.setpos(-200,100)  # move turtle left by 200 units
    abc.pd()            # put pen back down (ready for writing)

    for i in range(1,37):  
        abc.left(35)    # rotate turtle left (ac) by 35 degress 
        abc.forward(50) # draw line 50 units long
        abc.right(35)   # rotate turtle right (clockwise) by 35 degress
        abc.forward(50)
        abc.right(145)
        abc.forward(50)
        abc.right(35)
        abc.forward(50)
        abc.right(10)
    abc.seth(270)        # set the turtle pointing south/down
    abc.forward(200)     # draw line 200 units long
    return

def draw_square(brad):
    brad.shape("triangle")
    # "arrow", "turtle", "circle", "square", "triangle", "classic". 
    brad.color("yellow")
    brad.speed(10)
    brad.pu()
    brad.setpos(200,0)
    brad.pd()
    for j in range (0,36):
        for i in range (0,4):
            brad.forward(100)
            brad.right(90)
        brad.right(10)
    return    

def draw_letters(michael):
    michael.shape("classic")
    michael.speed(10)
    michael.seth(90)
    michael.forward(200)
    michael.right(160)
    michael.forward(215)
    michael.left(140)
    michael.forward(215)
    michael.seth(270)
    michael.forward(200)

    michael.pu()
    michael.setpos(200,0)
    michael.pd()
    michael.seth(0)
    michael.forward(150)
    michael.seth(90)
    michael.forward(100)
    michael.seth(180)
    michael.forward(150)
    michael.seth(90)
    michael.forward(100)
    michael.seth(0)
    michael.forward(150)

    return

draw_shape()
