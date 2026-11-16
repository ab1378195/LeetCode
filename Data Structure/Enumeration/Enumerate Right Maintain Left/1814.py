from typing import List
from collections import defaultdict


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for num in nums:
            temp = num
            rev = 0
            while temp > 0:
                rev = 10 * rev + temp % 10
                temp //= 10
            ans += cnt[num - rev]
            cnt[num - rev] += 1
        return ans % 1_000_000_007


if __name__ == "__main__":
    solution = Solution()
    print(solution.countNicePairs([42, 11, 1, 97]))
    print(solution.countNicePairs([13, 10, 35, 24, 76]))
