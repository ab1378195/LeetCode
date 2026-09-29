from typing import List
from collections import defaultdict


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for right, num in enumerate(nums):
            cnt[num] += 1
            while cnt[num] > k:
                cnt[nums[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2))
    print(solution.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1))
    print(solution.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4))
