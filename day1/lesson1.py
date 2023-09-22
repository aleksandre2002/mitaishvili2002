from turtle import *


width(7)
speed(30)
forward(200)
left(90)

forward(200)
left(90)  

forward(200)
left(90)

forward(200)
left(90)

#end of square

#draw a door
begin_fill()
forward(70)
color("green")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

begin_fill()
color("blue")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#add window
width(4)
penup()
goto(20,160)
pendown()

begin_fill()
color("red")
left(30)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


penup()
goto(180, 160)
pendown()

begin_fill()
color("red")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()



exitonclick()