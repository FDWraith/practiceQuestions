def firstDuplicate(l1):
	# Initialize an empty set
	s = set()

	# Loop through the given array/list
	for num in l1:
		# For each number, check if already in set
		# (1) If it is, return that number
		# (2) If it isn't, add it to the set
		if num in s:
			return num
		else:
			s.add(num)
	# Reached the end without returning anything
	# Means there are no repeating elements
	# Return -1
	return -1


print firstDuplicate([1,2,3,4,5])
print firstDuplicate([1,2,3,2,3])
print firstDuplicate([1,1,1,1,1])


def firstNotRepeatingChar(s):
	# Init an empty set
	hs = set()

	# Loop through characters in string
	for char in s:
		# For each character, check if already in set
		# (1) If it is, return that char
		# (2) If it isn't, add it to the set
		if char in hs:
			return char
		else:
			hs.add(char)
	# Reached the end without finding a repeating char
	# Means there is no repeating elements
	return "_"


print firstNotRepeatingChar("hello")
print firstNotRepeatingChar("woah")
print firstNotRepeatingChar("gggggggg")