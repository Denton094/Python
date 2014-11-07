#GEORGE DENTON
#LECTURE 8 - PART 2
#INTEGER DIVISION

from random import randrange
n = 0
while(n < 5):
	try:
		print("INTEGER DIVISION")
		a = randrange(5)
		b = randrange(5)
		ans = input(str(a)+"/"+str(b)+"= ")
		cal = a//b
		if cal == int(ans):
			print("CORRECT!")

		else:
			print("INCORRECT!")
#capture two exceptions: divison by zero or user enter letter
	except ValueError: 
		print("Please enter user a integer")
	except ZeroDivisionError:
		print("Division by zero isnt possible")

	
	n+= 1