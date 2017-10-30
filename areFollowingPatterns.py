def areFollowingPatterns(strings, patterns):
	"""
	:strings type: Listof String
	:patterns type: Listof String
	rtype: Boolean
	"""

	dstrings = {}
	dpatterns = {}

	for index in range(len(patterns)):
		if patterns[index] in dpatterns:
			if dpatterns[patterns[index]] != strings[index]:
				return False
		if strings[index] in dstrings:
			if dstrings[strings[index]] != patterns[index]:
				return False
		else:
			dpatterns[patterns[index]] = strings[index]
			dstrings[strings[index]] = patterns[index]

	return True

'''
create a dictionary aka hashtable
[key:value]
strings = pattern --> [strings:pattern] 
ex: ["cat":"a"]

create another dict 
[key:value] --> [pattern:strings]

current index of strings:
check the first d and see the key and match that with the value
otherwise if its not in the d then u add in the entry with the corresponding index of pattern

'''
