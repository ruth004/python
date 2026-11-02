def append_to_tuple():
	my_tuple = (1,2,3)
	new_number = 4
	new_tuple = my_tuple + (new_number,)
	print(new_tuple)
	
def change_nested():
	numbers = ( 1,2,[3,4],5)
	numbers[2][1]= 99
	print(numbers)
	
	 
def tuples_to_list():
	fruits = ('apple', 'banana', 'cherry')
	fruit_list = list(fruits)
	fruit_list.append('mango')
	fruits = tuple(fruit_list)
	print(fruits)
	
	
def unpack_tuple():
	my_tuple = (10,20,30,40)
	a, b, *last =_tuple
	print(a)
	print(b)
	print(last)
