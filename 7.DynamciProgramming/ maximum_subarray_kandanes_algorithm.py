# Write an efficient program to find the sum of contiguous subarray 
# within a one-dimensional array of numbers that has the largest sum.

# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d
# local_maximum at index i is the maximum of A[i] and the sum of A[i] 
# and local_maximum at index i-1.


import sys

def maxContiguousSubArray(arr):
  max_so_far = -sys.maxsize -1
  local_max = 0
  
  for i in range(len(arr)):
    local_max = max(arr[i], local_max + arr[i])
    if max_so_far < local_max:
      max_so_far = local_max
  return max_so_far

def maxContiguousSubArrayIndexes(arr):
  max_so_far = -sys.maxsize -1
  local_max = 0
  start  = end  = 0
  for i in range(len(arr)):
    local_max = max(arr[i], local_max + arr[i])
    if local_max == arr[i]:
      start = i
    if max_so_far < local_max:
      max_so_far = local_max
      end = i
  return (max_so_far, start, end)

if __name__ == '__main__':
  input_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
  max1 = maxContiguousSubArray(input_array)
  max2, i, j = maxContiguousSubArrayIndexes(input_array)
  print(max2)
  print(i, j)