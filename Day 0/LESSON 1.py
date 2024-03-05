from turtle import * 


#we want to paint a house

#step 1:  drawing a square 
speed(25)
shape("turtle")
width(7)
color("black")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of drawing a square

#drawing a door
begin_fill()
forward(70)
color("red")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()
#end of drawing a door

#drawing a roof 
penup()
goto(200, 200)
pendown()

color("purple")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of drawing a roof

# drawning a window N1

penup()
goto(20, 130)
pendown()


color("black")
right(240)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

penup()
goto(140, 130)
pendown()

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

left(90)
forward(40)

penup()
goto(110, 55)
pendown()

left(90)
forward(5)

penup()
goto(111, 1111)

exitonclick()