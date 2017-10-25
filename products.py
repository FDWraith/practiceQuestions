# Problem Statement:
# You have a list of integers, and for each index you want to
# find the product of every integer except for the integer at
# that index


# [Listof Integer] -> [Listof Integer]
# For each index, computes the product of all other integers
# Examples:
# Given: [1, 7, 3, 4]
# Expect: [7*3*4, 1*3*4, 1*7*4, 1*7*3] or [84,12,28,21]
# Note: Cannot use Division
def get_products_of_all_ints_except_at_index(l):

	endList = []
	
	for index in range(len(l)):
		if index == 0:
			endList.append(product(l[index+1:len(l)]))
		else:
			endList.append(product(l[0:index]) * product(l[index+1:len(l)]))
	return endList



# [Listof Integer] -> Integer
# computes the product of all integers in list
def product(l):
	prod = 1
	for i in range(len(l)):
		prod *= l[i]
	return prod





print get_products_of_all_ints_except_at_index([1,7,3,4])
print get_products_of_all_ints_except_at_index([1,0,3,4])
