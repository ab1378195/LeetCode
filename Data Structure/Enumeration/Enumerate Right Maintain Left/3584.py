from typing import List
from math import inf


class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = positive = -inf
        negative = inf
        for i, num in enumerate(nums[m - 1 :], m - 1):
            positive = max(positive, nums[i - m + 1])
            negative = min(negative, nums[i - m + 1])
            ans = max(ans, num * negative, num * positive)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumProduct([-1, -9, 2, 3, -2, -3, 1], 1))
    print(solution.maximumProduct([1, 3, -5, 5, 6, -4], 3))
    print(solution.maximumProduct([2, -1, 2, -6, 5, 2, -5, 7], 2))
