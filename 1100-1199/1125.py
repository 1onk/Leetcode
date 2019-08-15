"""
1125. 最小的必要团队
地址：https://leetcode-cn.com/problems/smallest-sufficient-team/

参考题解：https://leetcode-cn.com/problems/smallest-sufficient-team/solution/smallest-sufficient-team-by-xiaohejun/
"""
class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        skill_dict = {}
        for i in range(len(req_skills)):
            skill_dict[req_skills[i]] = i
        n = len(req_skills)
        dp = [-1 for _ in range(1 << n)]
        team = [[] for _ in range(1 << n)]
        dp[0] = 0
        for i in range(len(people)):
            now = 0
            curr_people_skill = people[i]
            for j in curr_people_skill:
                x = skill_dict[j]
                now |= (1 << x)

            for j in range(1 << len(req_skills)):
                if dp[j] >= 0:
                    x = now | j
                    if dp[x] == -1 or dp[x] > dp[j] + 1:
                        dp[x] = dp[j] + 1
                        team[x] = team[j][:]
                        team[x].append(i)
        return team[(1 << n) - 1]