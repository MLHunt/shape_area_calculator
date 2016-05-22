import math 

def shape_calc():

	shape = raw_input("Choose a shape to calculate it's area: enter C for circle, S for square, T for triangle. Alternatively enter Q to quit: ")

	if shape == "C":
		radius = float(raw_input("Enter circle radius: ")) 
		area_circle = math.pi * radius ** 2
		print area_circle
		repeat()


	elif shape == "S":
		square_side = float(raw_input("Enter square side length: "))
		area_square = square_side ** 2
		print area_square
		repeat()

	elif shape == "T":
		triangle_base = float(raw_input("Enter triangle base length: "))
		triangle_height = float(raw_input("Enter triangle height: "))
		area_triangle = 0.5 * triangle_height * triangle_base
		print area_triangle
		repeat()

	elif shape == "Q":
		print "Quitting shape calculator"

	else:
		print "Try Again"	
		shape_calc()

def repeat():
	repeat = raw_input("Would you like to run the shape calulator again? Y or N")

	if repeat == "Y":
		shape_calc()

	elif repeat == "N":
		print "Quitting shape calculator"

	else:
		print "Try again"
		repeat()


shape_calc()