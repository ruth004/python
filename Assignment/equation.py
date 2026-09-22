firstNumber = int(input("Enter first number"))
secondNumber = int(input("Enter second number"))
thirdNumber = int(input("Enter third number"))
fourthNumber = int(input("Enter last number"))

if firstNumber > secondNumber:
	firstNumber, secondNumber = secondNumber, firstNumber
	
if secondNumber > thirdNumber:
	secondNumber, thirdNumber = thirdNumber, secondNumber
	
if thirdNumber > fourthNumber :
	thirdNumber, fourthNumber = fourthNumber, thirdNumber
	
if secondNumber > thirdNumber :
    secondNumber, thirdNumber = thirdNumber, secondNumber
    
if thirdNumber > fourthNumber:
    thirdNumber, fourthNumber = fourthNumber, thirdNumber
    
if thirdNumber > fourthNumber:
    thirdNumber, fourthNumber = fourthNumber, thirdNumber
    
print(secondNumber + thirdNumber)/ secondNumber) )  


print ( firstNumber + secondNumber + thirdNumber + fourthNumber)

result = firstNumber + secondNumber + thirdNumber + fourthNumber / 4
print(result)



	
