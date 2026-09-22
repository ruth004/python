favorite_color = "blue"
	for number in range(3):
		guess = input("Guess your favorite color")
		if guess == favorite_color:
			print("correct!")
		elif guess == "green":
			print("close")
		else:
			print("wrong")
