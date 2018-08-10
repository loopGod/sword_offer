# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        ks,kd=[],[]
        for i,a in enumerate(array):
            if a%2 == 1:
                ks.append(a)
            else:
                kd.append(a)
        return ks+kd


mySolu=Solution()

print(mySolu.reOrderArray([1,2,3,4,5,6]))

# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1==None:
            return pHead2
        if pHead2==None:
            return pHead1
        root=ListNode(0)
        new=root
        while pHead1 and pHead2:
            if pHead1.val <= pHead.val:
                new.val=pHead1.val
                tmp=ListNode(0)
                new.next=tmp
                new=new.next
                pHead1=pHead1.next
            else:
                new.val=pHead2.val
                tmp=ListNode(0)
                new.next=tmp
                new=new.next
                pHead2=pHead2.next
        if pHead1=None:
            new.val=pHead2.val
            new.next=pHead2.next
        else:
            new.val=pHead1.val
            new.next=pHead1.next
        return root
