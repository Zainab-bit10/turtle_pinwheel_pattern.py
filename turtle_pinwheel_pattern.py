import turtle
screen = turtle.Screen()
screen.bgcolor('black')  
t = turtle.Turtle()
t.speed(0)  
t.penup()
t.goto(80, 0)
t.pendown()
t.color('cyan')  
for i in range(80):
    if i % 2 == 0:
        t.color('yellow')  
    else:
        t.color('cyan')
    t.circle(50)
    t.forward(100 - i)
    t.left(70)
    t.forward(50)
    t.backward(100)
    t.right(20)
    t.left(30)
    t.forward(100)
    t.dot(6, 'magenta')  
    t.dot(3, 'red')

screen.mainloop()