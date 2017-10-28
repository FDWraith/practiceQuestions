# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0 
        # Sum the two and the carry
        s = l1.val + l2.val + carry
        # Find what we have to carry over
        carry = s / 10
        # Find the digit that remains
        r = s % 10
        # change l1 & l2
        l1 = l1.next
        l2 = l2.next

        # generate head
        head = ListNode(r)
        temp = head

        while( l1 != None and l2 != None):
        	# Sum the two and the carry
        	s = l1.val + l2.val + carry
        	# Find what we have to carry over
        	carry = s / 10
        	# Find the digit that remains
        	r = s % 10
        	# change l1 & l2
        	l1 = l1.next
        	l2 = l2.next

        	# Generate a ListNode
        	e = ListNode(r)

        	# Bind the listNode to previous
        	temp.next = e
        	temp = e

		# If one of the two are still not empty,
		# bind it to the list
		# Make sure to add carry to first element tho
		while( l1 != None):
			s = l1.val + carry
			carry = s / 10
			r = s % 10
			l1 = l1.next
			e = ListNode(r)
			temp.next = e
			temp = e

		# Same as above
		while( l2 != None):
			s = l2.val + carry
			carry = s / 10
			r = s % 10
			l2 = l2.next
			e = ListNode(r)
			temp.next = e
			temp = e

		# If Carry is still not zero, but both lists are empty,
		# then generate a new node
		if (carry != 0):
			e = ListNode(carry)
			temp.next = e


        return head

