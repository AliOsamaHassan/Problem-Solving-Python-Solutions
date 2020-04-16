"""
Problem Link: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
"""

class Solution:
    def pivotIndex(self, nums):
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            # total_sum is now the right sum
            total_sum -= num
            if left_sum == total_sum:
                return i
            left_sum += num


        # If no pivot index found, then return -1 
        return -1


arr = list(map(int, input().rstrip().split()))

solution = Solution()
print(solution.pivotIndex(arr))


