# -*- coding:utf-8 -*-
class Solution2:
    reslist=[]
    def FindGreatestSumOfSubArray(self, array):
        max_v=array[0]
        for i in range(len(array)):
            for j in range(i,len(array)):
                if sum(array[i:j+1])>max_v:
                    max_v=sum(array[i:j+1])
        return max_v

# -*- coding:utf-8 -*-
class Solution:
    reslist=[]
    def FindGreatestSumOfSubArray(self, array):
        dplist=[array[0]]
        for i in range(1,len(array)):
            if dplist[i-1]>0:
                dplist.append(dplist[i-1]+array[i])
            else:
                dplist.append(array[i])
        return max(dplist)

mysolu=Solution()
print(mysolu.FindGreatestSumOfSubArray([1,2,3]))   
