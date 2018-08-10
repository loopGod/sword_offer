# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n==0:
            return 0
        nstr=''
        for i in range(n+1):
            nstr+=str(i)
        print(nstr)
        nstrlist=sorted(list(map(int,list(nstr))))
        for i,v in enumerate(nstrlist):
            if (v==1 and i==0) or (nstrlist[i-1]<1 and v==1):
                start=i
            if (v==1 and i==len(nstrlist)-1) or v==1 and (nstrlist[i+1]>1):
                end=i+1
        return end-start

mysolu=Solution()
print(mysolu.NumberOf1Between1AndN_Solution(0))   
