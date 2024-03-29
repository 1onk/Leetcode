class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        # 答案数组
        ans = [-1] * n
        ans[0] = 0
        # 访问过的结点
        visited = set()
        visited.add((0, True))
        visited.add((0, False))
        # 初始结点
        q = [(0, True), (0, False)]
        # 红色边和蓝色边
        r = collections.defaultdict(set)
        b = collections.defaultdict(set)
        for e in red_edges:
            r[e[0]].add(e[1])
        for e in blue_edges:
            b[e[0]].add(e[1])
        # 步数
        step = 0
        # BFS
        while q:
            step += 1
            t = []
            while q:
                node, color = q.pop()
                if color and node in r:
                    for next_node in r[node]:
                        if (next_node, False) not in visited:
                            visited.add((next_node, False))
                            if ans[next_node] == -1:
                                ans[next_node] = step
                            t.append((next_node, False))
                elif not color and node in b:
                    for next_node in b[node]:
                        if (next_node, True) not in visited:
                            if ans[next_node] == -1:
                                ans[next_node] = step
                            t.append((next_node, True))
            q = t
        return ans