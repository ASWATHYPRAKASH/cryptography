def decrypt(text,s): 
	result = "" 
	for i in range(len(text)): 
		char = text[i] 

		# Encrypt uppercase characters 
		if (char.isupper()): 
			result += chr((ord(char) - s-65) % 26 + 65) 

		# Encrypt lowercase characters 
		else: 
			result += chr((ord(char) - s - 97) % 26 + 97) 

	return result 
text = input("enter the ciphertext")
s =int(input("enter the shift")) 
print (" The cipher text is : " + text) 
print ("Shift : " + str(s) )
print ("plaintext is: " + decrypt(text,s) )

