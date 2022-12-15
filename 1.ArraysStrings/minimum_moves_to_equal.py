# Given an integer array nums of size n, return the minimum number of moves 
# required to make all array elements equal.
# In one move, you can increment n - 1 elements of the array by 1.
# 453 of leetcode

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Approach:
        # we want to make all the elements equal ; question does not 
        # say "to which element" they should be made equal so that means
        # we can "choose" to what element they all should finally reach
        
        # Choose the minimum element of the array as a starting point
        # because the statement says - 
        # we can increment all elements except one element 
        # which can be interpreted as "decreasing that one element" in each
        # move to make all the elements equal
        
        # for eg: 
        # [1,2,3] -> [1,1,3] -> [1,1,2] -> [1,1,1]
        # at each step, we decrement one element towards the smallest
        _min = min(nums)
        ans = 0
        
        # if all elements are already equal; ans = 0
        if all(ele == nums[0] for ele in nums):
            return 0
        else:
            for ele in nums:
                ans = ans + (ele - _min)
                # ele - _min because it takes ele - _min steps to make ele 
                # equal to the minimum element
            return ans
