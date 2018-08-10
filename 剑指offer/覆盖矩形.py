class Solution:
    def rectCover(self, number):
    	if number == 0:
    		return 0
    	S = [1,2]
    	if number == 1:
    		return S[0]
    	if number == 2:
    		return S[1]
    	for i in range(3,number+1):
    		S.append(S[-1]+S[-2])
    	return S[-1]


mySolu=Solution()

print(mySolu.rectCover(4))
