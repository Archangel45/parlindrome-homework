import string

def remove_punctuation(text):
	# List all the punctuations. I included the escape sequences, too. ;)
	punctuations = string.punctuation + '\n\t '
	
	# The string to produce to have no punctuations. :D
	no_punc = text
	
	# A for loop for all punctuation checks.
	for find_punc in punctuations:
		# If one of our punctuations are found in this string, we take it off.
		if find_punc in no_punc:
			no_punc = no_punc.replace(find_punc, '')
		
	return no_punc
	
def reverse(text):
	# Reverse the text string parameter.
	return remove_punctuation(text[::-1]).lower()
	
def is_palindrome(text):
	return text == reverse(text)
	
something = remove_punctuation(input("Enter text: ")).lower()

# DEBUG
# print('String A:', something, 'String B:', reverse(something))

# If two of the strings are palindromes.
if is_palindrome(something):
	print("Yes, it is a palindrome.")
else:
	print("No, it is not a palindrome.")
