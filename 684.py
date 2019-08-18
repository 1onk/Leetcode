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



# https://leetcode-cn.com/problems/redundant-connection/solution/12xing-de-chun-chun-bing-cha-ji-by-tuotuoli/
