from typing import List
from collections import defaultdict


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        for num in nums:
            if cnt[k - num]:
                ans += 1
                cnt[k - num] -= 1
            else:
                cnt[num] += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxOperations([1, 2, 3, 4], 5))
    print(solution.maxOperations([3, 1, 3, 4, 3], 6))
