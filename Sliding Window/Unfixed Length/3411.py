from typing import List
from math import gcd


class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 2
        mul = 1
        left = 0
        for right, num in enumerate(nums):
            while gcd(mul, num) > 1:
                mul //= nums[left]
                left += 1
            mul *= num
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxLength([1, 2, 1, 2, 1, 1, 1]))
    print(solution.maxLength([2, 3, 4, 5, 6]))
    print(solution.maxLength([1, 2, 3, 1, 4, 5, 1]))
