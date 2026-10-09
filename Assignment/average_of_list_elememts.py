def average_of_list_elememts(list):
	total_of_elements = 0
	for number in list:
		total_of_elements = total_of_elements + number
	average = total_of_elements / len(list)
	return average
	
print(average_of_list_element([1,2,3,4,5,6,7,8,9,10]))
