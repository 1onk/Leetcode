class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        p = [*range(len(edges) + 1)]      #并查集元素初始化
        def f(x):
            if p[x] != x:       #递归修改所属集合
                p[x] = f(p[x])
            return p[x]
        for x, y in edges:      #遍历边
            px, py = f(x), f(y)
            if px != py:        #检查集合，如果集合不同就合并
                p[py] = px
            else:
                return [x, y]   #集合相同就返回答案

# 利用py集合特性也可以做并查集，本质上没有区别，不过不用递归了。
#
# class Solution:
#     def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
#         p = {i: {i} for i in range(1, len(edges) + 1)}  #并查集初始化
#         for x, y in edges:
#             if p[x] is not p[y]:    #如果两个集合地址不一样
#                 p[x] |= p[y]        #合并集合
#                 for z in p[y]:
#                     p[z] = p[x]     #修改元素集合标记的指针地址
#             else:
#                 return [x, y]


# https://leetcode-cn.com/problems/redundant-connection/solution/12xing-de-chun-chun-bing-cha-ji-by-tuotuoli/
