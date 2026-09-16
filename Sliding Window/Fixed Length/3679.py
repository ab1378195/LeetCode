from typing import List
from collections import defaultdict


class Solution:
    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for i, arrival in enumerate(arrivals):
            if cnt[arrival] == m:
                arrivals[i] = 0
                ans += 1
            else:
                cnt[arrival] += 1
            left = i - w + 1
            if left >= 0:
                cnt[arrivals[left]] -= 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minArrivalsToDiscard([1, 2, 1, 3, 1], 4, 2))
    print(solution.minArrivalsToDiscard([1, 2, 3, 3, 3, 4], 3, 2))
