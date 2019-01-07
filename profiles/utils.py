# random_string_generator is used to generate a random string from characters and alphabets 

from random import randint

def random_string_generator(max_len):
	rand_string = ''

	for i in range(max_len):
		count = randint(1, 3)
		
		if count == 1:
			ch = chr(randint(48, 57))
		elif count == 2:
			ch = chr(randint(65, 90))
		else:
			ch = chr(randint(97, 122))
		
		rand_string += ch

	return rand_string