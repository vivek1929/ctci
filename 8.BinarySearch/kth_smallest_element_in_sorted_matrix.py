# Given an n x n matrix where each of the rows and columns is sorted in 
# ascending order, return the kth smallest element in the matrix.
# Note that it is the kth smallest element in the sorted order, 
# not the kth distinct element.
# You must find a solution with a memory complexity better than O(n2).
# 378 of leetcode


class Solution:
    def kthSmallest(self, matrix,k):
        l, i, N = matrix[0][0], matrix[-1][-1], len(matrix)
        
        def less_k(m):
            count = 0 # count
            for i in range(N):
                # binary search 
                x = bisect_right(matrix[i], m) #bisect
                count = count + x
            return count
        
        while l<i:
            mid = (l+i) // 2
            
            if less_k(mid) < k:
                l = mid + 1
            else:
                i = mid
        return l 
