"""
Problem Link: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/528/week-1/3289/
"""



class Solution:
    def countElements(self, arr):
        counts = 0
        if len(arr) >= 1 and len(arr) <= 1000:
            for i in range(len(arr)):
                if arr[i] >= 0 and arr[i] <= 1000:
                    if arr[i] in arr and int(arr[i]+1) in arr:
                        counts += 1    
        return counts



arr = list(map(int, input().rstrip().split()))

solution = Solution()
print(solution.countElements(arr))


