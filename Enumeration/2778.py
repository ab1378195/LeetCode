from typing import List
from math import isqrt


class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                ans += nums[i - 1] ** 2
                if i * i < n:
                    ans += nums[n // i - 1] ** 2
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.sumOfSquares([1, 2, 3, 4]))
    print(solution.sumOfSquares([2, 7, 1, 19, 18, 3]))
