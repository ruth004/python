celsus = float(input("Enter a temperature in celsus"))

for number in range(5):
	temperature = celsus + number
	if temperature < -273:
		print(temperature, "c is not impossible")
	else:
		farenheit = (temperature * 9/5) + 32
		print(temperature, "c")
