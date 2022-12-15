# You are given an integer array nums where the ith bag contains nums[i] balls. 
# You are also given an integer maxOperations.
# You can perform the following operation at most maxOperations times:
# Take any bag of balls and divide it into two new bags with a positive 
# number of balls. For example, a bag of 5 balls can become two new bags 
# of 1 and 4 balls, or two new bags of 2 and 3 balls.
# Your penalty is the maximum number of balls in a bag. 
# You want to minimize your penalty after the operations.
# Return the minimum possible penalty after performing the operations.
# 1760 of leetcode
# https://easyforces.com/solutions/1760/
# Here we know how many operations need on each element to make it k. 
# We will find that k that takes <= max_operations

import math


class Solution:
    def minimumSize(self, nums, maxOperations):
        low = 1
        high = 10 ** 9 + 1
        if self._minOperations(nums, low) <= maxOperations:
            return low

        while high - low > 1:
            mid = (high + low) // 2
            operations = self._minOperations(nums, mid)
            if operations > maxOperations:
                low = mid
            else:
                high = mid
        return high


    def _minOperations(self, nums, k):
        return sum([math.ceil(num / k) - 1 for num in nums])
