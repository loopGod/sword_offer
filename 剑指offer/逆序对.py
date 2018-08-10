# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        dp=[0 for i in range(len(data))]
        for i in range(len(data))[::-1][1:len(data)]:
            if data[i]>data[i+1]:
                dp[i]=dp[i+1]+1
            else:
                j=i+1
                while j<len(data):
                    if data[i]>data[j]:
                        dp[i]=dp[j]+1
                        j=len(data)
                    else:
                        j+=1
        return sum(dp)
        # write code here

mysolu=Solution()
print(mysolu.InversePairs([8,1,2,3,4,5,0]))   
'''
# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        dp=[0 for i in range(len(data))]
        for i in range(len(data))[::-1][1:len(data)]:
            if data[i]>data[i+1]:
                dp[i]=dp[i+1]+1
            else:
                j=i+1
                while j<len(data):
                    if data[i]>data[j]:
                        dp[i]=dp[j]+1
                        j=len(data)
                    else:
                        j+=1
        return sum(dp)
        # write code here

mysolu=Solution()
print(mysolu.InversePairs([8,1,2,3,4,5,0]))  
