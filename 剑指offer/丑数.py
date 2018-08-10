# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index==0:
            return 0
        listedugl=[1,2,3,4,5]
        if index<6:
            return listedugl[index-1]
        for i in range(index-5):
            tmp=[]
            for num in listedugl:
                if 2*num>listedugl[-1]:
                    tmp.append(2*num)
                if 3*num>listedugl[-1]:
                    tmp.append(3*num)
                if 5*num>listedugl[-1]:
                    tmp.append(5*num)
            listedugl.append(sorted(tmp)[0])
        return listedugl[-1]

mysolu=Solution()
print(mysolu.GetUglyNumber_Solution(7))   
