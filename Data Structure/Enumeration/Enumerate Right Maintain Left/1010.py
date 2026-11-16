from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for num in time:
            key = num % 60
            ans += cnt[60 - key]
            if key == 0:
                cnt[60] += 1
            else:
                cnt[key] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
    print(solution.numPairsDivisibleBy60([60, 60, 60]))
