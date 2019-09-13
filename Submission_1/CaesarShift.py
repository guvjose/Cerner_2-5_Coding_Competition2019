#cerner_2^5_2019

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

##
# Shifts all letters in s by n
# @param s The string to be shifted
# @param n The amount of characters to shift by
# @return A string that is the same as s but with the letters shifted by n
def doCaesarShiftRight(s, n):
	shiftedString = ''
	for char in s:
		if char.isalpha():
			letterPosition = letters.index(char)
			shiftedString += letters[(letterPosition+n)%26]
		else:
			shiftedString += char

	return shiftedString

if __name__ == "__main__":
	s = raw_input("Enter letters (a-z) to be encoded: ")
	n = raw_input("Enter number (0-25) to shift by: ")
	if n.isdigit():
		print doCaesarShiftRight(s.lower(), int(n))
	else:
		print "Invalid number provided"