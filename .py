import turtle 
obj=turtle.Turtle()
wn=turtle.screen()
wn.bgcolor("pink")
obj.color("green")
obj.speed(0)
for i in range (120):
      obj.circle(i+8)
      obj.left(30)

turtle.done()
