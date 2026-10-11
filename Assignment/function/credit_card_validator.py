def get_card_type(card_number):
	if card_number[0] == "4":
		return "Visa Card"
	elif card_number[0] == "5":
		return "Master Card"
	elif card_number[0] == "3" and card_number[1] == "7":
		return "American Express Card"
	elif card_number[0] == "6":
		return "Discover Card"
