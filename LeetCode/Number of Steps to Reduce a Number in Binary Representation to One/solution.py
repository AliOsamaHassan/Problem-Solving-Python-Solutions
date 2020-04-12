"""
Problem Link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/?fbclid=IwAR1lQWakf12PUC32E_Yz8Kadht-Jvw6Vj3zP6qmEMfE7MwWGvs8cSmUDtDg

"""


class Solution:
    def numSteps(self, s):
        int_num = int(s, 2)
        steps_num = 0
        
        if s == '1':
            return steps_num
        
        while int_num != 1:
            steps_num += 1
            if int_num %2 != 0 :
                int_num += 1
            else:
                int_num = int_num // 2
        
        return steps_num


s= "1101"
print("Input: s = \"{}\"".format(s))
solution = Solution()
print("Output: ", solution.numSteps(s))
