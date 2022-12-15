# Given an array of distinct integers nums and a target integer target, 
# return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.
# 377 of leetcode

# Using backtrack algorithm. But unfortunately time limit exceeded on this.

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.ans = 0
        self.smallest = min(nums)
        if self.smallest > target:
            return self.ans
        nums.sort() # To make it more efficient
        self.find_combinations(nums, target)
        return self.ans

    def find_combinations(self, nums, target):
        if target != 0 and self.smallest > target:
            return
        if target == 0:
            self.ans += 1
            return
        for each in nums:
            if target >= each:
                self.find_combinations(nums, target - each)
            else:
                break
        return