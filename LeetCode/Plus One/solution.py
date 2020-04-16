"""
Problem Link: https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
"""


class Solution:
    def plusOne(self, digits):
        result = int(''.join([str(digit) for digit in digits])) + 1
        return [int(digit) for digit in str(result)]


arr = list(map(int, input().rstrip().split()))

solution = Solution()
print(solution.plusOne(arr))
