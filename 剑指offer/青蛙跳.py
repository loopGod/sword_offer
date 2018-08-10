# -*- coding:utf-8 -*-
class Solution2:
    def jumpFloor(self, number):
        if number < 0:
            return 0
        if number ==0: 
            return 1
        return(self.jumpFloor(number-1) + self.jumpFloor(number-2))

class Solution:
    def jumpFloor(self, number):
        S2 = 2
        S1 = 1
        if number == 1:
            return S1
        if number == 2: 
            return S2
        for i in range(3,number+1):
            tmp = S1
            S1 = S2
            S2 = S1 + tmp
        return S2

mySolu=Solution()

print(mySolu.jumpFloor(4))
