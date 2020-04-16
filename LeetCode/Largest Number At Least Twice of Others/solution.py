"""
Problem Link: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
"""

class Solution:
    def dominantIndex(self, nums):
        largest_num = max(nums)
        if all(largest_num >= 2*num for num in nums if num != largest_num):
            return nums.index(largest_num)
        return -1

arr = list(map(int, input().rstrip().split()))

solution = Solution()
print(solution.dominantIndex(arr))
