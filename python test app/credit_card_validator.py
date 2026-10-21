def get_card_type(card_number):
    if card_number[0] == "4":
	    return "Visa Card"
    elif card_number[0] == "5":
	    return "Master Card"
    elif card_number[0] == "3" and card_number[1] == "7":
	    return "American Express Card"
    elif card_number[0] == "6":
	    return "Discover Card"
    else:
        return "unknown card"
	    
	    
def cardValidation(creditNumber):
    text = str(creditNumber)
    value = []
    digit = 0
    total = 0
    for num in range(len(text)-1, -1, -1):
        value.append(int(text[num])) 
		    
    for index in range(len(value)):
        if index % 2 == 1:
            digit = value[index] *2
        if digit > 9:
            remainder = digit % 10
            digit = digit / 10
            #value[index] = digit
            total = total + remainder
            
            if total % 10 == 0:
                return "valid card"
            else:
                return "invalid card"
	                

def len_Of_Digit( userInput):
    user = str(userInput);
    return len(user);


def  check_Card_Len( card):
    userInput = str(card)
    if len(userInput) >= 13 and len(userInput) <= 16:
        return True
    else: 
        return False


def  get_Card_Type( number):
    cardType = "";
    value = str(number)
    if value[0] == "4":
        cardType = "Visa Card"
    elif value[0] == "5":
        cardType = "Master Card"
    elif value[0] == "3" and value[1] == "7": 
        cardType = "American Express Card"
    elif value[0] == "6":
        cardType = "Discover card";
    else:
        cardType = "unknown card"
        
    return cardType

	
	
