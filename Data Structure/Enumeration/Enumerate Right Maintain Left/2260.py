from typing import List
from math import inf


class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        has = {}
        ans = inf
        for i, card in enumerate(cards):
            if card in has:
                ans = min(ans, i - has[card] + 1)
            has[card] = i
        return -1 if ans == inf else ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.minimumCardPickup([3, 4, 2, 3, 4, 7]))
    print(solution.minimumCardPickup([1, 0, 5, 3]))
