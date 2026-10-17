def get_card_type(card_number):
	if card_number[0] == "4":
		return "Visa Card"
	elif card_number[0] == "5":
		return "Master Card"
	elif card_number[0] == "3" and card_number[1] == "7":
		return "American Express Card"
	elif card_number[0] == "6":
		return "Discover Card"
		
		
def cardValidation(creditNumber){
	number = number + creditNumber;
	value = []
	while creditNumber < 0:
			remainder = creditNumber % 10;
	        creditNumber = creditNumber / 10;
	        if remainder > 9:
	            lastDigit = remainder % 10;
	            remainder = remainder / 10;
	            remainder += lastDigit;
		        value.append(remainder)
		        
	 sumOfNumbers = 0;
	for i in range(len(value)):
	    sumOfNumbers +=i	
	
	 sumOfOddNumbers = 0;
	for i in range(len(value)):
	    if i % 2 != 0: 
	        sumOfOddNumbers += i
	
	total = sumOfNumbers + sumOfOddNumbers
	
    if total % 10 == 0:
	    return "valid card"
	else: 
	    return "invalid card"
	
	def len_Of_Digit(long userInput){
	 input = "" + userInput;
  return input.len(self);
	
	
	def  check_Card_Len(long userInput){
   value = "" + userInput;
  if i in range value.len() >= 13 && value.length() <= 16)
  return true;
  else 
  return false;
  
	
	
	def  get_Card_Type( creditNumber)
		number =  + creditNumber;
    value [] = [number.len(value)];
	for num in range = 0; num < value.length; 
	    remainder = creditNumber % 10;
	creditNumber = creditNumber / 10;
	if remainder > 9
	lastDigit = remainder % 10;
	remainder = remainder / 10;
	remainder += lastDigit;
	
	value[count] = remainder;
	
	cardType = "";
	    if value[0] == 4
	cardType = "Visa Card";
	 elif 
	    if value[0] == 5
	cardType = "Master Card";
	 elif
	    if value[0] == 3 & value[1] == 7 
	    cardType = "American Express Card";
	 else 
	    if value[0] == 6
	cardType = "Discover card";
	
	return cardType;
	
	
	
