from typing import List
from collections import defaultdict


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        count = defaultdict(int)
        ans = 0
        s = 0
        for i, num in enumerate(nums):
            s += num
            count[num] += 1
            left = i - k + 1
            if left < 0:
                continue
            if len(count) >= m:
                ans = max(ans, s)
            out = nums[left]
            s -= out
            count[out] -= 1
            if count[out] == 0:
                del count[out]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSum([2, 6, 7, 3, 1, 7], 3, 4))
    print(solution.maxSum([5, 9, 9, 2, 4, 5, 4], 1, 3))
    print(solution.maxSum([1, 2, 1, 2, 1, 2, 1], 3, 3))
