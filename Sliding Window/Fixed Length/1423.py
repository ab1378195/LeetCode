from typing import List
from math import inf


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        ans = inf
        s = 0
        k = len(cardPoints) - k
        if k == 0:
            return sum(cardPoints)
        for i, num in enumerate(cardPoints):
            s += num
            left = i - k + 1
            if left < 0:
                continue
            ans = min(ans, s)
            s -= cardPoints[left]
        return sum(cardPoints) - ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxScore([1, 2, 3, 4, 5, 6, 1], 3))
    print(solution.maxScore([2, 2, 2], 2))
    print(solution.maxScore([9, 7, 7, 9, 7, 7, 9], 7))
