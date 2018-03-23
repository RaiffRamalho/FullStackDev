import turtle

def draw_shapes():
	window = turtle.Screen()
	window.bgcolor("red")
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("yellow")
	brad.speed("slow")
	for i in range(1,5):
		draw_square(brad)
		brad.right(10)
		
	draw_circle()
	window.exitonclick()



def draw_square(turt):
	for i in range(1,37):	
		turt.forward(100)
		turt.right(90)

def draw_circle():
	sam = turtle.Turtle()
	sam.shape("arrow")
	sam.color("green")
	sam.circle(100)

	
draw_shapes()