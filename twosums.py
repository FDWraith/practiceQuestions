class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        """
        # Brute Force Approach
        for n1 in range(len(nums)-1):
        	for n2 in range(n1+1, len(nums)):
        		if nums[n1] + nums[n2] == target:
        			return [n1,n2]
        """

        # One-Pass Hash Method
      	s = {}
      	for num in range(len(nums)):
      		comp = target - nums[num]
      		if comp in s:
      			return [num, s[comp]]
      		else:
      			s[nums[num]] = num 
