#psuacode
#1.draw one square
#1.1 move forward
#1.2 turn right
#loop 4 times
#2.move another direction
#3.draw another square


import turtle


def draw_square(someone):
    for i in range (1, 5):
        someone.forward(100)
        someone.right(90)

        
def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(4)
    for i in range (1,37):
        draw_square(brad)
        brad.right(10)

    #angie = turtle.Turtle()
    #angie.color("blue")
    #angie.circle(100)
    

    window.exitonclick()


draw_art()
