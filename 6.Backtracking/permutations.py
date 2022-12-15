# Given an array nums of distinct integers, return all the 
# possible permutations. You can return the answer in any order.
# 46 in leetcode

def backtrack(nums, ans, final_ans):
  if len(nums) == 1:
    ans.append(nums[0])
    final_ans.append(ans)
    return
  for i in range(len(nums)):
    backtrack(nums[:i] + nums[i+1:], ans + [nums[i]], final_ans)
  return final_ans
if __name__ == '__main__':
  nums = [1,2,3]
  res = backtrack(nums, [], [])
  print(res)
  