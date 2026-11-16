from typing import List
from collections import defaultdict


class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = defaultdict(int)
        ans = 0
        s = 0
        for point in points:
            x = cnt[point[1]]
            if x:
                ans += x * (s - x * (x - 1) // 2)
            s += x
            cnt[point[1]] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))
    print(solution.countTrapezoids([[0, 0], [1, 0], [0, 1], [2, 1]]))
