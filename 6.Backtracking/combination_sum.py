# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the 
# chosen numbers is different. It is guaranteed that the number of 
# unique combinations that sum up to target is less than 150 combinations 
# for the given input.
# 39 leetcode

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = self.backtrack(candidates, target, [], [])
        return res
    
    def backtrack(self, candidates, target, comb, final_res):
        i = 0
        while(i < len(candidates) and target >= candidates[i]):
            if target ==  candidates[i]:
                comb.append(candidates[i])
                final_res.append(comb)
                return final_res
            else:
                self.backtrack(candidates[i:], target - candidates[i], comb + [candidates[i]], final_res)
            i += 1
        return final_res