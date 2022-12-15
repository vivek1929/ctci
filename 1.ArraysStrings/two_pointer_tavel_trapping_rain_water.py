# 42 Given n non-negative integers representing an elevation map 
# where the width of each bar is 1, compute how much water 
# it can trap after raining.
# https://leetcode.com/problems/trapping-rain-water/solution/ Approach 4


import sys


def area_trapping_rain_water(heights):
  area = 0
  left = 0
  right = len(heights) - 1
  left_max = -sys.maxsize - 1
  right_max = -sys.maxsize - 1

  while (left < right):
    if heights[left] < heights[right]:
      if heights[left] > left_max:
        left_max = heights[left]
      else:
        area += (left_max - heights[left])
      left += 1
    else:
      if heights[right] > right_max:
        right_max = heights[right]
      else:
        area += (right_max - heights[right])
      right -= 1
  return area


if __name__ == '__main__':
  height = [0,1,0,2,1,0,1,3,2,1,2,1]
  # height = [4,2,0,3,2,5]
  area = area_trapping_rain_water(height)
  print(area)