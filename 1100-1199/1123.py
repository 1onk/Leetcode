"""
1123.最深叶节点的最近公共祖先
地址：https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/

参考Leetcode 236 二叉树的最近公共祖先
地址：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
实现求两个节点的最近公共祖先

先把所有的最深叶节点求出来，若有多个节点，可以先求两个节点的最近公共祖先，得出的结果再和下一个节点求最近公共祖先，依次类推，得到结果
"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        if not root or (not root.left and not root.right):
            return root
        
        dic = {}
        
        def depth(node, tmp):
            if not node:
                return 
            dic[node] = tmp + 1
            depth(node.left, tmp+1)
            depth(node.right, tmp+1)
        
        depth(root, 0)
        
        #print(dic)
        
        l = []
        max_depth = max(dic.values())
        
        for key, val in dic.items():
            if val == max_depth:
                l.append(key)
        
        #print(l)
        if len(l) == 1:
            return l[0]
        tmpAncestor = l[0]
        for i in range(len(l)-1):
            tmpAncestor = self.lowest(root, tmpAncestor, l[i+1])
        return tmpAncestor
            
    def lowest(self, root, p, q):
        if not root or root == p or root == q:
            return root
        
        left = self.lowest(root.left, p, q)
        right = self.lowest(root.right, p, q)
        
        if left and right:
            return root
        elif left:
            return left
        elif right:
            return right
        else:
            return None