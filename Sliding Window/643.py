from typing import List
from math import inf


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        ans = -inf
        for i, num in enumerate(nums):
            sum += num
            left = i - k + 1
            if left < 0:
                continue
            ans = max(ans, sum)
            sum -= nums[left]
        return ans / k


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
    print(solution.findMaxAverage([5], 1))
