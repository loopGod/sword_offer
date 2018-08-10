class Solution:
    def jumpFloorII(self, number):
        S = [1,2]
        if number == 1:
            return S[0]
        if number == 2: 
            return S[1]
        for i in range(3,number+1):
            S.append(sum(S))
        return S.pop()

mySolu=Solution()

print(mySolu.jumpFloorII(4))
