character = input("Enter a letter").lower()

if len(character) != 1 or not character.isAlphabeth():
	print("invalid input")
else if charcter in "aiou":
	print("vowel")
else:
	print("consonant")
