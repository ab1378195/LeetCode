from typing import List
from math import inf


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        ans = inf
        left = s = 0
        n = len(nums)
        total = sum(nums)
        remainder = target % total
        for right in range(2 * n):
            s += nums[right % n]
            while s > remainder:
                s -= nums[left % n]
                left += 1
            if s == remainder:
                ans = min(ans, right - left + 1)
        return -1 if ans == inf else ans + (target // total) * n


if __name__ == "__main__":
    solution = Solution()
    print(solution.minSizeSubarray([1, 2, 3], 5))
    print(solution.minSizeSubarray([1, 1, 1, 2, 3], 4))
    print(solution.minSizeSubarray([2, 4, 6, 8], 3))
