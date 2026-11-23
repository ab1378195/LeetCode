from typing import List
from collections import defaultdict


class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)
        size = [1] * n
        ancestor = defaultdict(lambda: -1)

        def dfs(x: int) -> None:
            old = ancestor[s[x]]
            ancestor[s[x]] = x
            for y in g[x]:
                dfs(y)
                anc = ancestor[s[y]]
                size[x if anc < 0 else anc] += size[y]
            ancestor[s[x]] = old

        dfs(0)
        return size


if __name__ == "__main__":
    solution = Solution()
    print(solution.findSubtreeSizes([-1, 0, 0, 1, 1, 1], "abaabc"))
    print(solution.findSubtreeSizes([-1, 0, 4, 0, 1], "abbba"))
