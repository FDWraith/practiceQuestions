#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def isTreeSymmetric(t):
	"""
	:t type: Tree
	rtype: Boolean
	"""

	if t == None:
		return True

	return leftEqualRight(t.left, flipTree(t.right) )

# returns a flipped tree
def flipTree(t):
	"""
	:t type: Tree
	rtype: Tree
	"""

	if t == None:
		return None
	else:
		t1 = flipTree(t.left) 
    	t2 = flipTree(t.right)

    	t.left = t2
    	t.right = t1

    	return t

# determines if t1 is equal to t2
def leftEqualRight(t1, t2):
	"""
	:t1 type: Tree
	:t2 type: Tree
	rtype: Boolean
	"""

	if t1 == None:
		return t2 == None
	else:
		if t2 == None:
			return False

	if t1.value == t2.value:
		return leftEqualRight(t1.left, t2.left) and leftEqualRight(t1.right, t2.right)
	else:
		return False



