def add_every_third(list):
	total_of_numbers = 0
	for numbers in list[2: :3]:
		total_of_numbers = total_of_numbers + numbers 
	return total_of_numbers	
		
print(add_third_in_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
	
