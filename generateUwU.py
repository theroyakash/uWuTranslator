def generateUwU(input_text): 
	
	length = len(input_text) 
	
	output_text = '' 
	
	for i in range(length): 
		
		current_char = input_text[i] 
		previous_char = '&# 092;&# 048;'
		
		if i > 0: 
			previous_char = input_text[i - 1] 
		
		if current_char == 'L' or current_char == 'R': 
			output_text += 'W'
		
		elif current_char == 'l' or current_char == 'r': 
			output_text += 'w'

		elif current_char == 'O' or current_char == 'o': 
			if previous_char == 'N' or previous_char == 'n' or previous_char == 'M' or previous_char == 'm': 
				output_text += "yo"
			else: 
				output_text += current_char 
		
		else: 
			output_text += current_char 

	return output_text