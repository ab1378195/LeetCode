from collections import defaultdict
from bisect import bisect_left
from math import inf


class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        pos = defaultdict(list)
        for i, b in enumerate(s):
            pos[b].append(i)
        # 有向图
        g = defaultdict(list)
        for i, p in pos.items():
            left, right = p[0], p[-1]
            for j, q in pos.items():
                if j == i:
                    continue
                k = bisect_left(q, left)
                if k < len(q) and q[k] <= right:
                    g[i].append(j)

        def dfs(x: str) -> None:
            nonlocal left, right
            vis.add(x)
            p = pos[x]
            left = min(left, p[0])
            right = max(right, p[-1])
            for y in g[x]:
                if y not in vis:
                    dfs(y)

        intervals = []
        for i, p in pos.items():
            vis = set()
            left, right = inf, 0
            dfs(i)
            intervals.append((left, right))

        ans = []
        intervals.sort(key=lambda x: x[1])
        pre_r = -1
        for left, right in intervals:
            if left > pre_r:
                ans.append(s[left : right + 1])
                pre_r = right
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxNumOfSubstrings("adefaddaccc"))
    print(solution.maxNumOfSubstrings("abbaccd"))
