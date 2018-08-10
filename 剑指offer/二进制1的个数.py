# -*- coding:utf-8 -*-
print(0b1001 & 0b1101)
class Solution:
    def NumberOf1(self, n):
        return sum([(n>>i & 1) for i in range(0,32)])

        # write code here


mySolu=Solution()

print(mySolu.NumberOf1(4))
