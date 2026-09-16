from typing import List
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        ans = 0
        s = 0
        for i, num in enumerate(nums):
            s += num
            cnt[num] += 1
            left = i - k + 1
            if left < 0:
                continue
            if len(cnt) == k:
                ans = max(ans, s)
            out = nums[left]
            s -= out
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3))
    print(solution.maximumSubarraySum([4, 4, 4], 3))
