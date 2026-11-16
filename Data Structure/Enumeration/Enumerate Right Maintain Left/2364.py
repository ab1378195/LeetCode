from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for i, num in enumerate(nums):
            ans += cnt[num - i]
            cnt[num - i] += 1
        n = len(nums)
        return n * (n - 1) // 2 - ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.countBadPairs([4, 1, 3, 3]))
    print(solution.countBadPairs([1, 2, 3, 4, 5]))
