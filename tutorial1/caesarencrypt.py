"""c=(x-n)%26
c is the cipher text, n is the key
x is the ascii value of the plaintext


"""
def encrypt(text,s): 
	result = "" 
	for i in range(len(text)): 
		char = text[i] 

		# Encrypt uppercase characters 
		if (char.isupper()): 
			result += chr((ord(char) + s-65) % 26 + 65) 

		# Encrypt lowercase characters 
		else: 
			result += chr((ord(char) + s - 97) % 26 + 97) 

	return result 
text = input("enter the text")
s =int(input("enter the shift")) 
print (" The original text is : " + text) 
print ("Shift : " + str(s) )
print ("Ciphertext is: " + encrypt(text,s) )


