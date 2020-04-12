"""
Problem Link : https://leetcode.com/problems/single-number/
"""


class Solution:
    def singleNumber(self, nums):
        if len(nums) == 1: return nums[0]
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]


arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

solution = Solution()
print(solution.singleNumber(arr))
