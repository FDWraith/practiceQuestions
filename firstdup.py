import copy

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
	nonrepeats = []
	seen = set()

	for char in s:
		if char not in seen:
			nonrepeats.append(char)
			seen.add(char)
		elif char in nonrepeats:
			nonrepeats.remove(char)
	return nonrepeats[0]
	

print firstNotRepeatingChar("hello")
print firstNotRepeatingChar("woah")
print firstNotRepeatingChar("gaggggggg")
print firstNotRepeatingChar("bcb")

def rotateImage(a):
	acopy = copy.deepcopy(a)

	# 0, 0 -> 0, 2
	# 0, 1 -> 1, 2
	# 0, 2 -> 2, 2
	# 1, 0 -> 0, 1
	# 1, 1 -> 1, 1
	# 1, 2 -> 2, 1
	# 2, 0 -> 0, 0
	# 2, 1 -> 1, 0
	# 2, 2 -> 2, 0

	for row in range(len(a)):
		for col in range(len(a[row])):
			acopy[col][len(a[row])-row-1] = a[row][col]

	return acopy


nA = [ [1,2,3], 
       [4,5,6],
       [7,8,9] ]
nB = [ [7,4,1],
       [8,5,2],
       [9,6,3] ]
print rotateImage(nA)
print rotateImage(nB)


def removeKFromList(l,k):

	head = l
	while( head.next != None):
		nextNode = head.next
		if nextNode.value == k:
			head.next = nextNode.next
		else:
			head = nextNode
	if l.value == k:
		return l.next
	else:
		return l

