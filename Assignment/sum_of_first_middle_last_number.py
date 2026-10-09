def sum_of_first_middle_last_number(list):
	first_number = list[0]
	last_number = list[-1]
	middle = len(list) // 2
	
	if len(list) % 2 == 0:
		middle_number = (list[middle - 1] + list[middle])/2
	else:
		middle_number = list[middle]
		
	return first_number + middle_number + last_number
	
print(total_of_first_middle_last_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(total_of_first_middle_last_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))	
	
