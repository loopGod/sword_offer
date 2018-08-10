# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        if ss=='':
            return []
        reslist=[]
        ss=list(ss)
        return list(set(self.ddd(ss,0,reslist)))
        # write code here
    
    def ddd(self, ss, i, reslist):
        if i>=len(ss):
            reslist.append(''.join(ss))
        for j in range(i,len(ss)):
            ss[j],ss[i]=ss[i],ss[j]
            self.ddd(ss,i+1, reslist)
            ss[j],ss[i]=ss[i],ss[j]
        return reslist
mysolu=Solution()
print(mysolu.Permutation('abb'))   
print(sorted(['abb', 'bab', 'bba']))