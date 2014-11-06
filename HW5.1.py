#GEORGE DENTON
#LECTURE 8 - PROGRAM # 1


class Animal(object):

	def __init__(self,hints,type_anim):
		self.hints = hints
		self.type_anim = type_anim

	def hint_to_guess_animal(self):
		print("I will give you 3 hints, guess what animal I am\n")
		n = 0
		
		for line in self.hints:
			n+=1
			print (line)
			user_input = input("Who am I?: ")
			if user_input == self.type_anim:
				print("You got it! I am "+ self.type_anim)
				break
			else:
				print("Nope, try again!")	
		  
		if n==3:
			print("I am out of hints! The answer is:" + self.type_anim)


e = Animal([" I am the largest living animal in the world","I have a trunk","I have very big feet"], "elephant")
e.hint_to_guess_animal()

t = Animal(["I have yellow and black stripes","I am the biggest cat","I also come in black and white"],"tiger")
t.hint_to_guess_animal()


b = Animal(["I can fly","I see well in the dark","I use echo-location"],"bat")
b.hint_to_guess_animal()