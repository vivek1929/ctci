# Given an array of non-negative integers nums, you are 
# initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.
# 45 leetcode


class Solution:
    def jump(self, nums: List[int]) -> int:
        currReach = 0
        reach = 0
        jump = 0 
        for i in range(len(nums)):
            if i > reach:
                return -1
            if i > currReach:
                jump += 1
                currReach = reach
            reach = max(reach, i + nums[i])
        return jump