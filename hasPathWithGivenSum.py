# Defintion for binary tree:
# class Tree(object):
# 	 def __init__(self, x):
# 		 self.value = x
# 		 self.left = None
# 		 self.right = None

def hasPathWithGivenSum(t, s):
	"""
	:type t: Tree
	:type s: Number
	rtype: Boolean
	"""

	if t == None:
		return s == 0

	if t.left == None and t.right == None:
		return t.value == s
		# t.value - s == 0
	else:
		if t.left == None:
			return hasPathWithGivenSum(t.right, s-t.value)
		elif t.right == None:
			return hasPathWithGivenSum(t.left, s-t.value)
		else:
			return hasPathWithGivenSum(t.left, s-t.value) or hasPathWithGivenSum(t.right, s-t.value)
