# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.res=[]
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        self.getPath( root, expectNumber, 0, '')
        return self.res

    def getPath(self, root, expectNumber, tmp, tmpres):
        tmp+=root.val
        tmpres+=str(root.val)+' '
        if not root.left and not root.right:
            if tmp==expectNumber:
                self.res.append(list(map(int,tmpres.strip().split(' '))))
            return
        if root.left:
            self.getPath(root.left, expectNumber, tmp, tmpres)
        if root.right:
            self.getPath(root.right, expectNumber, tmp, tmpres)
        return
        # write code here

node1=TreeNode(10)
node2=TreeNode(5)
node1.left=node2
node3=TreeNode(12)
node1.right=node3
node4=TreeNode(4)
node2.left=node4
node5=TreeNode(7)
node2.right=node5

mySolu=Solution()
print(mySolu.FindPath(node1, 22))